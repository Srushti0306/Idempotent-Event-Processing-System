from fastapi import APIRouter
from app.schemas.event import EventCreate

router = APIRouter(
    prefix="/events",
    tags=["Events"]
)


@router.post("")
def create_event(event: EventCreate):

    return {
        "event_id": event.event_id,
        "status": "received",
        "message": "Event received successfully"
    }