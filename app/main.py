from fastapi import FastAPI
from app.api.events import router as events_router


app = FastAPI(
    title="Distributed Idempotent Event Processing System",
    description="A fault-tolerant backend for processing events",
    version="1.0.0"
)


@app.get("/")
def root():
    return {
        "message": "Idempotent Event Processing API"
    }


@app.get("/health")
def health_check():
    return {
        "status": "healthy"
    }

app.include_router(events_router)