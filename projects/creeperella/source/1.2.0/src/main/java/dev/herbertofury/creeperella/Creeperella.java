package dev.herbertofury.creeperella;

import dev.herbertofury.creeperella.config.CreeperellaConfig;
import dev.herbertofury.creeperella.registry.ModEntities;
import dev.herbertofury.creeperella.registry.ModItems;
import net.minecraft.world.item.CreativeModeTabs;
import net.minecraftforge.event.BuildCreativeModeTabContentsEvent;
import net.minecraftforge.eventbus.api.IEventBus;
import net.minecraftforge.fml.ModLoadingContext;
import net.minecraftforge.fml.common.Mod;
import net.minecraftforge.fml.config.ModConfig;
import net.minecraftforge.fml.javafmlmod.FMLJavaModLoadingContext;

@Mod(Creeperella.MOD_ID)
public final class Creeperella {
    public static final String MOD_ID = "creeperella";

    public Creeperella() {
        IEventBus modBus = FMLJavaModLoadingContext.get().getModEventBus();
        ModEntities.register(modBus);
        ModItems.register(modBus);
        ModLoadingContext.get().registerConfig(ModConfig.Type.COMMON, CreeperellaConfig.SPEC, "creeperella-common.toml");
        modBus.addListener(this::populateCreativeTabs);
    }

    private void populateCreativeTabs(BuildCreativeModeTabContentsEvent event) {
        if (event.getTabKey() == CreativeModeTabs.SPAWN_EGGS) {
            event.accept(ModItems.FEMALE_CREEPER_SPAWN_EGG.get());
            event.accept(ModItems.BUNNY_CREEPER_SPAWN_EGG.get());
            event.accept(ModItems.BEE_CREEPER_SPAWN_EGG.get());
            event.accept(ModItems.CHERRY_CREEPER_SPAWN_EGG.get());
            event.accept(ModItems.BLOSSOM_CREEPER_SPAWN_EGG.get());
        }
        if (event.getTabKey() == CreativeModeTabs.FOOD_AND_DRINKS) {
            event.accept(ModItems.ROSY_FUSE_CAKE.get());
            event.accept(ModItems.BUNNY_BOOM_BITE.get());
            event.accept(ModItems.HONEY_POP.get());
            event.accept(ModItems.CHERRY_BOMB_BONBON.get());
            event.accept(ModItems.BLOSSOM_BURST_COOKIE.get());
        }
        if (event.getTabKey() == CreativeModeTabs.TOOLS_AND_UTILITIES) {
            event.accept(ModItems.FUSE_WHISTLE.get());
        }
    }
}
