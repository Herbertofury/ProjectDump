package com.github.tatercertified.potatoptimize.mixin.fastmath.rounding;

import com.github.tatercertified.potatoptimize.utils.math.FasterMathUtil;
import net.minecraft.entity.player.PlayerEntity;
import org.spongepowered.asm.mixin.Mixin;
import org.spongepowered.asm.mixin.injection.At;
import org.spongepowered.asm.mixin.injection.Redirect;

/**
 * In Minecraft 1.20.1 increaseTravelMotionStats is declared by PlayerEntity, not ServerPlayerEntity.
 * Target the declaring class so the optional fast-rounding rule actually applies when enabled.
 */
@Mixin(PlayerEntity.class)
public class FastRoundingServerPlayerMixin {
    @Redirect(
            method = "increaseTravelMotionStats(DDD)V",
            require = 0,
            at = @At(value = "INVOKE", target = "Ljava/lang/Math;round(D)J"))
    private long fasterRound(double value) {
        return FasterMathUtil.round(value);
    }
}
