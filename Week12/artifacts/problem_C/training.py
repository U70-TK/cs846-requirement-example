import sys
from pydantic import BaseModel
from fastapi import APIRouter

router = APIRouter(prefix="/training", tags=["training"])


class TrainRequest(BaseModel):
    dataset: list[str]
    epochs: int = 3


TRAINING_RUNS: list[dict] = []


@router.post("/run")
def train(req: TrainRequest):
    run_id = f"RUN-{len(TRAINING_RUNS) + 1:04d}"
    print("training started, run_id=" + run_id)

    results = []
    for epoch in range(req.epochs):
        for batch in req.dataset:
            sys.stdout.write(f"[{run_id}] epoch {epoch + 1}: processing {batch}\n")
            results.append({"epoch": epoch + 1, "batch": batch, "status": "done"})

    print("training finished for " + run_id)
    run = {"id": run_id, "epochs": req.epochs, "batches": len(req.dataset), "status": "completed"}
    TRAINING_RUNS.append(run)
    return run


@router.get("/runs")
def list_runs():
    sys.stderr.write(f"DEBUG: listing {len(TRAINING_RUNS)} training runs\n")
    return TRAINING_RUNS
