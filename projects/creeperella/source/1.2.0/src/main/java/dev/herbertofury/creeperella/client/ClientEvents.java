package dev.herbertofury.creeperella.client;

import dev.herbertofury.creeperella.Creeperella;
import dev.herbertofury.creeperella.entity.CreeperellaKind;
import dev.herbertofury.creeperella.registry.ModEntities;
import net.minecraft.client.model.geom.ModelLayerLocation;
import net.minecraft.resources.ResourceLocation;
import net.minecraftforge.api.distmarker.Dist;
import net.minecraftforge.client.event.EntityRenderersEvent;
import net.minecraftforge.eventbus.api.SubscribeEvent;
import net.minecraftforge.fml.common.Mod;

@Mod.EventBusSubscriber(modid = Creeperella.MOD_ID, bus = Mod.EventBusSubscriber.Bus.MOD, value = Dist.CLIENT)
public final class ClientEvents {
    public static final ModelLayerLocation FEMALE = layer("female_creeper");
    public static final ModelLayerLocation BUNNY = layer("bunny_creeper");
    public static final ModelLayerLocation BEE = layer("bee_creeper");
    public static final ModelLayerLocation CHERRY = layer("cherry_creeper");
    public static final ModelLayerLocation FEMALE_CHARGE = layer("female_creeper_charge");
    public static final ModelLayerLocation BUNNY_CHARGE = layer("bunny_creeper_charge");
    public static final ModelLayerLocation BEE_CHARGE = layer("bee_creeper_charge");
    public static final ModelLayerLocation CHERRY_CHARGE = layer("cherry_creeper_charge");

    @SubscribeEvent
    public static void registerLayers(EntityRenderersEvent.RegisterLayerDefinitions event) {
        event.registerLayerDefinition(FEMALE, CreeperellaModelLayers::createFemaleLayer);
        event.registerLayerDefinition(BUNNY, CreeperellaModelLayers::createBunnyLayer);
        event.registerLayerDefinition(BEE, CreeperellaModelLayers::createBeeLayer);
        event.registerLayerDefinition(CHERRY, CreeperellaModelLayers::createCherryLayer);
        event.registerLayerDefinition(FEMALE_CHARGE, CreeperellaModelLayers::createFemaleChargeLayer);
        event.registerLayerDefinition(BUNNY_CHARGE, CreeperellaModelLayers::createBunnyChargeLayer);
        event.registerLayerDefinition(BEE_CHARGE, CreeperellaModelLayers::createBeeChargeLayer);
        event.registerLayerDefinition(CHERRY_CHARGE, CreeperellaModelLayers::createCherryChargeLayer);
    }

    @SubscribeEvent
    public static void registerRenderers(EntityRenderersEvent.RegisterRenderers event) {
        event.registerEntityRenderer(ModEntities.FEMALE_CREEPER.get(), context -> new CreeperellaRenderer(context, CreeperellaKind.FEMALE));
        event.registerEntityRenderer(ModEntities.BUNNY_CREEPER.get(), context -> new CreeperellaRenderer(context, CreeperellaKind.BUNNY));
        event.registerEntityRenderer(ModEntities.BEE_CREEPER.get(), context -> new CreeperellaRenderer(context, CreeperellaKind.BEE));
        event.registerEntityRenderer(ModEntities.CHERRY_CREEPER.get(), context -> new CreeperellaRenderer(context, CreeperellaKind.CHERRY));
        event.registerEntityRenderer(ModEntities.BLOSSOM_CREEPER.get(), context -> new CreeperellaRenderer(context, CreeperellaKind.BLOSSOM));
    }

    public static ModelLayerLocation baseLayer(CreeperellaKind kind) {
        return switch (kind) {
            case FEMALE -> FEMALE;
            case BUNNY -> BUNNY;
            case BEE -> BEE;
            case CHERRY, BLOSSOM -> CHERRY;
        };
    }

    public static ModelLayerLocation chargeLayer(CreeperellaKind kind) {
        return switch (kind) {
            case FEMALE -> FEMALE_CHARGE;
            case BUNNY -> BUNNY_CHARGE;
            case BEE -> BEE_CHARGE;
            case CHERRY, BLOSSOM -> CHERRY_CHARGE;
        };
    }

    private static ModelLayerLocation layer(String path) {
        return new ModelLayerLocation(new ResourceLocation(Creeperella.MOD_ID, path), "main");
    }

    private ClientEvents() {}
}
