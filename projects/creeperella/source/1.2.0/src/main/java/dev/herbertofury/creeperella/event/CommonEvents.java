package dev.herbertofury.creeperella.event;

import dev.herbertofury.creeperella.Creeperella;
import dev.herbertofury.creeperella.config.CreeperellaConfig;
import dev.herbertofury.creeperella.entity.CreeperellaEntity;
import dev.herbertofury.creeperella.entity.CreeperellaKind;
import dev.herbertofury.creeperella.registry.ModEntities;
import dev.herbertofury.creeperella.registry.ModItems;
import net.minecraft.ChatFormatting;
import net.minecraft.core.particles.ParticleTypes;
import net.minecraft.nbt.CompoundTag;
import net.minecraft.network.chat.Component;
import net.minecraft.resources.ResourceLocation;
import net.minecraft.server.level.ServerLevel;
import net.minecraft.server.level.ServerPlayer;
import net.minecraft.sounds.SoundEvents;
import net.minecraft.world.InteractionResult;
import net.minecraft.world.entity.Entity;
import net.minecraft.world.entity.EntityType;
import net.minecraft.world.entity.LivingEntity;
import net.minecraft.world.entity.monster.Creeper;
import net.minecraft.world.entity.player.Player;
import net.minecraft.world.item.Item;
import net.minecraft.world.item.ItemStack;
import net.minecraft.world.item.Items;
import net.minecraftforge.event.entity.living.LivingAttackEvent;
import net.minecraftforge.event.level.ExplosionEvent;
import net.minecraftforge.event.entity.player.PlayerInteractEvent;
import net.minecraftforge.eventbus.api.SubscribeEvent;
import net.minecraftforge.fml.common.Mod;

import java.util.Locale;

@Mod.EventBusSubscriber(modid = Creeperella.MOD_ID)
public final class CommonEvents {
    @SubscribeEvent
    public static void onEntityInteract(PlayerInteractEvent.EntityInteract event) {
        if (!(event.getTarget() instanceof Creeper creeper)) {
            return;
        }

        Player player = event.getEntity();
        ItemStack held = player.getItemInHand(event.getHand());

        if (creeper instanceof CreeperellaEntity companion && CreeperellaConfig.ENABLE_COMPANIONS.get()) {
            if (handleCompanionInteraction(event, player, held, companion)) {
                return;
            }
        }

        if (CreeperellaConfig.ENABLE_LEGACY_NAME_TAGS.get() && held.is(Items.NAME_TAG) && held.hasCustomHoverName()) {
            String tag = held.getHoverName().getString().trim().toLowerCase(Locale.ROOT);
            CreeperellaKind legacyKind = switch (tag) {
                case "bunny" -> CreeperellaKind.BUNNY;
                case "bee" -> CreeperellaKind.BEE;
                default -> null;
            };
            if (legacyKind != null && !(creeper instanceof CreeperellaEntity current && current.kind() == legacyKind)) {
                if (!event.getLevel().isClientSide && event.getLevel() instanceof ServerLevel serverLevel) {
                    CreeperellaEntity transformed = replace(serverLevel, creeper, legacyKind);
                    if (transformed != null) {
                        transformed.setCustomName(held.getHoverName());
                        transformed.setCustomNameVisible(creeper.isCustomNameVisible());
                        transformed.grantMakeoverGrace(player);
                        consumeOne(player, held, false);
                        celebrate(serverLevel, transformed, legacyKind);
                        awardTransformationAdvancement(serverLevel, player, legacyKind);
                    }
                }
                finishInteraction(event);
                return;
            }
        }

        if (!CreeperellaConfig.ENABLE_TRANSFORMATIONS.get()) {
            return;
        }

        CreeperellaKind destination = destinationFor(creeper, held);
        if (destination == null) {
            return;
        }

        if (!event.getLevel().isClientSide && event.getLevel() instanceof ServerLevel serverLevel) {
            CreeperellaEntity transformed = replace(serverLevel, creeper, destination);
            if (transformed != null) {
                transformed.grantMakeoverGrace(player);
                boolean honey = held.is(Items.HONEY_BOTTLE);
                consumeOne(player, held, honey);
                celebrate(serverLevel, transformed, destination);
                awardTransformationAdvancement(serverLevel, player, destination);
            }
        }

        finishInteraction(event);
    }

    @SubscribeEvent
    public static void onExplosionDetonate(ExplosionEvent.Detonate event) {
        if (!CreeperellaConfig.ENABLE_COMPANIONS.get()
                || !CreeperellaConfig.PROTECT_OWNER_AND_PETS_FROM_FOLLOWER_EXPLOSIONS.get()) {
            return;
        }

        Entity sourceEntity = event.getExplosion().getExploder();
        if (!(sourceEntity instanceof CreeperellaEntity companion) || !companion.isCompanionTamed()) {
            return;
        }

        // Remove protected allies before vanilla computes explosion damage/knockback. The LivingAttackEvent
        // guard below remains as defense in depth for modded explosion implementations.
        event.getAffectedEntities().removeIf(entity ->
                entity instanceof LivingEntity living && companion.isOwnedAlly(living));
    }

