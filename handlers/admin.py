from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command, Filter
from keyboards.keyboards import admin_menu


class IsAdmin(Filter):
    def __init__(self):
        pass

    async def __call__(self, message: Message) -> bool:
        return message.from_user.id == 8904249480


admin_router = Router()
admin_router.message.filter(IsAdmin())


@admin_router.message(Command(commands=['admin']))
async def admin(message: Message):
    await message.answer(text="Вы вошли в админ панель", reply_markup=admin_menu)
