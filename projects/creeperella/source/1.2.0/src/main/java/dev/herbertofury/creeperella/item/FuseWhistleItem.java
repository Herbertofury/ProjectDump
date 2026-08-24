package dev.herbertofury.creeperella.item;

import dev.herbertofury.creeperella.config.CreeperellaConfig;
import dev.herbertofury.creeperella.entity.CreeperellaEntity;
import net.minecraft.ChatFormatting;
import net.minecraft.nbt.CompoundTag;
import net.minecraft.network.chat.Component;
import net.minecraft.server.level.ServerLevel;
import net.minecraft.world.InteractionHand;
import net.minecraft.world.InteractionResult;
import net.minecraft.world.InteractionResultHolder;
import net.minecraft.world.entity.Entity;
import net.minecraft.world.entity.LivingEntity;
import net.minecraft.world.entity.player.Player;
import net.minecraft.world.entity.projectile.ProjectileUtil;
import net.minecraft.world.item.Item;
import net.minecraft.world.item.ItemStack;
import net.minecraft.world.level.Level;
import net.minecraft.world.phys.AABB;
import net.minecraft.world.phys.EntityHitResult;
import net.minecraft.world.phys.HitResult;
import net.minecraft.world.phys.Vec3;

import java.util.Comparator;
import java.util.List;
import java.util.UUID;

public final class FuseWhistleItem extends Item {
    private static final String TAG_BOUND = "CreeperellaBoundCompanion";

    public FuseWhistleItem(Properties properties) {
        super(properties);
    }

    @Override
    public InteractionResult interactLivingEntity(ItemStack stack, Player player, LivingEntity target, InteractionHand hand) {
        if (!CreeperellaConfig.ENABLE_COMPANIONS.get()) {
            return InteractionResult.PASS;
        }

        if (target instanceof CreeperellaEntity companion) {
            if (!companion.isOwnedBy(player)) {
                return InteractionResult.PASS;
            }
            if (!player.level().isClientSide) {
                bind(stack, companion);
                player.displayClientMessage(Component.literal("Fuse Whistle bound to ")
                        .append(companion.getDisplayName()).withStyle(ChatFormatting.LIGHT_PURPLE), true);
            }
            return InteractionResult.sidedSuccess(player.level().isClientSide);
        }

        if (player.level().isClientSide) {
            return InteractionResult.SUCCESS;
        }

        CreeperellaEntity companion = resolveCompanion(stack, player, true);
        if (companion == null) {
            player.displayClientMessage(Component.literal("No ready Creeperella companion is in command range.")
                    .withStyle(ChatFormatting.RED), true);
            return InteractionResult.CONSUME;
        }

        if (!companion.isValidCommandTarget(player, target)) {
            player.displayClientMessage(Component.literal("That target is protected from your Creeperella.")
                    .withStyle(ChatFormatting.YELLOW), true);
            return InteractionResult.CONSUME;
        }

        if (!companion.commandTarget(player, target)) {
            showCooldown(player, companion);
            return InteractionResult.CONSUME;
        }

        player.displayClientMessage(Component.literal("Boom run: ")
                .append(companion.getDisplayName())
                .append(Component.literal(" -> "))
                .append(target.getDisplayName())
                .withStyle(ChatFormatting.GOLD), true);
        return InteractionResult.CONSUME;
    }

    @Override
    public InteractionResultHolder<ItemStack> use(Level level, Player player, InteractionHand hand) {
        ItemStack stack = player.getItemInHand(hand);
        if (!CreeperellaConfig.ENABLE_COMPANIONS.get()) {
            return InteractionResultHolder.pass(stack);
        }
        if (level.isClientSide) {
            return InteractionResultHolder.success(stack);
        }

        if (player.isShiftKeyDown()) {
            CreeperellaEntity companion = resolveCompanion(stack, player, true);
            if (companion == null) {
                player.displayClientMessage(Component.literal("No ready Creeperella companion is in command range.")
                        .withStyle(ChatFormatting.RED), true);
                return InteractionResultHolder.consume(stack);
            }
            if (!companion.commandDetonateNow(player)) {
                showCooldown(player, companion);
            } else {
                player.displayClientMessage(Component.literal("BOOM! She'll reform beside you shortly.")
                        .withStyle(ChatFormatting.GOLD), true);
            }
            return InteractionResultHolder.consume(stack);
        }

        LivingEntity aimedTarget = findLongRangeTarget(player);
        if (aimedTarget != null) {
            CreeperellaEntity companion = resolveCompanion(stack, player, true);
            if (companion == null) {
                player.displayClientMessage(Component.literal("No ready Creeperella companion is in command range.")
                        .withStyle(ChatFormatting.RED), true);
                return InteractionResultHolder.consume(stack);
            }
            if (!companion.isValidCommandTarget(player, aimedTarget)) {
                player.displayClientMessage(Component.literal("That target is protected from your Creeperella.")
                        .withStyle(ChatFormatting.YELLOW), true);
                return InteractionResultHolder.consume(stack);
            }
            if (!companion.commandTarget(player, aimedTarget)) {
                showCooldown(player, companion);
                return InteractionResultHolder.consume(stack);
            }
            player.displayClientMessage(Component.literal("Boom run: ")
                    .append(companion.getDisplayName())
                    .append(Component.literal(" -> "))
                    .append(aimedTarget.getDisplayName())
                    .withStyle(ChatFormatting.GOLD), true);
            return InteractionResultHolder.consume(stack);
        }

        CreeperellaEntity companion = resolveCompanion(stack, player, false);
        if (companion == null) {
            player.displayClientMessage(Component.literal("No Creeperella companion is in command range.")
                    .withStyle(ChatFormatting.RED), true);
            return InteractionResultHolder.consume(stack);
        }
        if (companion.recallTo(player)) {
            player.displayClientMessage(Component.literal("Recalled ")
                    .append(companion.getDisplayName()).withStyle(ChatFormatting.LIGHT_PURPLE), true);
        } else if (companion.isReforming()) {
            showCooldown(player, companion);
        }

        return InteractionResultHolder.consume(stack);
    }

