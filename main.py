from aiogram import Bot, Dispatcher
import asyncio
import handlers
from aiogram.fsm.strategy import FSMStrategy


async def main():
    bot = Bot(token="7990808992:AAFPFFG_3HriAwol8hGkUpUr9lbBytg_Y0U")
    dp = Dispatcher(FSMStrategy=FSMStrategy.USER_IN_CHAT)  # type: ignore
    dp.include_router(router=handlers.start_router)
    dp.include_router(router=handlers.new_ticket_router)
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
