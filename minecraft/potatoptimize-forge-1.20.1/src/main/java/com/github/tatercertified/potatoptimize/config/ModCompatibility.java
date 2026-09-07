package com.github.tatercertified.potatoptimize.config;

import net.minecraftforge.fml.loading.FMLLoader;
import org.apache.logging.log4j.LogManager;
import org.apache.logging.log4j.Logger;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public final class ModCompatibility {
    private static final Logger LOGGER = LogManager.getLogger("PotatoptimizeConfig");
    private static final List<String> DISABLED_MIXINS = new ArrayList<>();

    private ModCompatibility() {}

    public static boolean testFor(String mixin) {
        return DISABLED_MIXINS.contains(mixin);
    }

    public static void prepareMixins() {
        DISABLED_MIXINS.clear();
        addModCompatibility("krypton", "Krypton", new String[]{"mixin.logic.var_int"});
        addModCompatibility("kryptonreforged", "Krypton Reforged", new String[]{"mixin.logic.var_int"});
        addModCompatibility("modernfix", "ModernFix", new String[]{"mixin.logic.worker_thread", "mixin.startup.dfu"});
        addModCompatibility("servercore", "ServerCore", new String[]{"mixin.item.map_chunk_loading", "mixin.unstream.pathfinding"});
        addModCompatibility("chronos-carpet-addons", "Chronos Carpet Addons", new String[]{"mixin.entity.collisions"});
        addModCompatibility("faster-random", "FasterRandom", new String[]{"mixin.random.entity", "mixin.random.math", "mixin.random.world", "mixin.memory.reduce_random"});
        addModCompatibility("c2me", "C2ME", new String[]{"mixin.world.saving"});
        addModCompatibility("lithium", "Lithium", new String[]{"mixin.world.explosion"});
        addModCompatibility("canary", "Canary", new String[]{"mixin.world.explosion"});
        addModCompatibility("radium", "Radium", new String[]{"mixin.world.explosion"});
        addModCompatibility("valkyrienskies", "Valkyrien Skies", new String[]{"mixin.unstream.pathfinding"});
        addModCompatibility("enhancedvisuals", "EnhancedVisuals", new String[]{"mixin.world.explosion"});
    }

    private static void addModCompatibility(String modId, String visualName, String[] mixins) {
        if (FMLLoader.getLoadingModList() != null && FMLLoader.getLoadingModList().getModFileById(modId) != null) {
            LOGGER.info("{} detected; disabling overlapping Potatoptimize rules: {}", visualName, Arrays.toString(mixins));
            DISABLED_MIXINS.addAll(Arrays.asList(mixins));
        }
    }
}
