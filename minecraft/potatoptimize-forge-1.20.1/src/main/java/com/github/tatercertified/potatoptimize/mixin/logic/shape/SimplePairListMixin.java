package com.github.tatercertified.potatoptimize.mixin.logic.shape;

import it.unimi.dsi.fastutil.doubles.DoubleList;
import net.minecraft.util.shape.SimplePairList;
import org.spongepowered.asm.mixin.Final;
import org.spongepowered.asm.mixin.Mixin;
import org.spongepowered.asm.mixin.Mutable;
import org.spongepowered.asm.mixin.Shadow;
import org.spongepowered.asm.mixin.injection.At;
import org.spongepowered.asm.mixin.injection.Inject;
import org.spongepowered.asm.mixin.injection.callback.CallbackInfo;

/**
 * Credit: PaperMC patch #1003
 *
 * Forge 1.20.1 ships Mixin 0.8.5, which rejects the old cancellable FIELD injection
 * inside this constructor. Apply the same special-case final representation at RETURN
 * instead. This preserves the optimized retained arrays and exact PairList semantics,
 * while allowing vanilla construction to complete before the fields are compacted.
 */
@Mixin(SimplePairList.class)
public class SimplePairListMixin {
    @Mutable @Shadow @Final private double[] valueIndices;
    @Mutable @Shadow @Final private int size;
    @Mutable @Shadow @Final private int[] minValues;
    @Mutable @Shadow @Final private int[] maxValues;

    private static final int[] INFINITE_B_1 = new int[]{1, 1};
    private static final int[] INFINITE_B_0 = new int[]{0, 0};
    private static final int[] INFINITE_C = new int[]{0, 1};

    @Inject(method = "<init>", at = @At("RETURN"))
    private void compactInfiniteAxisPair(DoubleList first, DoubleList second, boolean includeFirstOnly, boolean includeSecondOnly, CallbackInfo ci) {
        int firstSize = first.size();
        if (firstSize != 2 && firstSize != 4) {
            return;
        }

        double head = first.getDouble(0);
        double tail = first.getDouble(firstSize - 1);
        if (head == Double.NEGATIVE_INFINITY && tail == Double.POSITIVE_INFINITY && !includeFirstOnly && !includeSecondOnly) {
            this.valueIndices = second.toDoubleArray();
            this.size = second.size();
            this.minValues = firstSize == 2 ? INFINITE_B_0 : INFINITE_B_1;
            this.maxValues = INFINITE_C;
        }
    }
}
