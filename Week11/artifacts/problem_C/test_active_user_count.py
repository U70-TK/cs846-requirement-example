from __future__ import annotations

from pathlib import Path

from active_user_count import count_active_users


def write_log(path: Path, rows: list[tuple[str, int, str]]) -> None:
    with path.open("w", encoding="utf-8") as f:
        for timestamp, user_id, page in rows:
            f.write(f"{timestamp},{user_id},{page}\n")


def test_counts_users_meeting_threshold(tmp_path: Path) -> None:
    path = tmp_path / "events.csv"
    write_log(
        path,
        [
            ("2026-03-22T00:00:00", 1, "/a"),
            ("2026-03-22T00:01:00", 1, "/b"),
            ("2026-03-22T00:02:00", 1, "/c"),
            ("2026-03-22T00:03:00", 2, "/a"),
            ("2026-03-22T00:04:00", 2, "/b"),
            ("2026-03-22T00:05:00", 3, "/a"),
        ],
    )

    assert count_active_users(path, min_events=3) == 1


def test_counts_all_events_for_same_user(tmp_path: Path) -> None:
    path = tmp_path / "events.csv"
    write_log(
        path,
        [
            ("2026-03-22T00:00:00", 7, "/x"),
            ("2026-03-22T00:01:00", 7, "/x"),
            ("2026-03-22T00:02:00", 7, "/y"),
            ("2026-03-22T00:03:00", 8, "/z"),
        ],
    )

    assert count_active_users(path, min_events=3) == 1
    assert count_active_users(path, min_events=4) == 0


def test_empty_input(tmp_path: Path) -> None:
    path = tmp_path / "events.csv"
    write_log(path, [])

    assert count_active_users(path, min_events=3) == 0
