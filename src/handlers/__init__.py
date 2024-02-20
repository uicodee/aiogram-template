from aiogram import Dispatcher

from src.handlers import commands


def setup(dp: Dispatcher):
    commands.setup(dp)
