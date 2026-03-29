import logging
from fastapi import FastAPI
from auth import router as auth_router
from order import router as order_router
from payment import router as payment_router
from user_service import router as user_router
from training import router as training_router

logging.basicConfig(level=logging.DEBUG)

app = FastAPI(title="Student Store API")

app.include_router(auth_router)
app.include_router(order_router)
app.include_router(payment_router)
app.include_router(user_router)
app.include_router(training_router)


@app.get("/health")
def health():
    logging.warning("Health check hit")
    return {"status": "ok"}
