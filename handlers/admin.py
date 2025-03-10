from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command, Filter
from keyboards.keyboards import admin_menu, get_week_tickets_kb, cancel_kb
from database.database import Database
from aiogram.types import BufferedInputFile, ReplyKeyboardRemove
from states.states import Marker, Marker_not_Ready
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import default_state
from functions.logging import Logger

Logs = Logger()


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


@admin_router.callback_query(F.data == "admin_export")
async def admin_export(callback: CallbackQuery):
    await callback.message.answer(text="Выгружаю файл")
    db_sql = Database()
    buffer = db_sql.get_bytes()
    db_sql.close_connection()
    files = BufferedInputFile(buffer.getvalue(), filename="Записи.xlsx")
    await callback.message.answer_document(files)


@admin_router.callback_query(F.data == "admin_marker_ready")
async def admin_marker_ready(callback: CallbackQuery, state: FSMContext):
    Logs.warning("Нажал кнопку пометить как готовую")
    await callback.message.edit_reply_markup()
    await callback.message.answer("Введите дату записи",
                                  reply_markup=cancel_kb)
    await state.set_state(Marker.date)


@admin_router.message(default_state, F.text.lower() == "отмена")
async def cmd_cancel_no_state(message: Message, state: FSMContext):
    await state.set_data({})
    await message.answer(
        text="Нечего отменять",
        reply_markup=ReplyKeyboardRemove()
    )


@admin_router.message(F.text.lower() == "отмена")
async def cancel(message: Message, state: FSMContext):
    print('Вызвалась отмена')
    await state.clear()
    await message.answer(
        text="Действие отменено",
        reply_markup=ReplyKeyboardRemove()
    )


@admin_router.message(Marker.date)
async def get_date(message: Message, state: FSMContext):
    Logs.warning("Получил дату")
    await state.update_data(date=message.text)
    await state.set_state(Marker.time)
    await message.answer("Введите Время записи", reply_markup=cancel_kb)
    Logs.warning("Жду время")


@admin_router.message(Marker.time)
async def time(message: Message, state: FSMContext):
    await state.update_data(time=message.text)
    Logs.warning("Получил время")
    data = await state.get_data()
    Logs.warning("Получил всё что нужно")
    db_sql = Database()
    try:
        db_sql.mark_ready(date=data["date"],
                          time=data["time"])
        Logs.warning("Заносит в БД")
        await message.answer(f"Запись {data['date']}, {data['time']} помечена как готовая",
                             reply_markup=ReplyKeyboardRemove())
    except Exception as e:
        await message.answer(f"Записи не существует.\nОшибка: {e}")
    finally:
        await state.clear()
        db_sql.close_connection()


@admin_router.callback_query(F.data == "admin_marker_not_ready")
async def admin_marker_not_ready(callback: CallbackQuery, state: FSMContext):
    Logs.warning("Нажал кнопку пометить как НЕ готовую")
    await callback.message.edit_reply_markup()
    await callback.message.answer("Введите дату записи",
                                  reply_markup=cancel_kb)
    await state.set_state(Marker_not_Ready.date)


@admin_router.message(Marker_not_Ready.date)
async def get_date_not_ready(message: Message, state: FSMContext):
    await state.update_data(date=message.text)
    await state.set_state(Marker_not_Ready.time)
    await message.answer("Введите Время записи", reply_markup=cancel_kb)


@admin_router.message(Marker_not_Ready.time)
async def time_not_ready(message: Message, state: FSMContext):
    await state.update_data(time=message.text)
    await state.set_state(Marker_not_Ready.comment)
    await message.answer("Введите комментарий", reply_markup=cancel_kb)


@admin_router.message(Marker_not_Ready.comment)
async def comment_not_ready(message: Message, state: FSMContext):
    await state.update_data(comment=message.text)
    data = await state.get_data()
    db_sql = Database()
    try:
        db_sql.mark_not_ready(date=data["date"],
                              time=data["time"],
                              comment=data["comment"])
        Logs.warning("Заносит в БД")
        await message.answer(f"Запись {data['date']}, {data['time']} помечена как НЕ готовая по причине {data['comment']}",
                             reply_markup=ReplyKeyboardRemove())
    except Exception as e:
        await message.answer(f"Записи не существует.\nОшибка: {e}")
    finally:
        await state.clear()
        db_sql.close_connection()


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


@admin_router.callback_query(F.data == "admin_stats")
async def check_stats(callback: CallbackQuery):
    db_sql = Database()
    ready_tickets = db_sql.get_ready_tickets()
    not_ready_tickets = db_sql.get_not_ready_tickets()
    message = f'На текущий момент:\n' \
        f'Выполненных записей: {ready_tickets}\n' \
        f'Не выполненных записей: {not_ready_tickets}'
    await callback.message.answer(text=message)
