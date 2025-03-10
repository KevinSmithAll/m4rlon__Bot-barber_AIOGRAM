from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command, Filter
from keyboards.keyboards import admin_menu, get_week_tickets_kb
from database.database import Database
from aiogram.types import BufferedInputFile


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


@admin_router.callback_query(F.data == "admin_7_days")
async def admin_7_days(callback: CallbackQuery):
    await callback.message.answer(text="Выберите день недели",
                                  reply_markup=await get_week_tickets_kb())


@admin_router.callback_query(F.data.startswith('Дата_'))
async def admin_date(callback: CallbackQuery):
    date = callback.data.split('_')[1]
    db_sql = Database()
    tickets = db_sql.check_any_day(date=date)
    if tickets:
        for number, ticket in enumerate(tickets):
            msg = f"{number+1}. Фамилия: {ticket[0]}\n" \
                f"Номер телефона: {ticket[1]}\n" \
                f"Дата записи: {ticket[2]}\n" \
                f"Время записи: {ticket[3]}\n"
            await callback.message.answer(text=msg)
    else:
        await callback.message.answer(text="Нет записей, отдыхаем")


@admin_router.callback_query(F.data == "admin_any_day")
async def admin_any_day(callback: CallbackQuery):
    await callback.message.answer(text="Введите дату в формате ДД.ММ.ГГГГ")


@admin_router.message()
async def check_date(message: Message):
    db_sql = Database()
    tickets = db_sql.check_any_day(date=message.text)
    if tickets:
        for number, ticket in enumerate(tickets):
            msg = f"{number+1}. Фамилия: {ticket[0]}\n" \
                f"Номер телефона: {ticket[1]}\n" \
                f"Дата записи: {ticket[2]}\n" \
                f"Время записи: {ticket[3]}\n"
            await message.answer(text=msg)
    else:
        await message.answer(text="Нет записей, отдыхаем")


@admin_router.callback_query(F.data == "admin_export")
async def admin_export(callback: CallbackQuery):
    await callback.message.answer(text="Выгружаю файл")
    db_sql = Database()
    buffer = db_sql.get_bytes()
    db_sql.close_connection()
    files = BufferedInputFile(buffer.getvalue(), filename="Записи.xlsx")
    await callback.message.answer_document(files)
