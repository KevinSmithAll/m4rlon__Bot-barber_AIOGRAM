from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton
import database as db
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from functions.time import get_avaliable_time


user_menu = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Записаться на стрижку',
                          callback_data='create_ticket')],
    [InlineKeyboardButton(text='Мои записи',
                          callback_data='my_tickets')]
])

cancel_kb = ReplyKeyboardMarkup(
    keyboard=[[KeyboardButton(text='Отмена')]], resize_keyboard=True)


async def valiable_times(date: str):
    keyboard = ReplyKeyboardBuilder()
    db_sql = db.Database()
    normal_time = get_avaliable_time(date=date)
    not_avaliable_tickets = db_sql.check_ticket(date=date)
    avaliable_time = tuple(
        set(not_avaliable_tickets).symmetric_difference(set(normal_time)))

    for time in avaliable_time:
        keyboard.add(KeyboardButton(text=time))
    return keyboard.adjust(4).as_markup()  # resize_keyboard=True)
