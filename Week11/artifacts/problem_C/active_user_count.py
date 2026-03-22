from __future__ import annotations

import random
from pathlib import Path


def generate_log_file(
    path: Path,
    *,
    num_events: int,
    num_users: int = 200_000,
    num_pages: int = 2_000,
    seed: int = 42,
) -> None:
    rng = random.Random(seed)
    pages = [f"/page/{i}" for i in range(num_pages)]

    with path.open("w", encoding="utf-8") as f:
        for event_index in range(num_events):
            timestamp = f"2026-03-22T{event_index % 24:02d}:{event_index % 60:02d}:00"
            user_id = rng.randint(1, num_users)
            page = pages[rng.randint(0, len(pages) - 1)]
            f.write(f"{timestamp},{user_id},{page}\n")


def count_active_users(path: Path, min_events: int = 3) -> int:
    """
    Return the exact number of users who appear at least `min_events` times.

    Input format:
    - One CSV record per line: "<timestamp>,<user_id>,<page>"
    - Example: "2026-03-22T13:45:00,42,/page/17"

    Required behavior:
    - Count total events per user exactly.
    - Return how many distinct users have at least `min_events` events.
    - Do not use approximations.

    Constraints for this task:
    - The full input may be much larger than available RAM.
    - The implementation must remain exact on very large files.
    - You may redesign the algorithm and data structures completely.

    Edit only this function.
    """
    raise NotImplementedError("Implement the exact counting algorithm here.")
