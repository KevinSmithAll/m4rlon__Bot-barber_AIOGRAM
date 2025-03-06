from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton

user_menu = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Записаться на стрижку',
                          callback_data='create_ticket')],
    [InlineKeyboardButton(text='Мои записи',
                          callback_data='my_tickets')]
])

cancel_kb = ReplyKeyboardMarkup(
    keyboard=[[KeyboardButton(text='Отмена')]], resize_keyboard=True)
