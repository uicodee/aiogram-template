from aiogram import Dispatcher
from sqlalchemy.orm import sessionmaker

from .database import HolderMiddleware


def setup(dp: Dispatcher, pool: sessionmaker):
    dp.update.middleware(HolderMiddleware(pool=pool))