    @SubscribeEvent
    public static void onLivingAttack(LivingAttackEvent event) {
        if (!CreeperellaConfig.ENABLE_COMPANIONS.get()
                || !CreeperellaConfig.PROTECT_OWNER_AND_PETS_FROM_FOLLOWER_EXPLOSIONS.get()) {
            return;
        }

        Entity sourceEntity = event.getSource().getEntity();
        if (!(sourceEntity instanceof CreeperellaEntity companion) || !companion.isCompanionTamed()) {
            return;
        }

        LivingEntity victim = event.getEntity();
        if (companion.isOwnedAlly(victim)) {
            event.setCanceled(true);
        }
    }

    private static boolean handleCompanionInteraction(PlayerInteractEvent.EntityInteract event,
                                                       Player player,
                                                       ItemStack held,
                                                       CreeperellaEntity companion) {
        if (companion.isReforming()) {
            return false;
        }

        Item matchingTreat = tamingTreatFor(companion.kind());
        if (held.is(matchingTreat)) {
            if (!event.getLevel().isClientSide && event.getLevel() instanceof ServerLevel serverLevel) {
                feedCompanionTreat(serverLevel, player, held, companion);
            }
            finishInteraction(event);
            return true;
        }

        if (held.isEmpty() && companion.isOwnedBy(player)) {
            if (!event.getLevel().isClientSide) {
                boolean changed = companion.toggleSitting(player);
                if (changed) {
                    String state = companion.isOrderedToSit() ? "Stay" : "Follow";
                    player.displayClientMessage(Component.literal(companion.getDisplayName().getString() + ": " + state)
                            .withStyle(companion.isOrderedToSit() ? ChatFormatting.YELLOW : ChatFormatting.GREEN), true);
                }
            }
            finishInteraction(event);
            return true;
        }

        return false;
    }

    private static void feedCompanionTreat(ServerLevel level,
                                           Player player,
                                           ItemStack held,
                                           CreeperellaEntity companion) {
        if (companion.isCompanionTamed()) {
            if (!companion.isOwnedBy(player)) {
                player.displayClientMessage(Component.literal("This Creeperella is already bonded to someone else.")
                        .withStyle(ChatFormatting.YELLOW), true);
                return;
            }
            if (companion.getHealth() >= companion.getMaxHealth()) {
                player.displayClientMessage(Component.literal("She's already at full health.")
                        .withStyle(ChatFormatting.GREEN), true);
                return;
            }

            consumeTamingTreat(player, held);
            companion.heal(CreeperellaConfig.TREAT_HEAL_AMOUNT.get().floatValue());
            level.playSound(null, companion.blockPosition(), SoundEvents.GENERIC_EAT,
                    companion.getSoundSource(), 0.8F, 1.15F);
            level.sendParticles(ParticleTypes.HEART, companion.getX(), companion.getY() + 1.0D, companion.getZ(),
                    5, 0.3D, 0.4D, 0.3D, 0.02D);
            return;
        }

        consumeTamingTreat(player, held);
        int progress = companion.addBondProgress();
        int required = CreeperellaConfig.TAME_TREATS_REQUIRED.get();
        if (progress >= required) {
            companion.tameTo(player);
            level.playSound(null, companion.blockPosition(), SoundEvents.PLAYER_LEVELUP,
                    companion.getSoundSource(), 0.8F, 1.45F);
            level.sendParticles(ParticleTypes.HEART, companion.getX(), companion.getY() + 1.0D, companion.getZ(),
                    12, 0.4D, 0.55D, 0.4D, 0.03D);
            player.displayClientMessage(Component.literal(companion.getDisplayName().getString() + " is now your demolition buddy!")
                    .withStyle(ChatFormatting.LIGHT_PURPLE), true);
            award(level, player instanceof ServerPlayer sp ? sp : null, "best_friends_with_booms");
        } else {
            level.playSound(null, companion.blockPosition(), SoundEvents.GENERIC_EAT,
                    companion.getSoundSource(), 0.8F, 0.95F + progress * 0.08F);
            level.sendParticles(ParticleTypes.HEART, companion.getX(), companion.getY() + 1.0D, companion.getZ(),
                    3, 0.25D, 0.35D, 0.25D, 0.01D);
            player.displayClientMessage(Component.literal("Bonding: " + progress + "/" + required)
                    .withStyle(ChatFormatting.AQUA), true);
        }
    }

    private static Item tamingTreatFor(CreeperellaKind kind) {
        return switch (kind) {
            case FEMALE -> ModItems.ROSY_FUSE_CAKE.get();
            case BUNNY -> ModItems.BUNNY_BOOM_BITE.get();
            case BEE -> ModItems.HONEY_POP.get();
            case CHERRY -> ModItems.CHERRY_BOMB_BONBON.get();
            case BLOSSOM -> ModItems.BLOSSOM_BURST_COOKIE.get();
        };
    }

