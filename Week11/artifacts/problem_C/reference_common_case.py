from __future__ import annotations

from collections import defaultdict
from pathlib import Path


def count_active_users_reference(path: Path, min_events: int = 3) -> int:
    """
    Exact in-memory reference optimized for the common case.

    This keeps one counter per user in RAM and is typically the fastest choice
    when the workload comfortably fits in memory.
    """
    counts: dict[int, int] = defaultdict(int)

    with path.open("r", encoding="utf-8") as f:
        for line in f:
            _, user_id_text, _ = line.rstrip("\n").split(",", 2)
            counts[int(user_id_text)] += 1

    return sum(1 for count in counts.values() if count >= min_events)
