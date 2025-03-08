from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from database.database import Database
from functions.logging import Logger
import keyboards as kb


Logs = Logger()
delete_ticket_router = Router()


@delete_ticket_router.callback_query(F.data.startswith('delete_'))
async def delete_ticket(callback: CallbackQuery):
    await callback.message.edit_reply_markup()
    date = callback.data.split("_")[1]
    time = callback.data.split("_")[2]
    db_sql = Database()
    try:
        db_sql.delete_ticket(date=date, time=time)
        await callback.message.answer("Запись успешно удалена")
    except Exception as error:
        await callback.message.answer(f"Произошла ошибка {error}")
