package com.github.tatercertified.potatoptimize.mixin.logic.data_bits;

import net.minecraft.util.collection.PackedIntegerArray;
import org.spongepowered.asm.mixin.Final;
import org.spongepowered.asm.mixin.Mixin;
import org.spongepowered.asm.mixin.Mutable;
import org.spongepowered.asm.mixin.Overwrite;
import org.spongepowered.asm.mixin.Shadow;
import org.spongepowered.asm.mixin.Unique;
import org.spongepowered.asm.mixin.injection.At;
import org.spongepowered.asm.mixin.injection.Inject;
import org.spongepowered.asm.mixin.injection.callback.CallbackInfo;

/**
 * Credit to PaperMC patch #0087.
 *
 * Forge 1.20.1 ships Mixin 0.8.5, which only permits constructor callbacks at
 * a safe post-initialization point. Cache the unsigned constants at RETURN
 * instead of injecting at intermediate FIELD writes in the constructor.
 */
@Mixin(PackedIntegerArray.class)
public class OptimizedPackedIntMixin {
    @Shadow @Final private int indexScale;
    @Shadow @Final private int indexOffset;
    @Shadow @Final private int indexShift;

    @Unique
    @Final @Mutable
    private long potatoptimize$indexScaleUnsigned;

    @Unique
    @Final @Mutable
    private long potatoptimize$indexOffsetUnsigned;

    @Inject(method = "<init>(II[J)V", at = @At("RETURN"))
    private void potatoptimize$cacheUnsignedIndexConstants(int elementBits, int size, long[] data, CallbackInfo ci) {
        this.potatoptimize$indexScaleUnsigned = Integer.toUnsignedLong(this.indexScale);
        this.potatoptimize$indexOffsetUnsigned = Integer.toUnsignedLong(this.indexOffset);
    }

    /**
     * @author QPCrummer
     * @reason Simplify the storage-index arithmetic while preserving vanilla output.
     */
    @Overwrite
    private int getStorageIndex(int index) {
        return (int) ((long) index * this.potatoptimize$indexScaleUnsigned
                + this.potatoptimize$indexOffsetUnsigned >> 32 >> this.indexShift);
    }
}
