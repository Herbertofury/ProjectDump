package com.github.tatercertified.potatoptimize.mixin.entity.navigation;

import net.minecraft.entity.LivingEntity;
import net.minecraft.entity.ai.pathing.EntityNavigation;
import net.minecraft.entity.mob.MobEntity;
import org.spongepowered.asm.mixin.Final;
import org.spongepowered.asm.mixin.Mixin;
import org.spongepowered.asm.mixin.Shadow;
import org.spongepowered.asm.mixin.injection.At;
import org.spongepowered.asm.mixin.injection.Inject;
import org.spongepowered.asm.mixin.injection.callback.CallbackInfo;

/**
 * Backported from modern Potatoptimize semantics: mobs riding living entities keep vanilla navigation ticking.
 * Navigation is skipped only while riding a non-living vehicle, where vanilla movement is not completed.
 */
@Mixin(EntityNavigation.class)
public class CancelNavigationMixin {
    @Shadow @Final protected MobEntity entity;

    @Inject(method = "tick", at = @At("HEAD"), cancellable = true)
    private void potatoptimize$cancelUnusedVehicleNavigation(CallbackInfo ci) {
        if (entity.hasVehicle() && !(entity.getVehicle() instanceof LivingEntity)) {
            ci.cancel();
        }
    }
}
