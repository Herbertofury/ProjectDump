package dev.herbertofury.creeperella.registry;

import dev.herbertofury.creeperella.Creeperella;
import dev.herbertofury.creeperella.item.FuseWhistleItem;
import net.minecraft.world.food.FoodProperties;
import net.minecraft.world.item.Item;
import net.minecraft.world.item.Rarity;
import net.minecraftforge.common.ForgeSpawnEggItem;
import net.minecraftforge.eventbus.api.IEventBus;
import net.minecraftforge.registries.DeferredRegister;
import net.minecraftforge.registries.ForgeRegistries;
import net.minecraftforge.registries.RegistryObject;

public final class ModItems {
    public static final DeferredRegister<Item> ITEMS = DeferredRegister.create(ForgeRegistries.ITEMS, Creeperella.MOD_ID);

    public static final RegistryObject<Item> FEMALE_CREEPER_SPAWN_EGG = ITEMS.register("female_creeper_spawn_egg",
            () -> new ForgeSpawnEggItem(ModEntities.FEMALE_CREEPER, 0x5A9E51, 0xEAA9CC, new Item.Properties()));
    public static final RegistryObject<Item> BUNNY_CREEPER_SPAWN_EGG = ITEMS.register("bunny_creeper_spawn_egg",
            () -> new ForgeSpawnEggItem(ModEntities.BUNNY_CREEPER, 0x7CAA63, 0xF5D9E5, new Item.Properties()));
    public static final RegistryObject<Item> BEE_CREEPER_SPAWN_EGG = ITEMS.register("bee_creeper_spawn_egg",
            () -> new ForgeSpawnEggItem(ModEntities.BEE_CREEPER, 0x5F9B58, 0xF6C645, new Item.Properties()));
    public static final RegistryObject<Item> CHERRY_CREEPER_SPAWN_EGG = ITEMS.register("cherry_creeper_spawn_egg",
            () -> new ForgeSpawnEggItem(ModEntities.CHERRY_CREEPER, 0xE7A0AF, 0x6C7D4C, new Item.Properties()));
    public static final RegistryObject<Item> BLOSSOM_CREEPER_SPAWN_EGG = ITEMS.register("blossom_creeper_spawn_egg",
            () -> new ForgeSpawnEggItem(ModEntities.BLOSSOM_CREEPER, 0xF7CAD7, 0xA55372, new Item.Properties()));

    private static final FoodProperties ROSY_FUSE_CAKE_FOOD = new FoodProperties.Builder()
            .nutrition(6).saturationMod(0.6F).build();
    private static final FoodProperties BUNNY_BOOM_BITE_FOOD = new FoodProperties.Builder()
            .nutrition(4).saturationMod(0.5F).build();
    private static final FoodProperties HONEY_POP_FOOD = new FoodProperties.Builder()
            .nutrition(3).saturationMod(0.6F).build();
    private static final FoodProperties CHERRY_BOMB_BONBON_FOOD = new FoodProperties.Builder()
            .nutrition(4).saturationMod(0.5F).build();
    private static final FoodProperties BLOSSOM_BURST_COOKIE_FOOD = new FoodProperties.Builder()
            .nutrition(3).saturationMod(0.4F).build();

    public static final RegistryObject<Item> ROSY_FUSE_CAKE = ITEMS.register("rosy_fuse_cake",
            () -> new Item(new Item.Properties().food(ROSY_FUSE_CAKE_FOOD)));
    public static final RegistryObject<Item> BUNNY_BOOM_BITE = ITEMS.register("bunny_boom_bite",
            () -> new Item(new Item.Properties().food(BUNNY_BOOM_BITE_FOOD)));
    public static final RegistryObject<Item> HONEY_POP = ITEMS.register("honey_pop",
            () -> new Item(new Item.Properties().food(HONEY_POP_FOOD)));
    public static final RegistryObject<Item> CHERRY_BOMB_BONBON = ITEMS.register("cherry_bomb_bonbon",
            () -> new Item(new Item.Properties().food(CHERRY_BOMB_BONBON_FOOD)));
    public static final RegistryObject<Item> BLOSSOM_BURST_COOKIE = ITEMS.register("blossom_burst_cookie",
            () -> new Item(new Item.Properties().food(BLOSSOM_BURST_COOKIE_FOOD)));

    public static final RegistryObject<Item> FUSE_WHISTLE = ITEMS.register("fuse_whistle",
            () -> new FuseWhistleItem(new Item.Properties().stacksTo(1).rarity(Rarity.UNCOMMON)));

    public static void register(IEventBus bus) {
        ITEMS.register(bus);
    }

    private ModItems() {}
}
