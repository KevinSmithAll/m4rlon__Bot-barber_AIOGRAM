# from aiogram import Router, F
# from aiogram.types import Message, CallbackQuery, ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
# from aiogram.filters import CommandStart, Command
# import keyboards.keyboards as kb
# from states import New_ticket
# from aiogram.fsm.state import default_state
# from aiogram.fsm.context import FSMContext
# from aiogram.filters import StateFilter


# router = Router()


# @router.message(CommandStart())
# async def cmd_start(message: Message):
#     await message.answer("Здравствуйте, добро пожаловать к Владимиру Оболенцеву",
#                          reply_markup=kb.user_menu)


# @router.callback_query(F.data == "create_ticket")
# async def create_ticket(callback: CallbackQuery, state: FSMContext):
#     await callback.message.answer("Создание записи")
#     await state.set_state(New_ticket.surname)
#     await callback.message.answer("Введите Вашу фамилию", reply_markup=cancel_kb)


# @router.message(default_state, F.text.lower() == "отмена")
# async def cmd_cancel_no_state(message: Message, state: FSMContext):
#     # Стейт сбрасывать не нужно, удалим только данные
#     await state.set_data({})
#     await message.answer(
#         text="Нечего отменять",
#         reply_markup=ReplyKeyboardRemove()
#     )


# @router.message(F.text.lower() == "отмена")
# async def cancel(message: Message, state: FSMContext):
#     print('Вызвалась отмена')
#     await state.clear()
#     await message.answer(
#         text="Действие отменено",
#         reply_markup=ReplyKeyboardRemove()
#     )


# @router.message(New_ticket.surname)
# async def surname(message: Message, state: FSMContext):
#     if len(message.text) < 3:
#         return await message.answer("Введена слишком короткая фамилия, введите еще раз")
#     await state.update_data(surname=message.text)
#     await state.set_state(New_ticket.number)
#     await message.answer("Введите Ваш номер телефона", reply_markup=cancel_kb)


# @router.message(New_ticket.number)
# async def number(message: Message, state: FSMContext):
#     await state.update_data(number=message.text)
#     await state.set_state(New_ticket.date)
#     await message.answer("Введите дату записи", reply_markup=cancel_kb)


# @router.message(New_ticket.date)
# async def date(message: Message, state: FSMContext):
#     await state.update_data(date=message.text)
#     await state.set_state(New_ticket.time)
#     await message.answer("Введите время записи", reply_markup=cancel_kb)


# @router.message(New_ticket.time)
# async def time(message: Message, state: FSMContext):
#     await state.update_data(time=message.text)
#     data = await state.get_data()
#     await message.answer(f"Успех! Ваша запись:\nФамилия: {data['surname']}\nТелефон: {data['number']}\nДата: {data['date']}\nВремя: {data['time']}")
#     await state.clear()
