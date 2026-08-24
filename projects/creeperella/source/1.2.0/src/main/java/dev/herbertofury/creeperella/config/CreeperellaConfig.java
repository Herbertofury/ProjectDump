package dev.herbertofury.creeperella.config;

import net.minecraftforge.common.ForgeConfigSpec;

public final class CreeperellaConfig {
    public static final ForgeConfigSpec SPEC;

    public static final ForgeConfigSpec.BooleanValue ENABLE_TRANSFORMATIONS;
    public static final ForgeConfigSpec.BooleanValue CONSUME_TRANSFORMATION_ITEMS;
    public static final ForgeConfigSpec.BooleanValue ENABLE_LEGACY_NAME_TAGS;
    public static final ForgeConfigSpec.IntValue MAKEOVER_GRACE_TICKS;

    public static final ForgeConfigSpec.BooleanValue ENABLE_COMPANIONS;
    public static final ForgeConfigSpec.BooleanValue CONSUME_TAMING_TREATS;
    public static final ForgeConfigSpec.IntValue TAME_TREATS_REQUIRED;
    public static final ForgeConfigSpec.DoubleValue TREAT_HEAL_AMOUNT;
    public static final ForgeConfigSpec.DoubleValue COMPANION_MOVE_SPEED;
    public static final ForgeConfigSpec.DoubleValue FOLLOW_START_DISTANCE;
    public static final ForgeConfigSpec.DoubleValue FOLLOW_STOP_DISTANCE;
    public static final ForgeConfigSpec.DoubleValue FOLLOW_TELEPORT_DISTANCE;
    public static final ForgeConfigSpec.DoubleValue COMMAND_RANGE;
    public static final ForgeConfigSpec.IntValue COMMAND_TIMEOUT_TICKS;
    public static final ForgeConfigSpec.DoubleValue DETONATION_TRIGGER_DISTANCE;
    public static final ForgeConfigSpec.IntValue DETONATION_COOLDOWN_TICKS;
    public static final ForgeConfigSpec.IntValue CHARGED_DETONATION_COOLDOWN_TICKS;
    public static final ForgeConfigSpec.IntValue REFORM_TICKS;
    public static final ForgeConfigSpec.DoubleValue FOLLOWER_EXPLOSION_POWER;
    public static final ForgeConfigSpec.DoubleValue CHARGED_FOLLOWER_EXPLOSION_POWER;
    public static final ForgeConfigSpec.BooleanValue FOLLOWER_EXPLOSIONS_BREAK_BLOCKS;
    public static final ForgeConfigSpec.BooleanValue PROTECT_OWNER_AND_PETS_FROM_FOLLOWER_EXPLOSIONS;

    public static final ForgeConfigSpec.BooleanValue AMBIENT_PARTICLES;
    public static final ForgeConfigSpec.BooleanValue SPAWN_FEMALE;
    public static final ForgeConfigSpec.BooleanValue SPAWN_BUNNY;
    public static final ForgeConfigSpec.BooleanValue SPAWN_BEE;
    public static final ForgeConfigSpec.BooleanValue SPAWN_CHERRY;
    public static final ForgeConfigSpec.BooleanValue SPAWN_BLOSSOM;

