from typing import Callable, Dict, Any, Awaitable
from aiogram import BaseMiddleware
from aiogram.types import TelegramObject
from sqlalchemy.orm import sessionmaker

from src.infrastructure.database.dao import HolderDao


class HolderMiddleware(BaseMiddleware):
    def __init__(self, pool: sessionmaker):
        super().__init__()
        self.pool = pool

    async def __call__(
        self,
        handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
        event: TelegramObject,
        data: Dict[str, Any],
    ) -> Any:
        async with self.pool() as session:
            data["dao"] = HolderDao(session=session)
            result = await handler(event, data)
            return result
