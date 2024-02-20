from datetime import datetime

from pydantic import BaseModel


def serialize_time(value: datetime) -> str:
    return value.strftime("%d.%m.%Y")


class Base(BaseModel):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        json_encoders = {datetime: serialize_time}
        from_attributes = True
        populate_by_name = True
