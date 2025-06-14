﻿import asyncio
import app.keyboards as kb

async def edit_start_message(message):
    await message.edit_text(f"""
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

async def service_list_message(message):
    await message.edit_text(""" 
    <b>Какие задачи мы решаем для вас?</b>
    
<u>Список услуг</u>:
🍏 3D-анимации и 3D-модели
🍐 Видеомонтаж и Motion-дизайн
🍊 Разработка мини-приложений
🍓 Разработка сайтов под ключ
🍌 Разработка ботов
🍉 Консультация
    
⚡️<em>Узнай подробнее — нажми на нужную кнопку ниже!</em>    
""", parse_mode='html', reply_markup=kb.service_list_keyboard)

async def animation_message(message):
    await message.edit_text("""<b>🍏 3D-анимации</b>

<b>Описание</b>:       
✨ Когда обычная графика перестаёт впечатлять — настало время оживить реальность.

Мы создаём <b>реалистичные</b> и <b>стилизованные 3D-модели</b>: от продуктов до персонажей, от архитектурных форм до фантастических миров.

🎬 А затем — вдохнём в них жизнь с помощью анимации.

Ваш продукт будет не просто показан — он станет понятным, запоминающимся и желанным.

✅ Идеально для рекламы, презентаций, метавселенных и многого другого.
""", parse_mode='html', reply_markup=kb.animation_inline_keyboard)

async def models_message(message):
    await message.edit_text("""<b>🍏 3D-модели</b>

<b>Описание</b>:       
✨ Когда обычная графика перестаёт впечатлять — настало время оживить реальность.

Мы создаём <b>реалистичные</b> и <b>стилизованные 3D-модели</b>: от продуктов до персонажей, от архитектурных форм до фантастических миров.

🎬 А затем — вдохнём в них жизнь с помощью анимации.

Ваш продукт будет не просто показан — он станет понятным, запоминающимся и желанным.

✅ Идеально для рекламы, презентаций, метавселенных и многого другого.
""", parse_mode='html', reply_markup=kb.models_inline_keyboard)

async def videomontage_message(message):
    await message.edit_text("""<b>🍐 Видеомонтаж</b>

<b>Описание</b>:
Это очень скрупулёзная работа, в которой важно учитывать множество компонентов:

🎨 <b>Цветовая гамма</b>  
⚡️ <b>Динамичность</b>  
🔍 <b>Крупность планов</b> 
🎧 <b>Саунд-дизайн</b>  
🌀 <b>3D-объекты</b>  
✨ <b>Переходы</b>  
🎞️ <b>Подбор футажей</b> и многое другое.

Каждый элемент — ключ к созданию по-настоящему впечатляющего результата.
""", parse_mode='html', reply_markup=kb.videomontage_inline_keyboard)

async def motion_message(message): 
    await message.edit_text("""<b>🍐 Motion-дизайн</b>

<b>Описание</b>:
Это очень скрупулёзная работа, в которой важно учитывать множество компонентов:

🎨 <b>Цветовая гамма</b>  
⚡️ <b>Динамичность</b>  
🔍 <b>Крупность планов</b> 
🎧 <b>Саунд-дизайн</b>  
🌀 <b>3D-объекты</b>  
✨ <b>Переходы</b>  
🎞️ <b>Подбор футажей</b> и многое другое.

Каждый элемент — ключ к созданию по-настоящему впечатляющего результата.
""", parse_mode='html', reply_markup=kb.motion_inline_keyboard)

async def miniapp_message(message):
    await message.edit_text("""<b>🍊 Разработка мини-приложений</b>

<b>Описание</b>:       
Мини-приложения наподобие «<em>Hamster Kombat</em>, <em>TapSwap</em>»  
✨ С Вас — концепция, с нас — воплощение.

Наши разработки — это симбиоз креатива и холодной расчетливости, а главное — баланс между ними, который обеспечивает продажи.  
Мы об этом знаем, а теперь и Вы.

⚡️ Ещё ни одно сотрудничество не состоялось с помощью телепатии, поэтому <b>поделитесь своей проблемой</b>.
""", parse_mode='html', reply_markup=kb.miniapp_inline_keyboard)

async def web_message(message):
    await message.edit_text("""<b>🍓 Разработка сайтов</b>

<b>Описание</b>:
Сочленение ума и креатива, нити безумия и здравомыслия, апогей вложения прикладной науки и психологических триггеров.
Если напишу так, то — звучит вульгарно и непонятно, мы за <b>взрослый диалог</b>.

Юзаем:  
💻 Используем современные языки программирования,  
🛠️ Конструкторы сайтов — всё для создания вашего успешного проекта.
    
Создадим <b>инструмент монетизации</b> для Вашего бизнеса (услуги).
""", parse_mode='html', reply_markup=kb.web_inline_keyboard)

async def bots_message(message):
    await message.edit_text("""<b>🍌 Разработка ботов</b>

<b>Описание</b>:
✨ <em><b>Бот любой сложности для бизнеса.</b></em>  
Он не спит, не берет больничный, не жалуется на работу.  
При необходимости интегрируем в Вашу систему под ключ.

🔒 За утечку данных можете не переживать — бот не собирает данные.  
Это <b>бот</b>, а не супер-ультра-мультиварка, с ним взаимодействовать гораздо проще.

<u>В чем польза Бота?</u>  
Можно много говорить о пользе, но это всё абстракции.  
Мы предпочитаем <b>реализм</b> и <b>прагматизм</b>.

Сообщите нам свой запрос, и от него будем отталкиваться.
""", parse_mode='html', reply_markup=kb.bots_inline_keyboard)

async def consultation_message(message):
    await message.edit_text("""<b>🍉 Консультация</b>

<b>Описание</b>:
    🌝 У нас есть: <b>помощь зала</b>, <b>звонок другу</b>, <b>последнее желание</b>.  
Только не обращайтесь по поводу грыжи Шморля, завоевания мира и проблем в отношениях, хотя — не проблема, могу и по этому поводу проконсультировать.

💡 В общем, всё очень просто:  
у Вас есть <b>проблема</b>, а у меня есть <b>решение</b>.
  
Если у меня нет решения, то порекомендую обратиться к другому специалисту, потому что <b>ценю Ваше время!</b>
""", parse_mode='html', reply_markup=kb.consultation_inline_keyboard)