    private static LivingEntity findLongRangeTarget(Player player) {
        double range = CreeperellaConfig.COMMAND_RANGE.get();
        Vec3 eye = player.getEyePosition();
        Vec3 look = player.getViewVector(1.0F);

        // Respect walls: first clip the view ray against blocks, then only search entities along
        // the unobstructed section. This makes the whistle feel deliberate instead of x-ray targeting.
        HitResult blockHit = player.pick(range, 1.0F, false);
        double visibleRange = range;
        if (blockHit.getType() != HitResult.Type.MISS) {
            visibleRange = Math.min(range, eye.distanceTo(blockHit.getLocation()));
        }

        Vec3 end = eye.add(look.scale(visibleRange));
        AABB searchBox = player.getBoundingBox().expandTowards(look.scale(visibleRange)).inflate(1.0D);
        EntityHitResult hit = ProjectileUtil.getEntityHitResult(
                player, eye, end, searchBox,
                entity -> entity instanceof LivingEntity living
                        && living.isAlive()
                        && living != player
                        && living.isPickable()
                        && !living.isSpectator(),
                visibleRange * visibleRange);
        return hit != null && hit.getEntity() instanceof LivingEntity living ? living : null;
    }

    private static void bind(ItemStack stack, CreeperellaEntity companion) {
        stack.getOrCreateTag().putUUID(TAG_BOUND, companion.getUUID());
    }

    private static CreeperellaEntity resolveCompanion(ItemStack stack, Player player, boolean requireReady) {
        if (!(player.level() instanceof ServerLevel serverLevel)) {
            return null;
        }

        CompoundTag tag = stack.getTag();
        if (tag != null && tag.hasUUID(TAG_BOUND)) {
            UUID id = tag.getUUID(TAG_BOUND);
            Entity entity = serverLevel.getEntity(id);
            double commandRange = CreeperellaConfig.COMMAND_RANGE.get();
            if (entity instanceof CreeperellaEntity companion
                    && companion.isOwnedBy(player)
                    && companion.distanceToSqr(player) <= commandRange * commandRange) {
                // A bound companion stays authoritative even while cooling down so the whistle can
                // report its remaining recharge instead of silently switching to a different pet.
                if (!requireReady || companion.isReadyToDetonate()) {
                    return companion;
                }
                return companion;
            }
        }

        double range = CreeperellaConfig.COMMAND_RANGE.get();
        AABB box = player.getBoundingBox().inflate(range);
        List<CreeperellaEntity> companions = serverLevel.getEntitiesOfClass(CreeperellaEntity.class, box,
                c -> c.isOwnedBy(player) && !c.isReforming() && (!requireReady || c.isReadyToDetonate()));
        return companions.stream().min(Comparator.comparingDouble(player::distanceToSqr)).orElse(null);
    }

    private static void showCooldown(Player player, CreeperellaEntity companion) {
        if (companion.isReforming()) {
            player.displayClientMessage(Component.literal("She's still reforming.")
                    .withStyle(ChatFormatting.YELLOW), true);
            return;
        }
        int ticks = companion.getDetonationCooldownTicks();
        int seconds = Math.max(1, (ticks + 19) / 20);
        player.displayClientMessage(Component.literal("Detonation recharging: " + seconds + "s")
                .withStyle(ChatFormatting.YELLOW), true);
    }
}
