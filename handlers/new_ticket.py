from aiogram import Router, F
from aiogram.types import CallbackQuery, ReplyKeyboardRemove, Message
from aiogram.fsm.context import FSMContext
from states.states import New_ticket
from keyboards.keyboards import cancel_kb, valiable_times
from aiogram.fsm.state import default_state
from functions.date import *
from database.database import Database
from functions.logging import Logger
from aiogram.filters import BaseFilter
from functions.time import get_avaliable_time

Logs = Logger()
new_ticket_router = Router()


class Data_check(BaseFilter):
    async def __call__(self, message: Message, state: FSMContext):
        db_sql = Database()
        temp_data = await state.get_data()
        data = temp_data['date']
        normal_time = get_avaliable_time(date=data)
        not_avaliable_tickets = db_sql.check_ticket(date=data)
        avaliable_time = tuple(
            set(not_avaliable_tickets).symmetric_difference(set(normal_time)))
        Logs.info(
            message=f'Пользователь {message.chat.id} решил стать самым умным')
        if message.text not in avaliable_time:
            await message.answer(text='Пожалуйста, выберете только из предложенных вариантов',
                                 reply_markup=await valiable_times(date=data))
        return message.text in avaliable_time


@new_ticket_router.callback_query(F.data == "create_ticket")
async def create_ticket(callback: CallbackQuery, state: FSMContext):
    Logs.info(
        message=f'Пользователь {callback.message.chat.id} нажал на кнопку "Создать заявку" в меню')
    await callback.message.edit_reply_markup()
    await callback.message.answer("Введите Вашу фамилию",
                                  reply_markup=cancel_kb)
    await state.set_state(New_ticket.surname)


@new_ticket_router.message(default_state, F.text.lower() == "отмена")
async def cmd_cancel_no_state(message: Message, state: FSMContext):
    await state.set_data({})
    await message.answer(
        text="Нечего отменять",
        reply_markup=ReplyKeyboardRemove()
    )


@new_ticket_router.message(F.text.lower() == "отмена")
async def cancel(message: Message, state: FSMContext):
    print('Вызвалась отмена')
    await state.clear()
    await message.answer(
        text="Действие отменено",
        reply_markup=ReplyKeyboardRemove()
    )


@new_ticket_router.message(New_ticket.surname)
async def surname(message: Message, state: FSMContext):
    await state.update_data(surname=message.text)
    await state.set_state(New_ticket.number)
    await message.answer("Введите Ваш номер телефона", reply_markup=cancel_kb)


@new_ticket_router.message(New_ticket.number)
async def number(message: Message, state: FSMContext):
    await state.update_data(number=message.text)
    await state.set_state(New_ticket.date)
    await message.answer("Введите дату записи в формате *день*.*месяц*.*год (например 06.03.2025)",
                         reply_markup=cancel_kb)


@new_ticket_router.message(New_ticket.date)
async def date(message: Message, state: FSMContext):
    if not is_valid_date(message.text):
        await message.answer('Неверный формат даты, попробуйте ещё раз')
        return
    if not is_past(message.text):
        await message.answer('Вы не можете записаться на прошедший день, попробуйте ещё раз')
        return
    try:
        await message.answer("Выберете время для записи из предложенных вариантов.",
                             reply_markup=await valiable_times(date=message.text))
    except Exception:
        await message.answer("На выбранную дату нет свободных мест, выберете другую дату\n(Введите в том же формате)")
        return
    await state.update_data(date=message.text)
    await state.set_state(New_ticket.time)


@new_ticket_router.message(New_ticket.time, Data_check())
async def time(message: Message, state: FSMContext):
    await state.update_data(time=message.text)
    data = await state.get_data()
    db_sql = Database()
    db_sql.create_ticket(
        tg_id=message.from_user.id,
        name=data['surname'],
        phone=data['number'],
        date=data['date'],
        time=data['time']
    )
    await message.answer(f"Успех! Ваша запись:\nФамилия: {data['surname']}\nТелефон: {data['number']}\nДата: {data['date']}\nВремя: {data['time']}",
                         reply_markup=ReplyKeyboardRemove())
    await state.clear()
