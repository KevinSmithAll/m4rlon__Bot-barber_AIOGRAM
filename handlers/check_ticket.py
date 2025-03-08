from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from database.database import Database
from functions.logging import Logger
import keyboards as kb


Logs = Logger()
check_ticket_router = Router()


@check_ticket_router.callback_query(F.data == "my_tickets")
async def my_tickets(callback: CallbackQuery):
    db_sql = Database()
    my_tickets = db_sql.check_my_ticket(tg_id=callback.from_user.id)
    Logs.info(
        message=f'Пользователь {callback.from_user.id} вызвал "МОИ ЗАПИСИ"')
    if my_tickets:
        for number, ticket in enumerate(my_tickets):
            msg = f"Заявка №{number+1}\n" \
                f"Дата записи на стрижку: {ticket[0]}\n" \
                f"Время записи на стрижку: {ticket[1]}\n"
            await callback.message.answer(text=msg,
                                          reply_markup=kb.delete_ticket_kb)
    else:
        await callback.message.answer(text="У вас нет записей")
