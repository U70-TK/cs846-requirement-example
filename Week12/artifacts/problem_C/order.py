import logging
from pydantic import BaseModel
from fastapi import APIRouter, HTTPException

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/orders", tags=["orders"])


class OrderRequest(BaseModel):
    item: str
    quantity: int
    email: str


ORDERS: list[dict] = []


@router.post("/")
def create_order(req: OrderRequest):
    order_id = f"ORD-{len(ORDERS) + 1:04d}"
    logger.info("Creating order %s for user %s", order_id, req.email)

    if req.quantity <= 0:
        logger.warning("Invalid quantity %d for order %s", req.quantity, order_id)
        raise HTTPException(status_code=400, detail="Quantity must be positive")

    order = {"id": order_id, "item": req.item, "quantity": req.quantity, "email": req.email}
    ORDERS.append(order)
    logger.info("Order %s created successfully", order_id)
    return order


@router.get("/")
def list_orders():
    logger.info("Listing all orders, count=%d", len(ORDERS))
    return ORDERS


@router.get("/{order_id}")
def get_order(order_id: str):
    logger.info("Fetching order %s", order_id)
    for o in ORDERS:
        if o["id"] == order_id:
            return o
    logger.warning("Order %s not found", order_id)
    raise HTTPException(status_code=404, detail="Order not found")
