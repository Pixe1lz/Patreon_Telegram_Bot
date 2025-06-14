# -*- coding: utf-8 -*-

import asyncio
import config

from aiogram import Bot, Dispatcher

from app.handlers import router_one_bot # События первого бота
from BotAdmin.handlers import router_two_bot # События второго бота 

bot_main = Bot(config.BOT_TOKEN_ONE)
bot_admin = Bot(config.BOT_TOKEN_TWO)

dp_main_bot = Dispatcher(bot=bot_main)
dp_admin_bot = Dispatcher(bot=bot_admin)

async def main():
    dp_main_bot.include_router(router_one_bot)
    dp_admin_bot.include_router(router_two_bot)
    
    await asyncio.gather (
        dp_main_bot.start_polling(bot_main),  
        dp_admin_bot.start_polling(bot_admin)
    )     

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Exit")