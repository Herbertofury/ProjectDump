package dev.herbertofury.creeperella.client;

import com.mojang.blaze3d.vertex.PoseStack;
import dev.herbertofury.creeperella.Creeperella;
import dev.herbertofury.creeperella.entity.CreeperellaEntity;
import dev.herbertofury.creeperella.entity.CreeperellaKind;
import net.minecraft.client.renderer.entity.EntityRendererProvider;
import net.minecraft.client.renderer.entity.MobRenderer;
import net.minecraft.resources.ResourceLocation;
import net.minecraft.util.Mth;

public final class CreeperellaRenderer extends MobRenderer<CreeperellaEntity, CreeperellaModel<CreeperellaEntity>> {
    private static final ResourceLocation FEMALE = texture("female_creeper.png");
    private static final ResourceLocation BUNNY = texture("bunny_creeper.png");
    private static final ResourceLocation BEE = texture("bee_creeper.png");
    private static final ResourceLocation CHERRY = texture("cherry_creeper.png");
    private static final ResourceLocation BLOSSOM = texture("blossom_creeper.png");

    private final CreeperellaKind kind;

    public CreeperellaRenderer(EntityRendererProvider.Context context, CreeperellaKind kind) {
        super(context, createBaseModel(context, kind), 0.5F);
        this.kind = kind;
        this.addLayer(new CreeperellaPowerLayer(this, createChargeModel(context, kind), kind));
    }

    private static CreeperellaModel<CreeperellaEntity> createBaseModel(EntityRendererProvider.Context context, CreeperellaKind kind) {
        float[] tint = tint(kind);
        return new CreeperellaModel<>(context.bakeLayer(ClientEvents.baseLayer(kind)), kind, tint[0], tint[1], tint[2]);
    }

    private static CreeperellaModel<CreeperellaEntity> createChargeModel(EntityRendererProvider.Context context, CreeperellaKind kind) {
        float[] tint = tint(kind);
        return new CreeperellaModel<>(context.bakeLayer(ClientEvents.chargeLayer(kind)), kind, tint[0], tint[1], tint[2]);
    }

    private static float[] tint(CreeperellaKind kind) {
        return new float[]{1.0F, 1.0F, 1.0F};
    }

    @Override
    protected void scale(CreeperellaEntity creeper, PoseStack poseStack, float partialTick) {
        float swelling = creeper.getSwelling(partialTick);
        float pulse = 1.0F + Mth.sin(swelling * 100.0F) * swelling * 0.01F;
        swelling = Mth.clamp(swelling, 0.0F, 1.0F);
        swelling *= swelling;
        swelling *= swelling;
        float horizontal = (1.0F + swelling * 0.4F) * pulse;
        float vertical = (1.0F + swelling * 0.1F) / pulse;
        poseStack.scale(horizontal, vertical, horizontal);
    }

    @Override
    protected float getWhiteOverlayProgress(CreeperellaEntity creeper, float partialTick) {
        float swelling = creeper.getSwelling(partialTick);
        return (int) (swelling * 10.0F) % 2 == 0 ? 0.0F : Mth.clamp(swelling, 0.5F, 1.0F);
    }

    @Override
    public ResourceLocation getTextureLocation(CreeperellaEntity entity) {
        return switch (this.kind) {
            case BUNNY -> BUNNY;
            case BEE -> BEE;
            case CHERRY -> CHERRY;
            case BLOSSOM -> BLOSSOM;
            case FEMALE -> FEMALE;
        };
    }

    private static ResourceLocation texture(String name) {
        return new ResourceLocation(Creeperella.MOD_ID, "textures/entity/" + name);
    }
}