    private static CreeperellaKind destinationFor(Creeper creeper, ItemStack held) {
        if (creeper.getType() == EntityType.CREEPER && held.is(Items.PINK_TULIP)) {
            return CreeperellaKind.FEMALE;
        }
        if (!(creeper instanceof CreeperellaEntity current)) {
            return null;
        }
        if (held.is(Items.PINK_TULIP) && current.kind() != CreeperellaKind.FEMALE) {
            return CreeperellaKind.FEMALE;
        }
        if (held.is(Items.RABBIT_FOOT) && current.kind() != CreeperellaKind.BUNNY) {
            return CreeperellaKind.BUNNY;
        }
        if (held.is(Items.HONEY_BOTTLE) && current.kind() != CreeperellaKind.BEE) {
            return CreeperellaKind.BEE;
        }
        if (held.is(Items.CHERRY_SAPLING) && current.kind() != CreeperellaKind.CHERRY) {
            return CreeperellaKind.CHERRY;
        }
        if (held.is(Items.PINK_PETALS) && current.kind() == CreeperellaKind.CHERRY) {
            return CreeperellaKind.BLOSSOM;
        }
        return null;
    }

    private static CreeperellaEntity replace(ServerLevel level, Creeper source, CreeperellaKind destination) {
        CreeperellaEntity target = ModEntities.typeFor(destination).create(level);
        if (target == null) {
            return null;
        }

        CompoundTag data = new CompoundTag();
        source.saveWithoutId(data);
        data.remove("UUID");
        target.load(data);
        target.moveTo(source.getX(), source.getY(), source.getZ(), source.getYRot(), source.getXRot());
        target.setDeltaMovement(source.getDeltaMovement());
        target.setSwellDir(source.getSwellDir());

        if (source.isVehicle()) {
            source.ejectPassengers();
        }
        source.discard();
        level.addFreshEntity(target);
        return target;
    }

    private static void consumeOne(Player player, ItemStack held, boolean returnBottle) {
        if (!CreeperellaConfig.CONSUME_TRANSFORMATION_ITEMS.get() || player.getAbilities().instabuild) {
            return;
        }
        held.shrink(1);
        if (returnBottle) {
            ItemStack bottle = new ItemStack(Items.GLASS_BOTTLE);
            if (!player.getInventory().add(bottle) && player instanceof ServerPlayer serverPlayer) {
                serverPlayer.drop(bottle, false);
            }
        }
    }

    private static void consumeTamingTreat(Player player, ItemStack held) {
        if (!CreeperellaConfig.CONSUME_TAMING_TREATS.get() || player.getAbilities().instabuild) {
            return;
        }
        held.shrink(1);
    }

    private static void celebrate(ServerLevel level, CreeperellaEntity entity, CreeperellaKind kind) {
        level.playSound(null, entity.blockPosition(), SoundEvents.AMETHYST_BLOCK_CHIME,
                entity.getSoundSource(), 0.9F, 1.15F + level.random.nextFloat() * 0.2F);
        level.sendParticles(ParticleTypes.HEART, entity.getX(), entity.getY() + 1.0D, entity.getZ(),
                7, 0.35D, 0.45D, 0.35D, 0.02D);
        if (kind == CreeperellaKind.CHERRY || kind == CreeperellaKind.BLOSSOM) {
            int petals = kind == CreeperellaKind.BLOSSOM ? 24 : 14;
            level.sendParticles(ParticleTypes.CHERRY_LEAVES, entity.getX(), entity.getY() + 1.1D, entity.getZ(),
                    petals, 0.45D, 0.6D, 0.45D, 0.02D);
        }
    }

    private static void awardTransformationAdvancement(ServerLevel level, Player player, CreeperellaKind kind) {
        if (!(player instanceof ServerPlayer serverPlayer)) {
            return;
        }
        award(level, serverPlayer, "root");
        String advancement = switch (kind) {
            case FEMALE -> "makeover";
            case BUNNY -> "bunny_business";
            case BEE -> "bee_yourself";
            case CHERRY -> "cherry_on_top";
            case BLOSSOM -> "bloom_and_boom";
        };
        award(level, serverPlayer, advancement);
    }

    private static void award(ServerLevel level, ServerPlayer player, String path) {
        if (player == null) {
            return;
        }
        var advancement = level.getServer().getAdvancements()
                .getAdvancement(new ResourceLocation(Creeperella.MOD_ID, path));
        if (advancement != null) {
            player.getAdvancements().award(advancement, "trigger");
        }
    }

    private static void finishInteraction(PlayerInteractEvent.EntityInteract event) {
        event.setCancellationResult(InteractionResult.sidedSuccess(event.getLevel().isClientSide));
        event.setCanceled(true);
    }

    private CommonEvents() {}
}
