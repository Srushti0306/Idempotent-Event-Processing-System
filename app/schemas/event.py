from pydantic import BaseModel, Field
from typing import Literal
from uuid import UUID


class EventCreate(BaseModel):

    event_id: UUID

    user_id: str = Field(min_length=1)

    amount_cents: int = Field(gt=0)

    event_type: Literal["PAYMENT"]