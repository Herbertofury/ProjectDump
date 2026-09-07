package com.github.tatercertified.potatoptimize.mixin.threading.entity_ticking;

import net.minecraft.entity.Entity;
import net.minecraft.world.EntityList;
import org.spongepowered.asm.mixin.Mixin;
import org.spongepowered.asm.mixin.Overwrite;
import org.spongepowered.asm.mixin.Unique;

import java.util.concurrent.ConcurrentHashMap;
import java.util.function.Consumer;

@Mixin(EntityList.class)
public class EntityListMixin {
    @Unique
    private final ConcurrentHashMap<Integer, Entity> concurrentEntities = new ConcurrentHashMap<>();

    /**
     * @author QPCrummer
     * @reason Make Concurrent
     */
    @Overwrite
    public void add(Entity entity) {
        this.concurrentEntities.put(entity.getId(), entity);
    }

    /**
     * @author QPCrummer
     * @reason Make Concurrent
     */
    @Overwrite
    public void remove(Entity entity) {
        concurrentEntities.remove(entity.getId());
    }

    /**
     * @author QPCrummer
     * @reason Make Concurrent
     */
    @Overwrite
    public boolean has(Entity entity) {
        return concurrentEntities.containsKey(entity.getId());
    }

    /**
     * @author QPCrummer, OpenAI
     * @reason Keep concurrent entity storage without off-thread world access.
     *
     * Forge 1.20.1 entity ticks may synchronously request chunk/world work that must
     * progress on the server thread. Waiting on worker-thread entity ticks from that
     * same server thread can therefore deadlock. Iterate the concurrent container on
     * the caller thread instead: structural mutation safety is retained while entity
     * gameplay remains on Minecraft's authoritative tick thread.
     */
    @Overwrite
    public void forEach(Consumer<Entity> action) {
        this.concurrentEntities.values().forEach(action);
    }
}
