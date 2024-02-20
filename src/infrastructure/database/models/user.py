from sqlalchemy import BigInteger, String
from sqlalchemy.orm import Mapped, mapped_column

from src.infrastructure.database.models import BaseModel


class User(BaseModel):

    __tablename__ = "user"

    telegram_id: Mapped[int] = mapped_column(BigInteger)
    full_name: Mapped[str] = mapped_column(String)
    username: Mapped[str] = mapped_column(String, nullable=True)
