from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    Application,
    CommandHandler,
    ContextTypes,
    ConversationHandler,
    CallbackQueryHandler,
    MessageHandler,
    filters,
)

from constants import *

from blocks.intro import intro_query_handlers, block1_intro
from blocks.block1 import block1_states
from blocks.block2 import block2_states
from blocks.block3 import block3_states
from blocks.block4 import block4_states
from blocks.block5 import block5_states
from blocks.block_finish import block_finish_states

from utils import asleep, process_user_data


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> str:
    return await block1_intro(update, context)


async def jump(update: Update, context: ContextTypes.DEFAULT_TYPE) -> str:
    query = update.callback_query
    if query:
        await query.answer()

    if context.user_data.get(USER_DATA_IN_SUPPORT):
        context.user_data[USER_DATA_SUPPORT_MESSAGE] = update.message.text
        await process_user_data(update.effective_user.id, context.user_data)
        await context.bot.send_message(chat_id=update.effective_chat.id, text='Спасибо за вашу обратную связь!')
        context.user_data[USER_DATA_IN_SUPPORT] = False
        await asleep(2)

    block_map = {
        'Начать курс сначала': BLOCK1_INTRO,
        'Готовимся к занятию': BLOCK2_INTRO,
        'Проводим занятие': BLOCK3_INTRO,
        'А что по домашкам?': BLOCK4_INTRO,
        'Преподаватель тоже человек!': BLOCK5_INTRO,
    }

    debug_block_map = {
        'BLOCK1_STUDENT_17': BLOCK1_STUDENT_17,
    }

    buttons = []
    for text, callback_data in block_map.items():
        buttons.append([InlineKeyboardButton(text=text, callback_data=callback_data)])
    if DEBUG:
        for text, callback_data in debug_block_map.items():
            buttons.append([InlineKeyboardButton(text=text, callback_data=callback_data)])
    keyboard = InlineKeyboardMarkup(buttons)

    text = '\n'.join([
        'К какому этапу обучения вы хотели бы перейти?'
    ])

    if query:
        await update.callback_query.message.reply_text(text=text, reply_markup=keyboard)
    else:
        await update.message.reply_text(text=text, reply_markup=keyboard)

    return BLOCK_JUMP


async def help(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    if query:
        await query.answer()

    text = '\n'.join([
        'Бот поддерживает следующие команды:',
        '',
        '/start - Запустить бота/начать курс заново',
        '/help - Вывести это сообщение',
        '/jump - Перейти к определенному этапу обучения',
        '/support - Оставить обращение в службу поддержки',
        '/cancel - Остановить бота',
    ])

    await context.bot.send_message(chat_id=update.effective_chat.id, text=text)


async def support(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    query = update.callback_query
    if query:
        await query.answer()

    text = '\n'.join([
        'Напишите, пожалуйста, ваши замечания и предложения'
    ])
    context.user_data[USER_DATA_IN_SUPPORT] = True

    if query:
        await update.callback_query.message.reply_text(text)
    else:
        await update.message.reply_text(text)

    return BLOCK_SUPPORT


async def cancel(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    query = update.callback_query
    if query:
        await query.answer()

    text = '\n'.join([
        'До встречи и классных студентов!'
    ])

    await context.bot.send_message(chat_id=update.effective_chat.id, text=text)

    return ConversationHandler.END


def main() -> None:
    application = Application.builder().token(TOKEN).concurrent_updates(True).build()

    conv_handler = ConversationHandler(
        entry_points=[
            CommandHandler('start', start),
            CommandHandler('jump', jump),
        ],
        states={
            **block1_states,
            **block2_states,
            **block3_states,
            **block4_states,
            **block5_states,
            **block_finish_states,

            BLOCK_JUMP: intro_query_handlers,

            BLOCK_SUPPORT: [
                MessageHandler(filters.TEXT & ~filters.COMMAND, jump),
            ]
        },
        fallbacks=[
            CommandHandler('start', start),
            CommandHandler('cancel', cancel),
            CommandHandler('help', help),
            CommandHandler('support', support),
            CommandHandler('jump', jump)
        ],
        name="my_conversation",
    )
    application.add_handler(conv_handler)

    application.add_handler(CommandHandler('support', support))
    application.add_handler(CommandHandler('help', help))

    application.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    main()
