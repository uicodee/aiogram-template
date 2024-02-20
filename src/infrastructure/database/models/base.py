from datetime import datetime

from sqlalchemy import (
    DateTime,
    func,
    BigInteger,
)
from sqlalchemy.orm import (
    declarative_base,
    Mapped,
    mapped_column,
)

Base = declarative_base()
metadata = Base.metadata


class BaseModel(Base):
    __abstract__ = True

    id: Mapped[int] = mapped_column(
        BigInteger,
        autoincrement=True,
        primary_key=True,
    )
    created_at: Mapped[datetime] = mapped_column(
        DateTime(True), server_default=func.now()
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(True),
        default=func.now(),
        onupdate=func.now(),
        server_default=func.now(),
    )
