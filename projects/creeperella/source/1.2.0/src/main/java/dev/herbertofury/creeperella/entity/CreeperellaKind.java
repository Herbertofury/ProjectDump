package dev.herbertofury.creeperella.entity;

public enum CreeperellaKind {
    FEMALE("female_creeper"),
    BUNNY("bunny_creeper"),
    BEE("bee_creeper"),
    CHERRY("cherry_creeper"),
    BLOSSOM("blossom_creeper");

    private final String id;

    CreeperellaKind(String id) {
        this.id = id;
    }

    public String id() {
        return this.id;
    }
}
