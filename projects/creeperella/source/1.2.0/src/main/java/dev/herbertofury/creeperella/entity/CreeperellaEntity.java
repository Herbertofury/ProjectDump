package dev.herbertofury.creeperella.entity;

import dev.herbertofury.creeperella.config.CreeperellaConfig;
import dev.herbertofury.creeperella.registry.ModEntities;
import net.minecraft.core.BlockPos;
import net.minecraft.core.Direction;
import net.minecraft.core.particles.ParticleOptions;
import net.minecraft.core.particles.ParticleTypes;
import net.minecraft.nbt.CompoundTag;
import net.minecraft.resources.ResourceLocation;
import net.minecraft.server.level.ServerLevel;
import net.minecraft.server.level.ServerPlayer;
import net.minecraft.sounds.SoundEvents;
import net.minecraft.world.entity.Entity;
import net.minecraft.world.entity.EntityType;
import net.minecraft.world.entity.LivingEntity;
import net.minecraft.world.entity.TamableAnimal;
import net.minecraft.world.entity.monster.Creeper;
import net.minecraft.world.entity.player.Player;
import net.minecraft.world.level.Level;
import net.minecraft.world.phys.Vec3;

import java.util.UUID;

public class CreeperellaEntity extends Creeper {
    private static final String TAG_MAKEOVER_GRACE = "CreeperellaMakeoverGrace";
    private static final String TAG_MAKEOVER_FRIEND = "CreeperellaMakeoverFriend";
    private static final String TAG_TAMED = "CreeperellaTamed";
    private static final String TAG_OWNER = "CreeperellaOwner";
    private static final String TAG_SITTING = "CreeperellaSitting";
    private static final String TAG_BOND = "CreeperellaBond";
    private static final String TAG_COOLDOWN = "CreeperellaDetonationCooldown";
    private static final String TAG_REFORM = "CreeperellaReformTicks";
    private static final String TAG_COMMAND_TARGET = "CreeperellaCommandTarget";
    private static final String TAG_COMMAND_TICKS = "CreeperellaCommandTicks";

    private int makeoverGraceTicks;
    private UUID makeoverFriend;

    private boolean companionTamed;
    private UUID ownerUuid;
    private boolean orderedToSit;
    private int bondProgress;
    private int detonationCooldownTicks;
    private int reformTicks;
    private UUID commandTargetUuid;
    private int commandChaseTicks;

    public CreeperellaEntity(EntityType<? extends CreeperellaEntity> type, Level level) {
        super(type, level);
    }

    public CreeperellaKind kind() {
        return ModEntities.kindOf(this.getType());
    }

    public boolean isCompanionTamed() {
        return companionTamed;
    }

    public UUID getOwnerUuid() {
        return ownerUuid;
    }

    public boolean isOwnedBy(Player player) {
        return companionTamed && ownerUuid != null && ownerUuid.equals(player.getUUID());
    }

    public boolean isOrderedToSit() {
        return orderedToSit;
    }

    public int getBondProgress() {
        return bondProgress;
    }

    public int getDetonationCooldownTicks() {
        return Math.max(0, detonationCooldownTicks);
    }

    public int getReformTicks() {
        return Math.max(0, reformTicks);
    }

    public boolean isReforming() {
        return reformTicks > 0;
    }

    public boolean isReadyToDetonate() {
        return companionTamed && !isReforming() && detonationCooldownTicks <= 0;
    }

    public void tameTo(Player player) {
        this.companionTamed = true;
        this.ownerUuid = player.getUUID();
        this.orderedToSit = false;
        this.bondProgress = 0;
        this.commandTargetUuid = null;
        this.commandChaseTicks = 0;
        this.setTarget(null);
        this.setSwellDir(-1);
        this.setPersistenceRequired();
        this.heal(this.getMaxHealth());
    }

    public int addBondProgress() {
        this.bondProgress = Math.min(CreeperellaConfig.TAME_TREATS_REQUIRED.get(), this.bondProgress + 1);
        return this.bondProgress;
    }

    public boolean toggleSitting(Player player) {
        if (!isOwnedBy(player) || isReforming()) {
            return false;
        }
        this.orderedToSit = !this.orderedToSit;
        this.commandTargetUuid = null;
        this.commandChaseTicks = 0;
        this.setTarget(null);
        this.setSwellDir(-1);
        this.getNavigation().stop();
        return true;
    }

