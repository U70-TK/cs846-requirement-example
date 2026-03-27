import logging
from dataclasses import dataclass
from datetime import datetime
from typing import List

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


@dataclass
class Transaction:
    transaction_id: str
    amount: float
    currency: str
    merchant_id: str
    timestamp: datetime


@dataclass
class RejectionResult:
    transaction: Transaction
    reason: str


DAILY_LIMIT = 10_000.0
BLOCKED_MERCHANTS = {"merchant_99", "merchant_42"}


def validate_transaction(tx: Transaction) -> str | None:
    if tx.amount <= 0:
        return "non_positive_amount"
    if tx.amount > DAILY_LIMIT:
        return "exceeds_daily_limit"
    if tx.merchant_id in BLOCKED_MERCHANTS:
        return "blocked_merchant"
    if tx.currency not in ("USD", "CAD", "EUR"):
        return "unsupported_currency"
    return None


def process_transactions(
    transactions: List[Transaction],
) -> tuple[List[Transaction], List[RejectionResult]]:

    # Guideline 6: 1 INFO log per major stage
    logger.info("Starting batch processing", extra={
        "batch_size": len(transactions)
    })

    approved = []
    rejected = []

    for tx in transactions:
        reason = validate_transaction(tx)
        if reason:
            rejected.append(RejectionResult(transaction=tx, reason=reason))
        else:
            approved.append(tx)

    # Guideline 6: summary only, no per-record logs
    logger.info("Batch processing complete", extra={
        "batch_size": len(transactions),
        "approved_count": len(approved),
        "rejected_count": len(rejected)
    })

    return approved, rejected


if __name__ == "__main__":
    transactions = [
        Transaction("txn_001", 500, "USD", "merchant_1", datetime.now()),
        Transaction("txn_002", 15000, "USD", "merchant_2", datetime.now()),
        Transaction("txn_003", 100, "CAD", "merchant_99", datetime.now()),
    ]

    approved, rejected = process_transactions(transactions)



    print("Approved Transactions:")
    for tx in approved:
        print(f"  - {tx.transaction_id}: {tx.amount} {tx.currency}")

    print("\nRejected Transactions:")
    for result in rejected:
        print(f"  - {result.transaction.transaction_id}: {result.reason}")


