import logging
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from config import Settings


logger = logging.getLogger(__name__)


def make_connection_string(settings: Settings) -> str:
    url = (
        f"postgresql+asyncpg://{settings.db.user}:{settings.db.password}"
        f"@{settings.db.host}/{settings.db.name}"
        f"?async_fallback=True"
    )
    return url


def create_pool(url: str) -> sessionmaker:
    engine = create_async_engine(url, echo=False)
    return sessionmaker(
        bind=engine,
        expire_on_commit=False,
        class_=AsyncSession,
        future=True,
        autoflush=False,
    )
