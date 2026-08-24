package dev.herbertofury.creeperella.client;

import dev.herbertofury.creeperella.Creeperella;
import dev.herbertofury.creeperella.entity.CreeperellaEntity;
import dev.herbertofury.creeperella.entity.CreeperellaKind;
import net.minecraft.client.model.EntityModel;
import net.minecraft.client.renderer.entity.RenderLayerParent;
import net.minecraft.client.renderer.entity.layers.EnergySwirlLayer;
import net.minecraft.resources.ResourceLocation;

public final class CreeperellaPowerLayer extends EnergySwirlLayer<CreeperellaEntity, CreeperellaModel<CreeperellaEntity>> {
    private static final ResourceLocation PIE_POWER = new ResourceLocation(Creeperella.MOD_ID, "textures/entity/pie_charge.png");
    private static final ResourceLocation VANILLA_POWER = new ResourceLocation("textures/entity/creeper/creeper_armor.png");

    private final CreeperellaModel<CreeperellaEntity> model;
    private final CreeperellaKind kind;

    public CreeperellaPowerLayer(RenderLayerParent<CreeperellaEntity, CreeperellaModel<CreeperellaEntity>> parent,
                                 CreeperellaModel<CreeperellaEntity> model, CreeperellaKind kind) {
        super(parent);
        this.model = model;
        this.kind = kind;
    }

    @Override
    protected float xOffset(float age) {
        return age * 0.01F;
    }

    @Override
    protected ResourceLocation getTextureLocation() {
        return switch (this.kind) {
            case FEMALE, BUNNY, BEE -> PIE_POWER;
            case CHERRY, BLOSSOM -> VANILLA_POWER;
        };
    }

    @Override
    protected EntityModel<CreeperellaEntity> model() {
        return this.model;
    }
}
