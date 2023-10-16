from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.constants import ParseMode
from telegram.ext import ContextTypes, CallbackQueryHandler

from constants import *
from utils import asleep


async def block1_intro(update: Update, context: ContextTypes.DEFAULT_TYPE) -> str:
    """Select an action: Adding parent/child or show data."""
    query = update.callback_query
    if query:
        await query.answer()

    text = '\n'.join([
        "Привет! 👋🏼",
        "Рад видеть вас на курсе!",
        '',
        "Меня зовут Саша, я — преподаватель Нетологии. "
        "Предлагаю вместе со мной познакомиться с особенностями онлайн-преподавания.",
        "",
        "А как вас зовут? Напишите имя, пожалуйста.",
    ])

    if query:
        await update.callback_query.message.reply_text(text=text)
    else:
        await update.message.reply_text(text=text)

    return BLOCK1_INTRODUCTION_SURNAME


async def block2_intro(update: Update, context: ContextTypes.DEFAULT_TYPE) -> str:
    query = update.callback_query
    await query.answer()

    await context.bot.copy_message(chat_id=update.effective_chat.id, from_chat_id=MEDIA_CHANNEL_ID,
                                   message_id=MEDIA_PHOTO_5)
    text = '\n'.join([
        'За каждым вебинаром, прямым эфиром и домашкой от эксперта стоит огромный этап подготовки. То, что видят '
        'студенты, — это лишь верхушка айсберга'
    ])

    buttons = [[
        InlineKeyboardButton(text='Звучит серьезно', callback_data=DUMMY),
    ]]
    keyboard = InlineKeyboardMarkup(buttons)

    await update.callback_query.message.reply_text(text, reply_markup=keyboard)

    return BLOCK2_INTRO_1


async def block3_intro(update: Update, context: ContextTypes.DEFAULT_TYPE) -> str:
    query = update.callback_query
    if query:
        await query.answer()

    text = '\n'.join([
        'Вы уже знаете, что обучение в онлайне отличается от офлайна. Мой друг и '
        'преподаватель Нетологии Евгений Корытов подробнее расскажет, в чём особенность вебинаров '
        'и как к ним подготовиться.',
    ])
    await context.bot.send_message(chat_id=update.effective_chat.id, text=text, disable_web_page_preview=True,
                                   parse_mode=ParseMode.HTML)

    await asleep(3)

    await context.bot.copy_message(chat_id=update.effective_chat.id, from_chat_id=MEDIA_CHANNEL_ID,
                                   message_id=MEDIA_BLOCK3_VIDEO_1)

    await asleep(10)

    text = '\n'.join([
        'Для занятия важно подобрать хорошее место. Вот несколько критериев. ',
        '1. Яркое освещение, но без источника света за спиной: иначе вас будет плохо видно. ',
        '2. Нейтральный фон спокойного цвета, без обилия мелких деталей. ',
        '3. Во время всего занятия в помещении должна быть тишина.',
    ])

    buttons = [[
        InlineKeyboardButton(text='Кажется, рано начинать занятие...', callback_data=DUMMY),
    ]]
    keyboard = InlineKeyboardMarkup(buttons)

    if query:
        await update.callback_query.message.reply_text(text, reply_markup=keyboard, disable_web_page_preview=True,
                                                       parse_mode=ParseMode.HTML)
    else:
        await update.message.reply_text(text, reply_markup=keyboard, disable_web_page_preview=True,
                                        parse_mode=ParseMode.HTML)

    return BLOCK3_INTRO_1


async def block4_intro(update: Update, context: ContextTypes.DEFAULT_TYPE) -> str:
    query = update.callback_query
    await query.answer()

    text = '\n'.join([
        'После занятия чаще всего студенты выполняют домашнее задание. Сейчас предлагаю поговорить о том, '
        'как его проверить.',
        '    ',
        'Преподавателю важно дать студенту развивающую обратную связь, после которой захочется '
        'продолжить обучение, а не забросить учёбу надолго :)',
    ])
    buttons = [[
        InlineKeyboardButton(text='Развивающая обратная связь?', callback_data=DUMMY),
    ]]
    keyboard = InlineKeyboardMarkup(buttons)

    await update.callback_query.message.reply_text(text, reply_markup=keyboard, disable_web_page_preview=True,
                                                   parse_mode=ParseMode.HTML)

    return BLOCK4_INTRO_1


async def block5_intro(update: Update, context: ContextTypes.DEFAULT_TYPE) -> str:
    query = update.callback_query
    if query:
        await query.answer()

    text = '\n'.join([
        'Большинство преподавателей в начале работы сталкиваются с разными страхами и сомнениями. Например, '
        'не ответить на вопрос студента, допустить ошибку при объяснении нового материала и т. д.',
        '   ',
        'Мне кажется '
        'важным поговорить о том, что преподаватели тоже люди. Они могут ошибаться, сомневаться и чего-то не знать.',
        '  ',
        'Начнём с самого распространенного: <b>«А что, если я ошибусь?»</b> Например, '
        'неправильно отвечу на вопрос или скажу '
        'что-то не то, когда буду объяснять новый материал.',
        '   ',
        'Предлагаю подумать вместе, что в такой ситуации лучше сделать. ',
        '',
        '1. Сделать вид, что ничего не произошло.',
        '2. Признать ошибку и разобрать её. ',
        '3. Сообщить причину, '
        'по которой вы ошиблись: усталость, проблемы в семье и т. д.',
    ])

    buttons = [[
        InlineKeyboardButton(text='1', callback_data=ANSWER_1),
        InlineKeyboardButton(text='2', callback_data=ANSWER_2),
        InlineKeyboardButton(text='3', callback_data=ANSWER_3),
    ]]
    keyboard = InlineKeyboardMarkup(buttons)

    if query:
        await update.callback_query.message.reply_text(text, reply_markup=keyboard, parse_mode=ParseMode.HTML)
    else:
        await update.message.reply_text(text, reply_markup=keyboard, parse_mode=ParseMode.HTML)

    return BLOCK5_INTRO_1


intro_query_handlers = [
    CallbackQueryHandler(block1_intro, pattern=BLOCK1_INTRO),
    CallbackQueryHandler(block2_intro, pattern=BLOCK2_INTRO),
    CallbackQueryHandler(block3_intro, pattern=BLOCK3_INTRO),
    CallbackQueryHandler(block4_intro, pattern=BLOCK4_INTRO),
    CallbackQueryHandler(block5_intro, pattern=BLOCK5_INTRO),
]