    public boolean commandTarget(Player player, LivingEntity target) {
        if (!CreeperellaConfig.ENABLE_COMPANIONS.get() || !isOwnedBy(player) || !isReadyToDetonate()) {
            return false;
        }
        if (!isValidCommandTarget(player, target)) {
            return false;
        }
        this.orderedToSit = false;
        this.commandTargetUuid = target.getUUID();
        this.commandChaseTicks = 0;
        this.setTarget(target);
        this.setSwellDir(-1);
        this.getNavigation().moveTo(target, CreeperellaConfig.COMPANION_MOVE_SPEED.get());
        return true;
    }

    public boolean commandDetonateNow(Player player) {
        if (!CreeperellaConfig.ENABLE_COMPANIONS.get() || !isOwnedBy(player) || !isReadyToDetonate()) {
            return false;
        }
        performCompanionExplosion();
        return true;
    }

    public boolean recallTo(Player player) {
        if (!CreeperellaConfig.ENABLE_COMPANIONS.get() || !isOwnedBy(player) || isReforming()) {
            return false;
        }
        this.orderedToSit = false;
        this.commandTargetUuid = null;
        this.commandChaseTicks = 0;
        this.setTarget(null);
        this.setSwellDir(-1);
        this.getNavigation().stop();
        return safeTeleportNear(player);
    }

    public boolean isOwnedAlly(LivingEntity entity) {
        if (!companionTamed || ownerUuid == null || entity == null) {
            return false;
        }
        if (ownerUuid.equals(entity.getUUID())) {
            return true;
        }
        if (entity instanceof Player player) {
            ServerPlayer owner = getOwnerPlayer();
            return owner != null && owner.isAlliedTo(player);
        }
        if (entity instanceof CreeperellaEntity other) {
            return other.isCompanionTamed() && ownerUuid.equals(other.getOwnerUuid());
        }
        if (entity instanceof TamableAnimal pet) {
            return ownerUuid.equals(pet.getOwnerUUID());
        }
        return false;
    }

    public boolean isValidCommandTarget(Player owner, LivingEntity target) {
        if (target == null || !target.isAlive() || target == this || target.isSpectator()) {
            return false;
        }
        if (target.getUUID().equals(owner.getUUID()) || owner.isAlliedTo(target) || isOwnedAlly(target)) {
            return false;
        }
        if (target instanceof Player targetPlayer && targetPlayer.isCreative()) {
            return false;
        }
        return true;
    }

    /**
     * Gives the player who performed a transformation a short non-hostile window.
     * A tamed Creeperella ignores normal hostile targeting permanently; this grace is for wild makeovers.
     */
    public void grantMakeoverGrace(Player player) {
        this.makeoverFriend = player.getUUID();
        this.makeoverGraceTicks = CreeperellaConfig.MAKEOVER_GRACE_TICKS.get();
        this.setTarget(null);
        this.setSwellDir(-1);
    }

    public boolean hasMakeoverGraceFor(LivingEntity entity) {
        return this.makeoverGraceTicks > 0
                && this.makeoverFriend != null
                && this.makeoverFriend.equals(entity.getUUID());
    }

    @Override
    protected ResourceLocation getDefaultLootTable() {
        return EntityType.CREEPER.getDefaultLootTable();
    }

    /**
     * Hard safety boundary for companions: no vanilla AI, modded goal, or stale ignition state may
     * ever push a tamed Creeperella into Creeper's destructive one-life fuse path. Companion
     * detonations are only performed through the reusable command/reformation system.
     */
    @Override
    public void setSwellDir(int direction) {
        if (this.companionTamed && direction > 0) {
            super.setSwellDir(-1);
            return;
        }
        super.setSwellDir(direction);
    }

    @Override
    public void ignite() {
        if (!this.companionTamed) {
            super.ignite();
        }
    }

