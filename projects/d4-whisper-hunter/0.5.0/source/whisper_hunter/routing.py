from __future__ import annotations

from dataclasses import dataclass
import math
from .config import Config
from .tracker import TrackedWhisper


@dataclass(slots=True)
class RoutePlan:
    items: list[TrackedWhisper]
    favor: int
    distance: float
    estimated_minutes: float
    score: float


def _activity_minutes(item: TrackedWhisper, cfg: Config) -> float:
    return {1: cfg.favor1_minutes, 3: cfg.favor3_minutes, 5: cfg.favor5_minutes}.get(item.favor, 5.0)


def plan_route(
    items: list[TrackedWhisper],
    start: tuple[float, float] | None,
    current_favors: int,
    cfg: Config,
    beam_width: int = 320,
) -> RoutePlan:
    needed = max(0, cfg.route_target_favors - max(0, current_favors))
    if needed == 0 or not items:
        return RoutePlan([], 0, 0.0, 0.0, 0.0)
    if start is None:
        start = (
            sum(x.map_x for x in items) / len(items),
            sum(x.map_y for x in items) / len(items),
        )

    # Limit to strongest/closest candidates while retaining exhaustive likely routes.
    ranked = sorted(
        items,
        key=lambda x: (
            -x.favor,
            math.hypot(x.map_x-start[0], x.map_y-start[1]) / max(1, x.favor),
            -x.confidence,
        ),
    )[:28]

    # Beam search state: (score, dist, minutes, favor, position, tuple(indices)).
    beam = [(0.0, 0.0, 0.0, 0, start, tuple())]
    finished = []
    for _depth in range(min(8, len(ranked))):
        nxt = []
        for _score, dist, minutes, favor, pos, used in beam:
            used_set = set(used)
            for i, item in enumerate(ranked):
                if i in used_set:
                    continue
                leg = math.hypot(item.map_x-pos[0], item.map_y-pos[1])
                ndist = dist + leg
                nminutes = minutes + _activity_minutes(item, cfg)
                nfavor = favor + item.favor
                # Penalize low-confidence candidates slightly; favor overshoot is fine.
                confidence_penalty = (1.0 - item.confidence) * 18.0
                nscore = ndist * cfg.route_distance_weight + nminutes * cfg.route_activity_weight + confidence_penalty
                state = (nscore, ndist, nminutes, nfavor, item.point, used + (i,))
                if nfavor >= needed:
                    finished.append(state)
                else:
                    nxt.append(state)
        if finished and _depth >= 2:
            # Once enough complete paths exist, deeper paths are rarely useful.
            finished.sort(key=lambda s: s[0])
            if len(finished) >= beam_width // 2:
                break
        nxt.sort(key=lambda s: (s[0] - s[3] * 65.0, s[0]))
        beam = nxt[:beam_width]
        if not beam:
            break

    if not finished:
        # Not enough total favor; route through all available by efficiency.
        seq = sorted(ranked, key=lambda x: (-x.favor / max(0.5, _activity_minutes(x, cfg)), -x.confidence))
        dist = 0.0
        mins = 0.0
        pos = start
        for x in seq:
            dist += math.hypot(x.map_x-pos[0], x.map_y-pos[1])
            mins += _activity_minutes(x, cfg)
            pos = x.point
        return RoutePlan(seq, sum(x.favor for x in seq), dist, mins, dist + mins*cfg.route_activity_weight)

    best = min(finished, key=lambda s: s[0])
    score, dist, minutes, favor, _pos, used = best
    seq = [ranked[i] for i in used]
    return RoutePlan(seq, favor, dist, minutes, score)
