from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton,
                           InlineKeyboardButton, InlineKeyboardMarkup)

general_service_btn = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="📋 Выбрать услугу", callback_data="clb_message_service_list")],    
    [InlineKeyboardButton(text="💲 Цены", callback_data="clb_send_file_price")],
    [InlineKeyboardButton(text="Сайт", url="https://пантеон.tech/")]    
])

service_list_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="🍏 3D-анимация", callback_data="Animation_callback"),
     InlineKeyboardButton(text="🍏 3D-модели", callback_data="Models_callback")],    
    
    [InlineKeyboardButton(text="🍐 Видеомонтаж", callback_data="VideoMontage_callback"),
     InlineKeyboardButton(text="🍐 Motion", callback_data="Motion_callback")],    
   
    [InlineKeyboardButton(text="🍊 Мини-приложения", callback_data="MiniApp_callback"),
     InlineKeyboardButton(text="🍓 Разработка сайтов", callback_data="Web_callback")],
    
    [InlineKeyboardButton(text="🍌 Боты", callback_data="Bots_callback"),
     InlineKeyboardButton(text="🍉 Консультация", callback_data="Consultation_callback")],

    [InlineKeyboardButton(text="Главная", callback_data="start_message_callback")]
])

return_in_service_list = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Вернуться 🔙", callback_data="clb_message_service_list")]    
])

def create_inline_service_keyboard(callback_name):
    cancel_btn = InlineKeyboardButton(text="Вернуться 🔙", callback_data="clb_message_service_list")
    help_contact_btn = InlineKeyboardButton(text="Связаться напрямую", callback_data="help_contact_callback")

    text_brief_btn = "📝 Заполнить бриф"

    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text=text_brief_btn, callback_data=callback_name)],
        [help_contact_btn],
        [cancel_btn]
    ])

    return keyboard

animation_inline_keyboard = create_inline_service_keyboard("brief_animation_callback")

models_inline_keyboard = create_inline_service_keyboard("brief_models_callback")

videomontage_inline_keyboard = create_inline_service_keyboard("brief_videomontage_callback")

motion_inline_keyboard = create_inline_service_keyboard("brief_motion_callback")

miniapp_inline_keyboard = create_inline_service_keyboard("brief_miniapp_callback")

web_inline_keyboard = create_inline_service_keyboard("brief_web_callback")

bots_inline_keyboard = create_inline_service_keyboard("brief_bots_callback") 

consultation_inline_keyboard = create_inline_service_keyboard("brief_consultation_callback")   