    @Override
    public void aiStep() {
        // Tamed companions never use the vanilla self-destructive fuse. Their explosions are deliberate,
        // reusable commands handled below, so a stray target-selector tick can never destroy the pet.
        if (!this.level().isClientSide && this.companionTamed) {
            this.setSwellDir(-1);
        }

        super.aiStep();

        if (!this.level().isClientSide) {
            tickMakeoverGrace();
            tickCompanion();
            return;
        }

        if (!CreeperellaConfig.AMBIENT_PARTICLES.get() || this.random.nextInt(34) != 0 || this.isInvisible()) {
            return;
        }

        ParticleOptions particle = switch (this.kind()) {
            case BUNNY -> this.random.nextBoolean() ? ParticleTypes.HEART : ParticleTypes.POOF;
            case BEE -> this.random.nextBoolean() ? ParticleTypes.FALLING_NECTAR : ParticleTypes.WAX_ON;
            case CHERRY -> ParticleTypes.CHERRY_LEAVES;
            case BLOSSOM -> this.random.nextBoolean() ? ParticleTypes.CHERRY_LEAVES : ParticleTypes.HEART;
            case FEMALE -> ParticleTypes.HEART;
        };

        double x = this.getX() + (this.random.nextDouble() - 0.5D) * 0.7D;
        double y = this.getY() + 0.7D + this.random.nextDouble() * 0.9D;
        double z = this.getZ() + (this.random.nextDouble() - 0.5D) * 0.7D;
        this.level().addParticle(particle, x, y, z, 0.0D, 0.01D, 0.0D);
    }

    private void tickCompanion() {
        if (this.detonationCooldownTicks > 0) {
            --this.detonationCooldownTicks;
        }

        if (!this.companionTamed || !CreeperellaConfig.ENABLE_COMPANIONS.get()) {
            return;
        }

        this.setPersistenceRequired();
        this.setSwellDir(-1);

        if (this.reformTicks > 0) {
            tickReforming();
            return;
        }

        this.setInvisible(false);
        this.setInvulnerable(false);
        this.noPhysics = false;

        if (this.orderedToSit) {
            this.commandTargetUuid = null;
            this.commandChaseTicks = 0;
            this.setTarget(null);
            this.getNavigation().stop();
            this.setDeltaMovement(Vec3.ZERO);
            return;
        }

        LivingEntity commandTarget = resolveCommandTarget();
        if (commandTarget != null) {
            tickCommandAttack(commandTarget);
            return;
        }

        // Suppress all vanilla hostile targets while tamed. A companion attacks only a whistle-designated target.
        if (this.getTarget() != null) {
            this.setTarget(null);
        }
        tickFollowOwner();
    }

    private void tickCommandAttack(LivingEntity target) {
        ServerPlayer owner = getOwnerPlayer();
        if (owner == null || !isValidCommandTarget(owner, target)) {
            clearCommandTarget();
            return;
        }

        ++this.commandChaseTicks;
        int timeout = CreeperellaConfig.COMMAND_TIMEOUT_TICKS.get();
        double maxRange = CreeperellaConfig.COMMAND_RANGE.get();
        if (this.commandChaseTicks > timeout || this.distanceToSqr(target) > maxRange * maxRange) {
            clearCommandTarget();
            return;
        }

        this.setTarget(target);
        this.setSwellDir(-1);
        this.getLookControl().setLookAt(target, 20.0F, this.getMaxHeadXRot());
        if (this.tickCount % 5 == 0 || this.getNavigation().isDone()) {
            this.getNavigation().moveTo(target, CreeperellaConfig.COMPANION_MOVE_SPEED.get());
        }

        double trigger = CreeperellaConfig.DETONATION_TRIGGER_DISTANCE.get();
        if (this.distanceToSqr(target) <= trigger * trigger && this.hasLineOfSight(target)) {
            performCompanionExplosion();
        }
    }

    private void tickFollowOwner() {
        ServerPlayer owner = getOwnerPlayer();
        if (owner == null || owner.level() != this.level() || owner.isSpectator()) {
            this.getNavigation().stop();
            return;
        }

        double distanceSq = this.distanceToSqr(owner);
        double teleportDistance = CreeperellaConfig.FOLLOW_TELEPORT_DISTANCE.get();
        if (distanceSq > teleportDistance * teleportDistance) {
            safeTeleportNear(owner);
            return;
        }

        double start = CreeperellaConfig.FOLLOW_START_DISTANCE.get();
        double stop = CreeperellaConfig.FOLLOW_STOP_DISTANCE.get();
        if (distanceSq > start * start) {
            this.getLookControl().setLookAt(owner, 10.0F, this.getMaxHeadXRot());
            if (this.tickCount % 10 == 0 || this.getNavigation().isDone()) {
                this.getNavigation().moveTo(owner, CreeperellaConfig.COMPANION_MOVE_SPEED.get());
            }
        } else if (distanceSq < stop * stop) {
            this.getNavigation().stop();
        }
    }

