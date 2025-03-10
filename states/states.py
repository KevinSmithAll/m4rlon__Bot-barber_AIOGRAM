from aiogram.fsm.state import State, StatesGroup


class New_ticket(StatesGroup):
    surname = State()
    number = State()
    date = State()
    time = State()


class Marker(StatesGroup):
    date = State()
    time = State()


class Marker_not_Ready(StatesGroup):
    date = State()
    time = State()
    comment = State()
