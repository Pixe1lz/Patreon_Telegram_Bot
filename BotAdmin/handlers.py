from aiogram import F, Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, CallbackQuery
from aiogram import Bot
import config

bot = Bot(token=config.BOT_TOKEN_TWO)

router_two_bot = Router()
chat_id = None

@router_two_bot.message(CommandStart())
async def start_message(message: Message):
    global chat_id
    chat_id = message.chat.id

    await message.answer("chat id сохранен")   

async def send_brief_for_admin(brief):                                        
    await bot.send_message(chat_id, brief)