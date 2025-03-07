from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton

user_menu = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Записаться на стрижку',
                          callback_data='create_ticket')],
    [InlineKeyboardButton(text='Мои записи',
                          callback_data='my_tickets')]
])

cancel_kb = ReplyKeyboardMarkup(
    keyboard=[[KeyboardButton(text='Отмена')]], resize_keyboard=True)


async def get_valiable_times():
    free_time: list[str] = []
    pass
"""
Основной смысл будет состоять в следующем:
При вызове определенной функции для получения свободных времен
мы проходимся по всем временам с заданным для дня недели шагом
делаем селекты из базы данных, проверяем на наличие записи на i-e время
Если на i-e время селект пустой, то добавляем это время в список свободных
Возвращаем список свободных времени
"""
