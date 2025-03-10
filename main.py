from aiogram import Bot, Dispatcher
import asyncio
import handlers
from aiogram.fsm.strategy import FSMStrategy
from apscheduler.schedulers.asyncio import AsyncIOScheduler
import datetime


async def main():
    bot = Bot(token="7990808992:AAFPFFG_3HriAwol8hGkUpUr9lbBytg_Y0U")
    dp = Dispatcher(FSMStrategy=FSMStrategy.USER_IN_CHAT)

    schedular = AsyncIOScheduler(timezone='Europe/Moscow')
    schedular.add_job(handlers.month_message,
                      trigger='cron',
                      day=1,
                      kwargs={'bot': bot})
    schedular.start()

    dp.include_router(router=handlers.start_router)
    dp.include_router(router=handlers.new_ticket_router)
    dp.include_router(router=handlers.check_ticket_router)
    dp.include_router(router=handlers.delete_ticket_router)
    dp.include_router(router=handlers.admin_router)
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
