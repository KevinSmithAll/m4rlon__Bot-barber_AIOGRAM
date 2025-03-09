from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command, Filter
from keyboards.keyboards import admin_menu
from database.database import Database


class IsAdmin(Filter):
    def __init__(self):
        pass

    async def __call__(self, message: Message) -> bool:
        return message.from_user.id == 890424948


admin_router = Router()
admin_router.message.filter(IsAdmin())


@admin_router.message(Command(commands=['admin']))
async def admin(message: Message):
    await message.answer(text="Вы вошли в админ панель", reply_markup=admin_menu)


@admin_router.callback_query(F.data == "admin_today")
async def admin_today(callback: CallbackQuery):
    db_sql = Database()
    tickets_today = db_sql.check_today()
    if tickets_today:
        for number, ticket in enumerate(tickets_today):
            msg = f"{number+1}. Фамилия: {ticket[0]}\n" \
                f"Номер телефона: {ticket[1]}\n" \
                f"Дата записи: {ticket[2]}\n" \
                f"Время записи: {ticket[3]}\n"
            await callback.message.answer(text=msg)
    else:
        await callback.message.answer(text="Сегодня нет записей, отдыхаем")
