package dev.herbertofury.creeperella.client;

import com.mojang.blaze3d.vertex.PoseStack;
import com.mojang.blaze3d.vertex.VertexConsumer;
import dev.herbertofury.creeperella.entity.CreeperellaEntity;
import dev.herbertofury.creeperella.entity.CreeperellaKind;
import net.minecraft.client.model.CreeperModel;
import net.minecraft.client.model.geom.ModelPart;
import net.minecraft.util.Mth;

public class CreeperellaModel<T extends CreeperellaEntity> extends CreeperModel<T> {
    private final CreeperellaKind kind;
    private final float tintR;
    private final float tintG;
    private final float tintB;

    public CreeperellaModel(ModelPart root, CreeperellaKind kind, float tintR, float tintG, float tintB) {
        super(root);
        this.kind = kind;
        this.tintR = tintR;
        this.tintG = tintG;
        this.tintB = tintB;
    }

    @Override
    public void setupAnim(T entity, float limbSwing, float limbSwingAmount, float ageInTicks, float netHeadYaw, float headPitch) {
        super.setupAnim(entity, limbSwing, limbSwingAmount, ageInTicks, netHeadYaw, headPitch);

        ModelPart head2 = child(this.root(), "head", "head2");
        if (head2 != null) {
            ModelPart leftHair = child(head2, "hair_left");
            ModelPart rightHair = child(head2, "hair_right");
            float hairSway = Mth.sin(ageInTicks * 0.11F) * 0.055F + Mth.sin(limbSwing * 0.45F) * limbSwingAmount * 0.08F;
            animateZ(leftHair, hairSway);
            animateZ(rightHair, hairSway);

            if (this.kind == CreeperellaKind.BUNNY) {
                float earBounce = Mth.sin(ageInTicks * 0.13F) * 0.045F + limbSwingAmount * 0.05F;
                animateZ(child(head2, "left_ear"), earBounce);
                animateZ(child(head2, "right_ear"), -earBounce);
            }
        }

        ModelPart cemBody = child(this.root(), "body", "body");
        if (cemBody != null && this.kind == CreeperellaKind.BUNNY) {
            ModelPart tail = child(cemBody, "tail");
            if (tail != null) {
                tail.resetPose();
                tail.xRot += Mth.sin(ageInTicks * 0.22F) * 0.08F;
            }
        }
        if (cemBody != null && this.kind == CreeperellaKind.BEE) {
            float flap = 0.22F + Math.abs(Mth.sin(ageInTicks * 1.15F)) * 0.38F;
            ModelPart leftWing = child(cemBody, "left_wings");
            ModelPart rightWing = child(cemBody, "right_wings");
            if (leftWing != null) {
                leftWing.resetPose();
                leftWing.yRot += flap;
            }
            if (rightWing != null) {
                rightWing.resetPose();
                rightWing.yRot -= flap;
            }
        }
    }

    private static void animateZ(ModelPart part, float offset) {
        if (part == null) return;
        part.resetPose();
        part.zRot += offset;
    }

    private static ModelPart child(ModelPart parent, String... path) {
        ModelPart current = parent;
        try {
            for (String name : path) {
                current = current.getChild(name);
            }
            return current;
        } catch (RuntimeException ignored) {
            return null;
        }
    }

    @Override
    public void renderToBuffer(PoseStack poseStack, VertexConsumer vertexConsumer, int packedLight, int packedOverlay,
                               float red, float green, float blue, float alpha) {
        super.renderToBuffer(poseStack, vertexConsumer, packedLight, packedOverlay,
                red * this.tintR, green * this.tintG, blue * this.tintB, alpha);
    }
}
