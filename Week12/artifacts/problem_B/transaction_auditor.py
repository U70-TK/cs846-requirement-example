import logging
from dataclasses import dataclass
from datetime import datetime
from typing import List

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
    """Returns a rejection reason string, or None if valid."""
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
    """
    Process a batch of transactions.
    Returns (approved_list, rejected_list).

    TODO: Add logging here following the unified logging guidelines.
    The compliance requirement mandates one log entry per rejected
    transaction, including: transaction_id, amount, reason, timestamp.
    """
    approved = []
    rejected = []

    for tx in transactions:
        reason = validate_transaction(tx)
        if reason:
            rejected.append(RejectionResult(transaction=tx, reason=reason))
            logger.warning(
                "Transaction rejected.",
                extra={
                    "transaction_id": tx.transaction_id,
                    "amount": tx.amount,
                    "reason": reason,
                    "timestamp": tx.timestamp
                }
            )
        else:
            approved.append(tx)

    return approved, rejected