    private void performCompanionExplosion() {
        if (!(this.level() instanceof ServerLevel serverLevel) || !this.isReadyToDetonate()) {
            return;
        }

        ServerPlayer owner = getOwnerPlayer();
        this.clearCommandTarget();
        this.getNavigation().stop();
        this.setSwellDir(-1);
        this.setInvulnerable(true);
        this.setInvisible(true);
        this.noPhysics = true;
        this.setDeltaMovement(Vec3.ZERO);

        float power = this.isPowered()
                ? CreeperellaConfig.CHARGED_FOLLOWER_EXPLOSION_POWER.get().floatValue()
                : CreeperellaConfig.FOLLOWER_EXPLOSION_POWER.get().floatValue();
        Level.ExplosionInteraction interaction = CreeperellaConfig.FOLLOWER_EXPLOSIONS_BREAK_BLOCKS.get()
                ? Level.ExplosionInteraction.MOB
                : Level.ExplosionInteraction.NONE;

        double blastX = this.getX();
        double blastY = this.getY();
        double blastZ = this.getZ();
        serverLevel.explode(this, blastX, blastY, blastZ, power, false, interaction);
        serverLevel.sendParticles(ParticleTypes.POOF, blastX, blastY + 0.8D, blastZ,
                24, 0.55D, 0.7D, 0.55D, 0.08D);

        this.detonationCooldownTicks = this.isPowered()
                ? CreeperellaConfig.CHARGED_DETONATION_COOLDOWN_TICKS.get()
                : CreeperellaConfig.DETONATION_COOLDOWN_TICKS.get();
        this.reformTicks = Math.max(1, CreeperellaConfig.REFORM_TICKS.get());

        // Move the hidden, invulnerable entity beside its owner immediately so its chunk stays loaded.
        // The visible "respawn" happens only after the configurable reform timer expires.
        if (owner != null && owner.level() == this.level()) {
            safeTeleportNear(owner);
        }
    }

    private void tickReforming() {
        this.setTarget(null);
        this.setSwellDir(-1);
        this.getNavigation().stop();
        this.setInvulnerable(true);
        this.setInvisible(true);
        this.noPhysics = true;
        this.setDeltaMovement(Vec3.ZERO);

        ServerPlayer owner = getOwnerPlayer();
        if (owner != null && owner.level() == this.level() && this.tickCount % 20 == 0) {
            safeTeleportNear(owner);
        }

        --this.reformTicks;
        if (this.reformTicks > 0) {
            return;
        }

        if (owner == null || owner.level() != this.level()) {
            // Keep the companion safely phased out until its owner is available in the same dimension.
            this.reformTicks = 20;
            return;
        }

        safeTeleportNear(owner);
        this.noPhysics = false;
        this.setInvisible(false);
        this.setInvulnerable(false);
        this.heal(this.getMaxHealth());
        this.level().playSound(null, this.blockPosition(), SoundEvents.AMETHYST_BLOCK_CHIME,
                this.getSoundSource(), 0.9F, 1.35F);
        if (this.level() instanceof ServerLevel serverLevel) {
            serverLevel.sendParticles(ParticleTypes.HEART, this.getX(), this.getY() + 1.0D, this.getZ(),
                    8, 0.35D, 0.45D, 0.35D, 0.03D);
            serverLevel.sendParticles(ParticleTypes.POOF, this.getX(), this.getY() + 0.7D, this.getZ(),
                    18, 0.4D, 0.5D, 0.4D, 0.05D);
        }
    }

    private LivingEntity resolveCommandTarget() {
        if (this.commandTargetUuid == null || !(this.level() instanceof ServerLevel serverLevel)) {
            return null;
        }
        Entity entity = serverLevel.getEntity(this.commandTargetUuid);
        if (entity instanceof LivingEntity living && living.isAlive()) {
            return living;
        }
        clearCommandTarget();
        return null;
    }

    private void clearCommandTarget() {
        this.commandTargetUuid = null;
        this.commandChaseTicks = 0;
        this.setTarget(null);
        this.setSwellDir(-1);
    }

    private ServerPlayer getOwnerPlayer() {
        if (this.ownerUuid == null || !(this.level() instanceof ServerLevel serverLevel)) {
            return null;
        }
        return serverLevel.getServer().getPlayerList().getPlayer(this.ownerUuid);
    }

