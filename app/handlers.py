from aiogram import F, Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, CallbackQuery

# FSM - Механизм состояния
from aiogram.fsm.state import State, StatesGroup   
from aiogram.fsm.context import FSMContext

import app.keyboards as kb

import app.functions as function

import briefs.Animation_brief as animBrief
import briefs.Model_brief as modBrief
import briefs.Videomontage_brief as videoBrief
import briefs.Motion_brief as motBrief
import briefs.Miniapp_brief as miniappBrief
import briefs.Web_brief as webBrief
import briefs.Bots_brief as botsBrief

import BotAdmin.handlers as AdminBot

router_one_bot = Router()

class Brief(StatesGroup):
    brief = State()

@router_one_bot.message(CommandStart())
async def start_message(message: Message):
    await message.answer(f"""
👋 <b>Добро пожаловать, <em>{message.from_user.username}</em>!</b>

    🤖 Я — ваш цифровой помощник и часть команды агентства <b>Пантеон</b>.
    
<b>Кто мы такие?</b> 
    👤 Группа единомышленников в виде адекватных и компетентных людей!
Такие люди мы:  
- Ценят своё и чужое время; 
- Не любим долгие переговоры и лишнюю бюрократию;
- Мы ценим свое и чужое время.

📌 <b>Услуги:</b>  
<em>3D-моделирование  •  Монтаж  •  Сайты  •  Мини-приложения  •  Боты</em>
""", parse_mode='html', reply_markup=kb.general_service_btn)

@router_one_bot.callback_query(F.data == "clb_message_service_list")
async def service_list(callback: CallbackQuery):
    await callback.answer() # Уведомление

    await function.service_list_message(callback.message)

@router_one_bot.callback_query(F.data == "start_message_callback")
async def edit_start(callback: CallbackQuery):
    await callback.answer() # Уведомление

    await function.edit_start_message(callback.message)

list_service_name = ["Animation_callback", "Models_callback", "VideoMontage_callback", "Motion_callback", "MiniApp_callback", "Web_callback", "Bots_callback", "Consultation_callback"]
@router_one_bot.callback_query(F.data.in_(list_service_name))
async def service_info_callbacks(callback: CallbackQuery):
    await callback.answer() # Уведомление

    if callback.data == list_service_name[0]:
        await function.animation_message(callback.message)

    elif callback.data == list_service_name[1]:
        await function.models_message(callback.message)

    elif callback.data == list_service_name[2]:
        await function.videomontage_message(callback.message)

    elif callback.data == list_service_name[3]:
        await function.motion_message(callback.message)

    elif callback.data == list_service_name[4]:
        await function.miniapp_message(callback.message)

    elif callback.data == list_service_name[5]:
        await function.web_message(callback.message)

    elif callback.data == list_service_name[6]:
        await function.bots_message(callback.message)

    elif callback.data == list_service_name[7]:
        await function.consultation_message(callback.message)

list_brief_name = ["brief_animation_callback", "brief_models_callback", "brief_videomontage_callback", "brief_motion_callback", "brief_miniapp_callback", "brief_web_callback", "brief_bots_callback"]
@router_one_bot.callback_query(F.data.in_(list_brief_name))
async def brief_info_callbacks(callback: CallbackQuery, state: FSMContext):
    await callback.answer()

    if callback.data == list_brief_name[0]:
        await animBrief.message(callback.message)

    elif callback.data == list_brief_name[1]:
        await modBrief.message(callback.message)

    elif callback.data == list_brief_name[2]:
        await videoBrief.message(callback.message)

    elif callback.data == list_brief_name[3]:
        await motBrief.message(callback.message)

    elif callback.data == list_brief_name[4]:
        await miniappBrief.message(callback.messsage)

    elif callback.data == list_brief_name[5]:
        await webBrief.message(callback.message)

    elif callback.data == list_brief_name[6]:
        await botsBrief.message(callback.message)

    await state.set_state(Brief.brief)

@router_one_bot.message(Brief.brief)
async def send_brief_function(message: Message, state: FSMContext):
    await state.update_data(brief = message.text)

    data = await state.get_data()

    await AdminBot.send_brief_for_admin(data["brief"])

    await message.answer("Бриф отправлен", reply_markup=kb.return_in_service_list)

    await state.clear()