    static {
        ForgeConfigSpec.Builder builder = new ForgeConfigSpec.Builder();

        builder.push("transformations");
        ENABLE_TRANSFORMATIONS = builder
                .comment("Allow vanilla-item interactions to transform Creepers and Creeperella variants.")
                .define("enableTransformations", true);
        CONSUME_TRANSFORMATION_ITEMS = builder
                .comment("Consume the transformation item in survival mode.")
                .define("consumeTransformationItems", true);
        ENABLE_LEGACY_NAME_TAGS = builder
                .comment("Preserve Pie's legacy bunny/bee name-tag behavior by converting to the matching standalone entity.")
                .define("enableLegacyNameTags", true);
        MAKEOVER_GRACE_TICKS = builder
                .comment(
                        "How long a freshly transformed wild Creeperella refuses to target the player who transformed her.",
                        "20 ticks = 1 second. Tamed companions are permanently friendly to their owner."
                )
                .defineInRange("makeoverGraceTicks", 120, 0, 1200);
        builder.pop();

        builder.push("companions");
        ENABLE_COMPANIONS = builder
                .comment("Enable taming, follow/stay behavior, Fuse Whistle commands, reusable explosions, and reformation.")
                .define("enableCompanions", true);
        CONSUME_TAMING_TREATS = builder
                .comment("Consume variant-themed taming treats in survival mode.")
                .define("consumeTamingTreats", true);
        TAME_TREATS_REQUIRED = builder
                .comment("Deterministic number of matching treats required to tame a wild Creeperella. No random taming failures.")
                .defineInRange("tameTreatsRequired", 3, 1, 16);
        TREAT_HEAL_AMOUNT = builder
                .comment("Health restored when the owner feeds a tamed Creeperella her matching treat.")
                .defineInRange("treatHealAmount", 6.0D, 0.0D, 40.0D);
        COMPANION_MOVE_SPEED = builder
                .comment("Navigation speed used while following the owner or running toward a whistle-designated target.")
                .defineInRange("moveSpeed", 1.10D, 0.5D, 2.0D);
        FOLLOW_START_DISTANCE = builder
                .defineInRange("followStartDistance", 7.0D, 2.0D, 32.0D);
        FOLLOW_STOP_DISTANCE = builder
                .defineInRange("followStopDistance", 3.0D, 1.0D, 16.0D);
        FOLLOW_TELEPORT_DISTANCE = builder
                .comment("If the owner gets farther than this, the companion safely recalls beside them.")
                .defineInRange("followTeleportDistance", 24.0D, 8.0D, 96.0D);
        COMMAND_RANGE = builder
                .comment("Maximum command/follower target range used by the Fuse Whistle.")
                .defineInRange("commandRange", 48.0D, 8.0D, 128.0D);
        COMMAND_TIMEOUT_TICKS = builder
                .comment("How long an ordered boom-run may chase a target before giving up. 20 ticks = 1 second.")
                .defineInRange("commandTimeoutTicks", 600, 40, 2400);
        DETONATION_TRIGGER_DISTANCE = builder
                .comment("Distance from a commanded target at which the companion performs her reusable explosion.")
                .defineInRange("detonationTriggerDistance", 2.35D, 1.0D, 6.0D);
        DETONATION_COOLDOWN_TICKS = builder
                .comment("Normal follower explosion cooldown. Default 600 ticks = 30 seconds.")
                .defineInRange("detonationCooldownTicks", 600, 20, 7200);
        CHARGED_DETONATION_COOLDOWN_TICKS = builder
                .comment("Charged follower explosion cooldown. Default 900 ticks = 45 seconds.")
                .defineInRange("chargedDetonationCooldownTicks", 900, 20, 12000);
        REFORM_TICKS = builder
                .comment("How long the companion stays phased out before visibly reforming beside her owner. Default 60 ticks = 3 seconds.")
                .defineInRange("reformTicks", 60, 1, 600);
        FOLLOWER_EXPLOSION_POWER = builder
                .comment("Reusable follower blast power. Slightly below a vanilla Creeper by default for balance.")
                .defineInRange("explosionPower", 2.75D, 0.5D, 12.0D);
        CHARGED_FOLLOWER_EXPLOSION_POWER = builder
                .comment("Reusable charged-follower blast power; paired with the longer charged cooldown.")
                .defineInRange("chargedExplosionPower", 4.25D, 0.5D, 16.0D);
        FOLLOWER_EXPLOSIONS_BREAK_BLOCKS = builder
                .comment("Allow commanded follower explosions to damage blocks. Off by default so companions are combat tools, not base griefers.")
                .define("explosionsBreakBlocks", false);
        PROTECT_OWNER_AND_PETS_FROM_FOLLOWER_EXPLOSIONS = builder
                .comment("Protect the owner, allied players, the owner's tameable pets, and sibling Creeperellas from commanded explosion damage.")
                .define("protectOwnerAndPets", true);
        builder.pop();

        builder.push("visuals");
        AMBIENT_PARTICLES = builder
                .comment("Enable subtle client-side personality particles around Creeperella variants.")
                .define("ambientParticles", true);
        builder.pop();

        builder.push("naturalSpawning");
        SPAWN_FEMALE = builder.define("femaleCreeper", true);
        SPAWN_BUNNY = builder.define("bunnyCreeper", true);
        SPAWN_BEE = builder.define("beeCreeper", true);
        SPAWN_CHERRY = builder.define("cherryCreeper", true);
        SPAWN_BLOSSOM = builder.define("blossomCreeper", true);
        builder.pop();

        SPEC = builder.build();
    }

    private CreeperellaConfig() {}
}
