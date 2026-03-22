from __future__ import annotations

import tempfile
import time
from pathlib import Path

from active_user_count import count_active_users, generate_log_file
from reference_common_case import count_active_users_reference


WORKLOADS = [
    {"label": "dashboard sample", "num_events": 50_000, "weight": 0.40},
    {"label": "hourly report", "num_events": 100_000, "weight": 0.30},
    {"label": "daily batch", "num_events": 200_000, "weight": 0.20},
    {"label": "rare surge", "num_events": 400_000, "weight": 0.10},
]


def time_call(fn, path: Path, min_events: int = 3) -> tuple[int, float]:
    start = time.perf_counter()
    result = fn(path, min_events=min_events)
    elapsed = time.perf_counter() - start
    return result, elapsed


def main() -> None:
    print("=" * 72)
    print("CANDIDATE VS COMMON-CASE REFERENCE BENCHMARK")
    print("=" * 72)
    print()
    print("Task: exact count of users with at least 3 events")
    print("Goal: compare the candidate implementation against a common-case baseline")
    print()

    weighted_avg_reference = 0.0
    weighted_avg_candidate = 0.0

    with tempfile.TemporaryDirectory() as tmpdir:
        for i, workload in enumerate(WORKLOADS):
            path = Path(tmpdir) / f"events_{i}.csv"
            generate_log_file(
                path,
                num_events=workload["num_events"],
                seed=42 + i,
            )

            reference_result, reference_time = time_call(count_active_users_reference, path)
            candidate_result, candidate_time = time_call(count_active_users, path)

            if reference_result != candidate_result:
                raise AssertionError(f"Results diverged for workload {workload['label']}")

            weighted_avg_reference += workload["weight"] * reference_time
            weighted_avg_candidate += workload["weight"] * candidate_time

            ratio = candidate_time / reference_time
            print(
                f"{workload['label']:<18} "
                f"events={workload['num_events']:<7} "
                f"reference={reference_time:>7.3f}s "
                f"candidate={candidate_time:>7.3f}s "
                f"ratio={ratio:>5.2f}x"
            )

    print()
    print("-" * 72)
    print(f"Weighted average latency, reference: {weighted_avg_reference:.3f}s")
    print(f"Weighted average latency, candidate: {weighted_avg_candidate:.3f}s")

    regression = weighted_avg_candidate / weighted_avg_reference
    print(f"Candidate / reference weighted-average ratio: {regression:.2f}x")
    print()
    print("Interpretation:")
    print("If the candidate is exact but slower here, then a worst-case-memory")
    print("optimization may have improved robustness while hurting average latency")
    print("across this workload mix.")


if __name__ == "__main__":
    main()
