#!/usr/bin/env python3
import csv
import re
import statistics
import sys
from pathlib import Path

root = Path(sys.argv[1])
run_dir = root / "runs"
rows = []
metric_re = re.compile(r"Mean tick time:\s*([0-9]+(?:\.[0-9]+)?)\s*ms", re.I)
sample_re = re.compile(r"POTATOBENCH_SAMPLE\s+(base|potato)\s+(\d+)\s+(\d+)")

for console in sorted(run_dir.glob("*.console.log")):
    m = re.match(r"(base|potato)-r(\d+)\.console\.log$", console.name)
    if not m:
        continue
    case, rep = m.group(1), int(m.group(2))
    lines = console.read_text(errors="replace").splitlines()
    samples = []
    current = None
    bucket = []
    in_steady = False
    for line in lines:
        if f"POTATOBENCH_STEADY_START {case} {rep}" in line:
            in_steady = True
            continue
        if f"POTATOBENCH_STEADY_END {case} {rep}" in line:
            if current is not None and bucket:
                overall = [x for x in bucket if "overall" in x[0].lower()]
                chosen = overall[-1] if overall else bucket[-1]
                samples.append(chosen[1])
            current = None
            bucket = []
            in_steady = False
            continue
        if not in_steady:
            continue
        sm = sample_re.search(line)
        if sm:
            if current is not None and bucket:
                overall = [x for x in bucket if "overall" in x[0].lower()]
                chosen = overall[-1] if overall else bucket[-1]
                samples.append(chosen[1])
            current = int(sm.group(3))
            bucket = []
            continue
        mm = metric_re.search(line)
        if mm and current is not None:
            bucket.append((line, float(mm.group(1))))
    if current is not None and bucket:
        overall = [x for x in bucket if "overall" in x[0].lower()]
        chosen = overall[-1] if overall else bucket[-1]
        samples.append(chosen[1])
    if len(samples) < 8:
        raise SystemExit(f"{console}: only {len(samples)} usable forge tps samples")
    gen_file = run_dir / f"{case}-r{rep}.gen_seconds"
    gen = float(gen_file.read_text().strip())
    rows.append({
        "case": case,
        "rep": rep,
        "samples": len(samples),
        "median_mspt": statistics.median(samples),
        "mean_mspt": statistics.fmean(samples),
        "min_mspt": min(samples),
        "max_mspt": max(samples),
        "gen_seconds": gen,
    })

for case in ("base", "potato"):
    if len([r for r in rows if r["case"] == case]) != 3:
        raise SystemExit(f"expected 3 {case} repetitions")

out_csv = root / "benchmark-results.csv"
with out_csv.open("w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
    w.writeheader(); w.writerows(rows)

base_mspt = statistics.median([r["median_mspt"] for r in rows if r["case"] == "base"])
pot_mspt = statistics.median([r["median_mspt"] for r in rows if r["case"] == "potato"])
base_gen = statistics.median([r["gen_seconds"] for r in rows if r["case"] == "base"])
pot_gen = statistics.median([r["gen_seconds"] for r in rows if r["case"] == "potato"])
mspt_gain = (base_mspt - pot_mspt) / base_mspt * 100.0
gen_gain = (base_gen - pot_gen) / base_gen * 100.0

if mspt_gain >= 3.0 and gen_gain >= -5.0:
    verdict = "REAL_GAIN"
elif mspt_gain <= -3.0 or gen_gain <= -8.0:
    verdict = "REGRESSION"
else:
    verdict = "WEAK_OR_NOISY_GAIN"

summary = root / "BENCHMARK-SUMMARY.md"
with summary.open("w") as f:
    f.write("# Potatoptimize + Midnight + DimThread + C2ME native benchmark\n\n")
    f.write(f"**Verdict:** `{verdict}`\n\n")
    f.write(f"- Baseline median steady-state MSPT: **{base_mspt:.3f} ms**\n")
    f.write(f"- Potatoptimize median steady-state MSPT: **{pot_mspt:.3f} ms**\n")
    f.write(f"- Steady-state improvement: **{mspt_gain:+.2f}%**\n")
    f.write(f"- Baseline median forced-generation workload: **{base_gen:.3f} s**\n")
    f.write(f"- Potatoptimize median forced-generation workload: **{pot_gen:.3f} s**\n")
    f.write(f"- Generation/workload improvement: **{gen_gain:+.2f}%**\n\n")
    f.write("## Repetitions\n\n")
    f.write("| Case | Rep | TPS samples | Median MSPT | Mean MSPT | Range | Generation s |\n")
    f.write("|---|---:|---:|---:|---:|---:|---:|\n")
    for r in rows:
        f.write(f"| {r['case']} | {r['rep']} | {r['samples']} | {r['median_mspt']:.3f} | {r['mean_mspt']:.3f} | {r['min_mspt']:.3f}-{r['max_mspt']:.3f} | {r['gen_seconds']:.3f} |\n")
    f.write("\nDecision rule: >=3% steady-state median MSPT improvement with no >5% generation regression counts as a real gain.\n")

print(summary.read_text())
if verdict == "REGRESSION":
    sys.exit(2)
