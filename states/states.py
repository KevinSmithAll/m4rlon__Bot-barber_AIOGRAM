from aiogram.fsm.state import State, StatesGroup


class New_ticket(StatesGroup):
    surname = State()
    number = State()
    date = State()
    time = State()
