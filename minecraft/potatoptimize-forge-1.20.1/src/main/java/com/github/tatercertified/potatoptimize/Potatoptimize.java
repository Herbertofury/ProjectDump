package com.github.tatercertified.potatoptimize;

import com.github.tatercertified.potatoptimize.config.PotatoptimizeConfig;
import net.minecraft.server.MinecraftServer;
import net.minecraftforge.common.MinecraftForge;
import net.minecraftforge.event.server.ServerStartingEvent;
import net.minecraftforge.fml.common.Mod;

import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;

@Mod(Potatoptimize.MOD_ID)
public class Potatoptimize {
    public static final String MOD_ID = "potatoptimize";
    public static PotatoptimizeConfig CONFIG;
    public static MinecraftServer almightyServerInstance;
    public static final ExecutorService clientTickExecutor = Executors.newSingleThreadExecutor(r -> {
        Thread t = new Thread(r, "Potatoptimize Client Tick Worker");
        t.setDaemon(true);
        return t;
    });
    public static boolean isUnsafeRandomEnabled;

    public Potatoptimize() {
        MinecraftForge.EVENT_BUS.addListener(this::onServerStarting);
    }

    private void onServerStarting(ServerStartingEvent event) {
        almightyServerInstance = event.getServer();
    }
}
