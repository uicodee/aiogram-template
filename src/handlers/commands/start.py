from aiogram import Router, types
from aiogram.filters import CommandStart

from src.infrastructure.database.dao import HolderDao

router = Router()


@router.message(CommandStart())
async def on_cmd_start(message: types.Message, dao: HolderDao):
    await message.answer(f"Hello, {message.from_user.full_name}!")
