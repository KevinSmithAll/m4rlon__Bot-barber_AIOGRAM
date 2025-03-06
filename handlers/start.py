from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message
import keyboards as kb
import database as db

start_router = Router()


@start_router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer("Здравствуйте, добро пожаловать к Владимиру Оболенцеву",
                         reply_markup=kb.user_menu)
    user_db = db.Database()
    user_db.new_user(message.from_user.id)
