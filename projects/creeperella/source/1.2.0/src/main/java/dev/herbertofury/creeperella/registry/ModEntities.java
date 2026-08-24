package dev.herbertofury.creeperella.registry;

import dev.herbertofury.creeperella.Creeperella;
import dev.herbertofury.creeperella.entity.CreeperellaEntity;
import dev.herbertofury.creeperella.entity.CreeperellaKind;
import net.minecraft.world.entity.EntityType;
import net.minecraft.world.entity.MobCategory;
import net.minecraftforge.eventbus.api.IEventBus;
import net.minecraftforge.registries.DeferredRegister;
import net.minecraftforge.registries.ForgeRegistries;
import net.minecraftforge.registries.RegistryObject;

public final class ModEntities {
    public static final DeferredRegister<EntityType<?>> ENTITIES =
            DeferredRegister.create(ForgeRegistries.ENTITY_TYPES, Creeperella.MOD_ID);

    public static final RegistryObject<EntityType<CreeperellaEntity>> FEMALE_CREEPER = register("female_creeper");
    public static final RegistryObject<EntityType<CreeperellaEntity>> BUNNY_CREEPER = register("bunny_creeper");
    public static final RegistryObject<EntityType<CreeperellaEntity>> BEE_CREEPER = register("bee_creeper");
    public static final RegistryObject<EntityType<CreeperellaEntity>> CHERRY_CREEPER = register("cherry_creeper");
    public static final RegistryObject<EntityType<CreeperellaEntity>> BLOSSOM_CREEPER = register("blossom_creeper");

    private static RegistryObject<EntityType<CreeperellaEntity>> register(String id) {
        return ENTITIES.register(id, () -> EntityType.Builder
                .of(CreeperellaEntity::new, MobCategory.MONSTER)
                .sized(0.6F, 1.7F)
                .clientTrackingRange(8)
                .build(Creeperella.MOD_ID + ":" + id));
    }

    public static CreeperellaKind kindOf(EntityType<?> type) {
        if (type == BUNNY_CREEPER.get()) return CreeperellaKind.BUNNY;
        if (type == BEE_CREEPER.get()) return CreeperellaKind.BEE;
        if (type == CHERRY_CREEPER.get()) return CreeperellaKind.CHERRY;
        if (type == BLOSSOM_CREEPER.get()) return CreeperellaKind.BLOSSOM;
        return CreeperellaKind.FEMALE;
    }

    public static EntityType<CreeperellaEntity> typeFor(CreeperellaKind kind) {
        return switch (kind) {
            case BUNNY -> BUNNY_CREEPER.get();
            case BEE -> BEE_CREEPER.get();
            case CHERRY -> CHERRY_CREEPER.get();
            case BLOSSOM -> BLOSSOM_CREEPER.get();
            case FEMALE -> FEMALE_CREEPER.get();
        };
    }

    public static void register(IEventBus bus) {
        ENTITIES.register(bus);
    }

    private ModEntities() {}
}
