#!/usr/bin/env bash
set -euo pipefail

SERVER=${SERVER:?}
COMMON_MODS=${COMMON_MODS:?}
POTATO_JAR=${POTATO_JAR:?}
EVIDENCE=${EVIDENCE:?}
TEMPLATE=${TEMPLATE:?}
mkdir -p "$EVIDENCE/runs"

DIMS=(minecraft:overworld minecraft:the_nether midnight:midnight)
BENCH_PID=""
BENCH_FD=""
BENCH_CONSOLE=""
BENCH_FIFO=""

fatal_re='MixinApplyError|MixinTransformerError|InjectionError|Critical injection failure|InvalidMixinException|NoClassDefFoundError|ClassNotFoundException|ConcurrentModificationException|ServerHangWatchdog|A single server tick took|Exception in server tick loop|FAILED TO BIND TO PORT|Watchdog'

write_server_properties() {
  local port=$1
  cat > "$SERVER/server.properties" <<EOF
server-port=$port
online-mode=false
spawn-protection=0
view-distance=6
simulation-distance=6
max-tick-time=60000
level-seed=867530920260907
motd=Potatoptimize Native Benchmark
allow-flight=true
enable-command-block=false
EOF
}

prepare_mods() {
  local potato=$1
  rm -rf "$SERVER/mods" "$SERVER/config"
  mkdir -p "$SERVER/mods" "$SERVER/config"
  cp "$COMMON_MODS"/*.jar "$SERVER/mods/"
  if [[ "$potato" == yes ]]; then cp "$POTATO_JAR" "$SERVER/mods/"; fi
}

start_server() {
  local label=$1 port=$2
  BENCH_CONSOLE="$EVIDENCE/runs/$label.console.log"
  BENCH_FIFO="$SERVER/server-input-$label"
  rm -rf "$SERVER/logs" "$SERVER/crash-reports" "$SERVER/debug"
  rm -f "$BENCH_FIFO"
  mkfifo "$BENCH_FIFO"
  write_server_properties "$port"
  cd "$SERVER"
  exec {BENCH_FD}<>"$BENCH_FIFO"
  setsid ./run.sh nogui <"$BENCH_FIFO" >"$BENCH_CONSOLE" 2>&1 &
  BENCH_PID=$!
  echo "$BENCH_PID" > "$EVIDENCE/runs/$label.pid"
}

send_cmd() { printf '%s\n' "$*" >&"$BENCH_FD"; }

wait_pattern() {
  local pattern=$1 timeout=${2:-180}
  for _ in $(seq 1 "$timeout"); do
    if grep -Fq "$pattern" "$BENCH_CONSOLE" 2>/dev/null; then return 0; fi
    if ! kill -0 "$BENCH_PID" 2>/dev/null; then tail -n 240 "$BENCH_CONSOLE" || true; return 1; fi
    sleep 1
  done
  echo "timeout waiting for: $pattern" >&2
  tail -n 240 "$BENCH_CONSOLE" || true
  return 1
}

wait_new_saved() {
  local before=$1 timeout=${2:-180}
  for _ in $(seq 1 "$timeout"); do
    local now
    now=$(grep -Ec 'Saved the game|Saved the world|Saved chunks' "$BENCH_CONSOLE" 2>/dev/null || true)
    if (( now > before )); then return 0; fi
    if ! kill -0 "$BENCH_PID" 2>/dev/null; then return 1; fi
    sleep 1
  done
  return 1
}

stop_server() {
  if kill -0 "$BENCH_PID" 2>/dev/null; then send_cmd stop || true; fi
  exec {BENCH_FD}>&- || true
  for _ in $(seq 1 45); do
    if ! kill -0 "$BENCH_PID" 2>/dev/null; then break; fi
    sleep 1
  done
  if kill -0 "$BENCH_PID" 2>/dev/null; then
    kill -TERM -- "-$BENCH_PID" 2>/dev/null || true
    sleep 3
    kill -KILL -- "-$BENCH_PID" 2>/dev/null || true
  fi
  wait "$BENCH_PID" || true
  rm -f "$BENCH_FIFO"
}

validate_console() {
  local label=$1
  if grep -Eiq "$fatal_re" "$BENCH_CONSOLE"; then
    echo "fatal runtime signature in $label" >&2
    grep -Ein "$fatal_re" "$BENCH_CONSOLE" | tail -n 80 >&2 || true
    return 1
  fi
  grep -Fq 'Done (' "$BENCH_CONSOLE"
  grep -Fq 'midnight' "$BENCH_CONSOLE"
  grep -Fq 'c2me' "$BENCH_CONSOLE"
  grep -Fq 'dimthread' "$BENCH_CONSOLE"
}

build_template() {
  rm -rf "$SERVER/world" "$TEMPLATE"
  prepare_mods no
  start_server template 25570
  wait_pattern 'Done (' 240
  send_cmd 'gamerule doMobSpawning false'
  send_cmd 'gamerule mobGriefing false'
  send_cmd 'difficulty hard'
  for dim in "${DIMS[@]}"; do
    send_cmd "execute in $dim run forceload add -2 -2 2 2"
    send_cmd "execute in $dim run fill -24 63 -24 23 63 23 minecraft:stone"
    send_cmd "execute in $dim run fill -24 64 -24 23 64 23 minecraft:oak_sign[rotation=0]"
  done
  send_cmd 'execute in midnight:midnight run say POTATOBENCH_MIDNIGHT_DIMENSION_OK'
  wait_pattern 'POTATOBENCH_MIDNIGHT_DIMENSION_OK' 60

  for dim in "${DIMS[@]}"; do
    for i in $(seq 0 95); do
      x=$(( -18 + (i % 12) * 3 ))
      z=$(( -12 + (i / 12) * 3 ))
      send_cmd "execute in $dim run summon minecraft:villager $x 65 $z {PersistenceRequired:1b}"
      send_cmd "execute in $dim run summon minecraft:item $x 72 $z {Item:{id:\"minecraft:bread\",Count:1b},NoGravity:1b,PickupDelay:32767,Age:-32768,Invulnerable:1b}"
    done
  done
  before=$(grep -Ec 'Saved the game|Saved the world|Saved chunks' "$BENCH_CONSOLE" 2>/dev/null || true)
  send_cmd 'save-all flush'
  wait_new_saved "$before" 240
  sleep 5
  stop_server
  validate_console template
  cp -a "$SERVER/world" "$TEMPLATE"
  echo 'template complete' > "$EVIDENCE/template-status.txt"
}

run_case() {
  local case=$1 rep=$2 potato=$3 port=$4
  local label="$case-r$rep"
  rm -rf "$SERVER/world"
  cp -a "$TEMPLATE" "$SERVER/world"
  prepare_mods "$potato"
  start_server "$label" "$port"
  wait_pattern 'Done (' 240
  if [[ "$potato" == yes ]]; then
    wait_pattern 'Potatoptimize' 60
    if ! grep -Eq 'C2ME detected; disabling overlapping Potatoptimize rules:.*mixin.world.saving' "$BENCH_CONSOLE"; then
      echo 'Potatoptimize did not activate C2ME overlap guard' >&2
      tail -n 160 "$BENCH_CONSOLE" >&2
      stop_server
      return 1
    fi
  fi

  # Warm up JIT, AI and rolling Forge tick metrics before collecting samples.
  sleep 25
  send_cmd "say POTATOBENCH_STEADY_START $case $rep"
  for sample in $(seq 1 12); do
    send_cmd "say POTATOBENCH_SAMPLE $case $rep $sample"
    send_cmd 'forge tps'
    if [[ "$sample" == 4 ]]; then
      java_pid=$(pgrep -P "$BENCH_PID" -f 'java' | head -n 1 || true)
      if [[ -z "$java_pid" ]]; then java_pid=$(pgrep -g "$BENCH_PID" -f 'java' | head -n 1 || true); fi
      if [[ -n "$java_pid" ]]; then
        "$JAVA_HOME/bin/jcmd" "$java_pid" Thread.print > "$EVIDENCE/runs/$label.thread-dump.txt" 2>&1 || true
      fi
    fi
    sleep 5
  done
  send_cmd "say POTATOBENCH_STEADY_END $case $rep"
  sleep 2

  # Fresh-region generation + palette mutation challenge. Template cloning means every rep sees identical ungenerated chunks.
  send_cmd "say POTATOBENCH_GEN_START $case $rep"
  local start_ns end_ns before
  start_ns=$(date +%s%N)
  for dim in "${DIMS[@]}"; do
    send_cmd "execute in $dim run forceload add 3200 3200 3327 3327"
    send_cmd "execute in $dim run fill 3200 100 3200 3327 100 3327 minecraft:stone"
  done
  before=$(grep -Ec 'Saved the game|Saved the world|Saved chunks' "$BENCH_CONSOLE" 2>/dev/null || true)
  send_cmd 'save-all flush'
  wait_new_saved "$before" 300
  end_ns=$(date +%s%N)
  awk -v a="$start_ns" -v b="$end_ns" 'BEGIN { printf "%.6f\n", (b-a)/1000000000.0 }' > "$EVIDENCE/runs/$label.gen_seconds"
  send_cmd "say POTATOBENCH_GEN_END $case $rep"
  for dim in "${DIMS[@]}"; do send_cmd "execute in $dim run forceload remove 3200 3200 3327 3327"; done
  send_cmd 'forge tps'
  sleep 3
  stop_server
  validate_console "$label"
  grep -q 'dimthread_server_' "$EVIDENCE/runs/$label.thread-dump.txt" || {
    echo "DimThread workers were not observed in $label thread dump" >&2
    return 1
  }
  if [[ "$potato" == yes ]]; then
    grep -q '^mixin.block_entity.sign_ticking=true\|^mixin.block_entity.sign_ticking = true' "$SERVER/config/potatoptimize.properties" || true
  fi
}

build_template
# ABBAAB ordering balances first-run/JIT/cache drift across the same hosted runner.
run_case base 1 no 25571
run_case potato 1 yes 25572
run_case potato 2 yes 25573
run_case base 2 no 25574
run_case base 3 no 25575
run_case potato 3 yes 25576
