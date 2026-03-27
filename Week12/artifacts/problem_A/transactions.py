from __future__ import annotations

from dataclasses import dataclass
import hashlib
import random
import time
from typing import Dict, List


@dataclass(frozen=True)
class Transaction:
    transaction_id: str
    account_id: str
    amount: float
    merchant: str
    trace_id: str


def _risk_score(txn: Transaction) -> float:
    raw = f"{txn.account_id}|{txn.amount}|{txn.merchant}|{txn.transaction_id}"
    digest = hashlib.sha256(raw.encode("utf-8")).hexdigest()
    return int(digest[:8], 16) / 0xFFFFFFFF


def _evaluate_rules(txn: Transaction, score: float) -> List[str]:
    triggers: List[str] = []
    if txn.amount > 2000:
        triggers.append("high_amount")
    if txn.merchant in {"offshore-gaming", "crypto-mixer"}:
        triggers.append("risky_merchant")
    if score > 0.85:
        triggers.append("high_model_score")
    return triggers


def _decision(score: float, triggers: List[str]) -> str:
    if score > 0.92 or len(triggers) >= 2:
        return "deny"
    if score > 0.75:
        return "manual_review"
    return "approve"


def make_sample_transactions(n: int = 5000, seed: int = 7) -> List[Transaction]:
    random.seed(seed)
    merchants = [
        "grocery",
        "fuel",
        "electronics",
        "offshore-gaming",
        "crypto-mixer",
        "pharmacy",
    ]
    txns: List[Transaction] = []
    for i in range(n):
        txns.append(
            Transaction(
                transaction_id=f"txn_{i:06d}",
                account_id=f"acct_{random.randint(1000, 9999)}",
                amount=round(random.uniform(5, 5000), 2),
                merchant=random.choice(merchants),
                trace_id=f"trace_{random.randint(10_000_000, 99_999_999)}",
            )
        )
    return txns


def process_transactions(transactions: List[Transaction]) -> Dict[str, str]:
    """Initial version: core logic with no logging."""
    decisions_by_txn_id: Dict[str, str] = {}
    for txn in transactions:
        score = _risk_score(txn)
        triggers = _evaluate_rules(txn, score)
        decision = _decision(score, triggers)
        decisions_by_txn_id[txn.transaction_id] = decision
    return decisions_by_txn_id


def run() -> None:
    txns = make_sample_transactions()
    t0 = time.perf_counter()
    decisions = process_transactions(txns)
    elapsed_ms = (time.perf_counter() - t0) * 1000
    print("=== Problem A Initial Code (No Logging) ===")
    print(f"processed_transactions={len(txns)}")
    print(f"decisions={len(decisions)}")
    print(f"runtime_ms={elapsed_ms:.2f}")


if __name__ == "__main__":
    run()
