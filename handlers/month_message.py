from aiogram import Bot
from database.database import Database


async def month_message(bot: Bot):
    db_sql = Database()
    ready_tickets = db_sql.get_ready_tickets()
    not_ready_tickets = db_sql.get_not_ready_tickets()
    msg = f'На текущий момент:\n' \
        f'Выполненных записей: {ready_tickets}\n' \
        f'Не выполненных записей: {not_ready_tickets}'
    await bot.send_message(chat_id=890424948, text=msg)
