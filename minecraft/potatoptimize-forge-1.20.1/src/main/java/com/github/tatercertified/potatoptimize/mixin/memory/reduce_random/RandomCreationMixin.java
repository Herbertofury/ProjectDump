package com.github.tatercertified.potatoptimize.mixin.memory.reduce_random;

import com.github.tatercertified.potatoptimize.utils.random.ThreadLocalRandomImpl;
import net.minecraft.util.math.random.Random;
import org.spongepowered.asm.mixin.Mixin;
import org.spongepowered.asm.mixin.Overwrite;

/**
 * Replaces the no-arg Random.create() factory with the thread-local implementation.
 *
 * Forge 1.20.1 ships Mixin 0.8.5, which requires a mixin targeting an interface to
 * itself be an interface. The old redirect-based interface mixin is rejected by the
 * Forge annotation processor, while converting it to a class compiles but is rejected
 * at production runtime as a target-type mismatch. A public static overwrite preserves
 * the original optimization without either failure mode.
 */
@Mixin(Random.class)
public interface RandomCreationMixin {

    /**
     * @author QPCrummer / Forge 1.20.1 port
     * @reason Reuse the existing thread-local random for the optional reduce-random profile.
     */
    @Overwrite
    static Random create() {
        return ThreadLocalRandomImpl.INSTANCE;
    }
}
