from pydantic import Field

from src.dto import Base


class User(Base):

    telegram_id: int
    full_name: str
    username: str | None = Field(default=None)
