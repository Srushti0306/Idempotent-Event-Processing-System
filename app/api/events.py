from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError

from app.schemas.event import EventCreate
from app.models.event import Event
from app.db.database import get_db
from uuid import UUID

router = APIRouter(
    prefix="/events",
    tags=["Events"]
)


@router.post("", status_code=201)
def create_event(
    event: EventCreate,
    db: Session = Depends(get_db)
):

    new_event = Event(
        event_id=event.event_id,
        user_id=event.user_id,
        amount_cents=event.amount_cents,
        event_type=event.event_type,
        status="PENDING"
    )

    db.add(new_event)   #it tells sqlalchemy to add the event into the db

    try:
        db.commit()   #commit permanently adds the data to db 

    except IntegrityError:
        db.rollback()

        raise HTTPException(
            status_code=409,
            detail="Event ID already exists or database constraint violated"
        )

    return {
        "event_id": event.event_id,
        "user_id": event.user_id,
        "status": "PENDING",
        "message": "Event saved successfully"
    }

@router.get("/{event_id}")
def get_event(
    event_id: UUID,
    db: Session=Depends(get_db)
):
    event=db.get(Event, event_id)

    if event is None:
        raise HTTPException(
            status_code=404,
            detail="Event not found"
            )

    return{
        "event_id": event.event_id,
        "user_id": event.user_id,
        "amount_cents": event.amount_cents,
        "event_type": event.event_type,
        "status": event.status
    }