    private boolean safeTeleportNear(Player player) {
        if (!(this.level() instanceof ServerLevel serverLevel) || player.level() != this.level()) {
            return false;
        }

        BlockPos origin = player.blockPosition();
        int[][] offsets = {
                {2, 0}, {-2, 0}, {0, 2}, {0, -2},
                {2, 2}, {-2, 2}, {2, -2}, {-2, -2},
                {1, 0}, {-1, 0}, {0, 1}, {0, -1}
        };
        for (int[] offset : offsets) {
            for (int dy = 1; dy >= -1; --dy) {
                BlockPos pos = origin.offset(offset[0], dy, offset[1]);
                if (!serverLevel.isEmptyBlock(pos) || !serverLevel.isEmptyBlock(pos.above())) {
                    continue;
                }
                BlockPos below = pos.below();
                if (!serverLevel.getBlockState(below).isFaceSturdy(serverLevel, below, Direction.UP)) {
                    continue;
                }
                this.teleportTo(pos.getX() + 0.5D, pos.getY(), pos.getZ() + 0.5D);
                this.setDeltaMovement(Vec3.ZERO);
                return true;
            }
        }

        this.teleportTo(player.getX(), player.getY(), player.getZ());
        this.setDeltaMovement(Vec3.ZERO);
        return true;
    }

    private void tickMakeoverGrace() {
        if (this.makeoverGraceTicks <= 0) {
            return;
        }

        --this.makeoverGraceTicks;
        LivingEntity target = this.getTarget();
        if (target != null && hasMakeoverGraceFor(target)) {
            this.setTarget(null);
            this.setSwellDir(-1);
        }

        if (this.makeoverGraceTicks == 0) {
            this.makeoverFriend = null;
        }
    }

    @Override
    public void addAdditionalSaveData(CompoundTag tag) {
        super.addAdditionalSaveData(tag);
        if (this.makeoverGraceTicks > 0) {
            tag.putInt(TAG_MAKEOVER_GRACE, this.makeoverGraceTicks);
            if (this.makeoverFriend != null) {
                tag.putUUID(TAG_MAKEOVER_FRIEND, this.makeoverFriend);
            }
        }

        tag.putBoolean(TAG_TAMED, this.companionTamed);
        tag.putBoolean(TAG_SITTING, this.orderedToSit);
        tag.putInt(TAG_BOND, this.bondProgress);
        tag.putInt(TAG_COOLDOWN, this.detonationCooldownTicks);
        tag.putInt(TAG_REFORM, this.reformTicks);
        tag.putInt(TAG_COMMAND_TICKS, this.commandChaseTicks);
        if (this.ownerUuid != null) {
            tag.putUUID(TAG_OWNER, this.ownerUuid);
        }
        if (this.commandTargetUuid != null) {
            tag.putUUID(TAG_COMMAND_TARGET, this.commandTargetUuid);
        }
    }

    @Override
    public void readAdditionalSaveData(CompoundTag tag) {
        super.readAdditionalSaveData(tag);
        this.makeoverGraceTicks = Math.max(0, tag.getInt(TAG_MAKEOVER_GRACE));
        this.makeoverFriend = tag.hasUUID(TAG_MAKEOVER_FRIEND) ? tag.getUUID(TAG_MAKEOVER_FRIEND) : null;

        this.companionTamed = tag.getBoolean(TAG_TAMED);
        this.ownerUuid = tag.hasUUID(TAG_OWNER) ? tag.getUUID(TAG_OWNER) : null;
        this.orderedToSit = tag.getBoolean(TAG_SITTING);
        this.bondProgress = Math.max(0, tag.getInt(TAG_BOND));
        this.detonationCooldownTicks = Math.max(0, tag.getInt(TAG_COOLDOWN));
        this.reformTicks = Math.max(0, tag.getInt(TAG_REFORM));
        this.commandTargetUuid = tag.hasUUID(TAG_COMMAND_TARGET) ? tag.getUUID(TAG_COMMAND_TARGET) : null;
        this.commandChaseTicks = Math.max(0, tag.getInt(TAG_COMMAND_TICKS));
        if (this.companionTamed) {
            this.setPersistenceRequired();
            this.setSwellDir(-1);
        }
    }
}
