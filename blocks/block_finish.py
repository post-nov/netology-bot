from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.constants import ParseMode
from telegram.ext import (
    CallbackQueryHandler,
    ContextTypes,
    MessageHandler,
    ConversationHandler,
    filters,
)

from constants import *
from utils import process_user_data


async def block1_finish_1(update: Update, context: ContextTypes.DEFAULT_TYPE) -> str:
    query = update.callback_query
    await query.answer()

    text = '\n'.join([
        'Что выберем?',
    ])

    buttons = [[
        InlineKeyboardButton(text='Готовимся к занятию', callback_data=ANSWER_1),
        InlineKeyboardButton(text='Проводим занятие', callback_data=ANSWER_2),
    ], [
        InlineKeyboardButton(text='А что по домашкам?', callback_data=ANSWER_3),
        InlineKeyboardButton(text='Преподаватель тоже человек!', callback_data=ANSWER_4),
    ]]
    keyboard = InlineKeyboardMarkup(buttons)

    await update.callback_query.message.reply_text(text, reply_markup=keyboard)

    return BLOCK1_FINISH_2


async def block1_final(update: Update, context: ContextTypes.DEFAULT_TYPE) -> str:
    query = update.callback_query
    await query.answer()

    text = """Спасибо, что вместе со мной разбирались, как устроено онлайн-образование. Надеюсь, это было полезно! Если вы захотите стать преподавателем в Нетологии, то оставьте заявку по ссылке.

Буду рад, если вы оставите обратную связь о курсе. Она помогает мне лучше рассказывать о преподавании в онлайне. Вы готовы ответить на несколько вопросов?"""

    buttons = [
        [InlineKeyboardButton(text='Да, я отвечу на три вопроса', callback_data=ANSWER_1)],
        [InlineKeyboardButton(text='Спасибо, пожалуй, я все!', callback_data=ANSWER_2)],
    ]
    keyboard = InlineKeyboardMarkup(buttons)

    await update.callback_query.message.reply_text(text, reply_markup=keyboard,
                                                   disable_web_page_preview=True,
                                                   parse_mode=ParseMode.HTML)

    return BLOCK1_FINAL_2


async def block1_final_2(update: Update, context: ContextTypes.DEFAULT_TYPE) -> [str, int]:
    query = update.callback_query
    await query.answer()

    if query.data == ANSWER_2:
        text = 'До встречи и классных студентов!'
        await context.bot.send_message(chat_id=update.effective_chat.id, text=text)
        await process_user_data(context.user_data)
        return ConversationHandler.END

    text = '\n'.join([
        'Оцените от 1 до 10 насколько полезным был для вас этот курс, где 1 – совсем не полезно, 10 – очень полезно.',
    ])

    buttons = [[
        InlineKeyboardButton(text=f'{i}', callback_data=f'{i}') for i in range(1, 6)
    ], [
        InlineKeyboardButton(text=f'{i}', callback_data=f'{i}') for i in range(5, 10)
    ], [
        InlineKeyboardButton(text='10', callback_data='10')
    ]]
    keyboard = InlineKeyboardMarkup(buttons)

    await update.callback_query.message.reply_text(text, reply_markup=keyboard, disable_web_page_preview=True,
                                                   parse_mode=ParseMode.HTML)

    return BLOCK1_FINAL_3


async def block1_final_3(update: Update, context: ContextTypes.DEFAULT_TYPE) -> [str, int]:
    query = update.callback_query
    await query.answer()

    context.user_data[USER_DATA_REVIEW_RATING] = query.data

    text = '\n'.join([
        'Спасибо! Было ли что-то, чего вам не хватило в курсе?',
    ])

    buttons = [[
        InlineKeyboardButton(text='Да', callback_data=ANSWER_1),
        InlineKeyboardButton(text='Нет', callback_data=ANSWER_2),
    ]]
    keyboard = InlineKeyboardMarkup(buttons)

    await update.callback_query.message.reply_text(text, reply_markup=keyboard)

    return BLOCK1_FINAL_4


async def block1_final_4(update: Update, context: ContextTypes.DEFAULT_TYPE) -> [str, int]:
    query = update.callback_query
    await query.answer()

    text = 'Поделитесь, пожалуйста, что это?'
    await update.callback_query.edit_message_text(text=text)

    return BLOCK1_FINAL_5


async def block1_final_4_4(update: Update, context: ContextTypes.DEFAULT_TYPE) -> [str, int]:
    context.user_data[USER_DATA_REVIEW_TEXT] = update.message.text

    return await block1_final_5(update, context)


async def block1_final_5(update: Update, context: ContextTypes.DEFAULT_TYPE) -> [str, int]:
    query = update.callback_query
    if query:
        await query.answer()

    text = '\n'.join([
        'Понял! Последний вопрос. Оцените от 1 до 10 с какой вероятностью вы поделитесь этим курсом с коллегой или '
        'порекомендуете его начинающему преподавателю? 1 – не порекомендую, 10 – точно порекомендую.',
    ])

    buttons = [[
        InlineKeyboardButton(text=f'{i}', callback_data=f'{i}') for i in range(1, 6)
    ], [
        InlineKeyboardButton(text=f'{i}', callback_data=f'{i}') for i in range(5, 10)
    ], [
        InlineKeyboardButton(text='10', callback_data='10')
    ]]
    keyboard = InlineKeyboardMarkup(buttons)

    if query:
        await update.callback_query.message.reply_text(text, reply_markup=keyboard)
    else:
        await update.message.reply_text(text, reply_markup=keyboard)

    return BLOCK1_FINAL_7


async def block1_final_6(update: Update, context: ContextTypes.DEFAULT_TYPE) -> [str, int]:
    query = update.callback_query
    await query.answer()

    context.user_data[USER_DATA_RECOMMENDATION_CHANCE] = query.data.strip('ANSWER_')

    text = '\n'.join([
        'Спасибо за обратную связь!',
        'До встречи и классных студентов!'
    ])
    await context.bot.send_message(chat_id=update.effective_chat.id, text=text)

    await process_user_data(update.effective_user.id, context.user_data)

    return ConversationHandler.END


block_finish_states = {
    BLOCK1_FINAL_1: [CallbackQueryHandler(block1_final)],
    BLOCK1_FINAL_2: [CallbackQueryHandler(block1_final_2)],
    BLOCK1_FINAL_3: [CallbackQueryHandler(block1_final_3)],
    BLOCK1_FINAL_4: [
        CallbackQueryHandler(block1_final_4, pattern=ANSWER_1),
        CallbackQueryHandler(block1_final_5, pattern=ANSWER_2),
    ],
    BLOCK1_FINAL_5: [MessageHandler(filters.TEXT & ~filters.COMMAND, block1_final_4_4)],
    BLOCK1_FINAL_6: [CallbackQueryHandler(block1_final_5)],
    BLOCK1_FINAL_7: [CallbackQueryHandler(block1_final_6)],
}
