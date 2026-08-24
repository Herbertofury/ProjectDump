package dev.herbertofury.creeperella.event;

import dev.herbertofury.creeperella.Creeperella;
import dev.herbertofury.creeperella.config.CreeperellaConfig;
import dev.herbertofury.creeperella.registry.ModEntities;
import net.minecraft.core.BlockPos;
import net.minecraft.util.RandomSource;
import net.minecraft.world.entity.EntityType;
import net.minecraft.world.entity.MobSpawnType;
import net.minecraft.world.entity.SpawnPlacements;
import net.minecraft.world.entity.monster.Creeper;
import net.minecraft.world.entity.monster.Monster;
import net.minecraft.world.level.ServerLevelAccessor;
import net.minecraft.world.level.biome.Biomes;
import net.minecraft.world.level.levelgen.Heightmap;
import net.minecraftforge.common.ForgeConfigSpec;
import net.minecraftforge.event.entity.EntityAttributeCreationEvent;
import net.minecraftforge.event.entity.SpawnPlacementRegisterEvent;
import net.minecraftforge.eventbus.api.SubscribeEvent;
import net.minecraftforge.fml.common.Mod;

@Mod.EventBusSubscriber(modid = Creeperella.MOD_ID, bus = Mod.EventBusSubscriber.Bus.MOD)
public final class ModBusEvents {
    @SubscribeEvent
    public static void registerAttributes(EntityAttributeCreationEvent event) {
        event.put(ModEntities.FEMALE_CREEPER.get(), Creeper.createAttributes().build());
        event.put(ModEntities.BUNNY_CREEPER.get(), Creeper.createAttributes().build());
        event.put(ModEntities.BEE_CREEPER.get(), Creeper.createAttributes().build());
        event.put(ModEntities.CHERRY_CREEPER.get(), Creeper.createAttributes().build());
        event.put(ModEntities.BLOSSOM_CREEPER.get(), Creeper.createAttributes().build());
    }

    @SubscribeEvent
    public static void registerSpawnPlacements(SpawnPlacementRegisterEvent event) {
        event.register(ModEntities.FEMALE_CREEPER.get(), SpawnPlacements.Type.ON_GROUND,
                Heightmap.Types.MOTION_BLOCKING_NO_LEAVES,
                (type, level, reason, pos, random) -> canSpawn(CreeperellaConfig.SPAWN_FEMALE, type, level, reason, pos, random),
                SpawnPlacementRegisterEvent.Operation.REPLACE);
        event.register(ModEntities.BUNNY_CREEPER.get(), SpawnPlacements.Type.ON_GROUND,
                Heightmap.Types.MOTION_BLOCKING_NO_LEAVES,
                (type, level, reason, pos, random) -> canSpawn(CreeperellaConfig.SPAWN_BUNNY, type, level, reason, pos, random),
                SpawnPlacementRegisterEvent.Operation.REPLACE);
        event.register(ModEntities.BEE_CREEPER.get(), SpawnPlacements.Type.ON_GROUND,
                Heightmap.Types.MOTION_BLOCKING_NO_LEAVES,
                (type, level, reason, pos, random) -> canSpawn(CreeperellaConfig.SPAWN_BEE, type, level, reason, pos, random),
                SpawnPlacementRegisterEvent.Operation.REPLACE);
        event.register(ModEntities.CHERRY_CREEPER.get(), SpawnPlacements.Type.ON_GROUND,
                Heightmap.Types.MOTION_BLOCKING_NO_LEAVES,
                (type, level, reason, pos, random) -> canSpawn(CreeperellaConfig.SPAWN_CHERRY, type, level, reason, pos, random),
                SpawnPlacementRegisterEvent.Operation.REPLACE);
        event.register(ModEntities.BLOSSOM_CREEPER.get(), SpawnPlacements.Type.ON_GROUND,
                Heightmap.Types.MOTION_BLOCKING_NO_LEAVES,
                (type, level, reason, pos, random) -> canSpawn(CreeperellaConfig.SPAWN_BLOSSOM, type, level, reason, pos, random),
                SpawnPlacementRegisterEvent.Operation.REPLACE);
    }

    private static boolean canSpawn(ForgeConfigSpec.BooleanValue enabled,
                                    EntityType<? extends Monster> type,
                                    ServerLevelAccessor level,
                                    MobSpawnType reason,
                                    BlockPos pos,
                                    RandomSource random) {
        if (!enabled.get()) {
            return false;
        }
        var biome = level.getBiome(pos);
        if (biome.is(Biomes.MUSHROOM_FIELDS) || biome.is(Biomes.DEEP_DARK)) {
            return false;
        }
        return Monster.checkMonsterSpawnRules(type, level, reason, pos, random);
    }

    private ModBusEvents() {}
}
