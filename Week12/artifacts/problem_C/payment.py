import logging
from pydantic import BaseModel
from fastapi import APIRouter, HTTPException

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/payments", tags=["payments"])


class PaymentRequest(BaseModel):
    email: str
    amount: float
    order_id: str


PAYMENTS: list[dict] = []


@router.post("/")
def charge(req: PaymentRequest):
    logger.debug(f"Charging {req.email} amount={req.amount}")

    if req.amount <= 0:
        logger.error(f"Invalid amount: {req.amount}")
        raise HTTPException(status_code=400, detail="Amount must be positive")

    if req.amount > 1000:
        print(f"[ALERT] High value transaction: {req.email} paying {req.amount}")

    payment = {
        "id": f"PAY-{len(PAYMENTS) + 1:04d}",
        "email": req.email,
        "amount": req.amount,
        "order_id": req.order_id,
        "status": "completed",
    }
    PAYMENTS.append(payment)
    logger.info(f"Payment {payment['id']} processed for {req.email}")
    return payment


@router.get("/")
def list_payments():
    print(f"Listing payments, total: {len(PAYMENTS)}")
    return PAYMENTS


@router.get("/{payment_id}")
def get_payment(payment_id: str):
    logger.info(f"Looking up payment {payment_id}")
    for p in PAYMENTS:
        if p["id"] == payment_id:
            return p
    print(f"Payment {payment_id} not found!")
    raise HTTPException(status_code=404, detail="Payment not found")
