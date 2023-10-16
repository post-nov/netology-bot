from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.constants import ParseMode
from telegram.ext import (
    CallbackQueryHandler,
    ContextTypes,
)

from constants import *
from utils import asleep

from blocks.intro import block2_intro, block3_intro, block4_intro, block5_intro
from blocks.block_finish import block1_final


async def block5_intro_1(update: Update, context: ContextTypes.DEFAULT_TYPE) -> str:
    query = update.callback_query
    await query.answer()

    if query.data == ANSWER_1:
        text = '\n'.join([
            'Ошибаться нормально для любого человека. Покажите это студентам на своём примере. Если они заметили '
            'ошибку, поблагодарите их и предложите её разобрать. Обсудите последствия ошибки: насколько они были '
            'критичны, как повлияли на результат. Студентам это поможет развивать критическое мышление и логику.',
        ])
    elif query.data == ANSWER_2:
        text = '\n'.join([
            'Обычно я использую этот подход. Ошибаться нормально для любого человека. Покажите это студентам на своём '
            'примере. Если они заметили ошибку, поблагодарите их и предложите её разобрать. Обсудите последствия '
            'ошибки: насколько они были критичны, как повлияли на результат. Студентам это поможет развивать '
            'критическое мышление и логику.',
        ])
    else:
        text = '\n'.join([
            'Конечно, вы можете сообщить причину, по которой совершили ошибку, не вдаваясь в подробности. Ошибаться '
            'нормально для любого человека. Покажите это студентам на своём примере. Если они заметили ошибку, '
            'поблагодарите их и предложите её разобрать. Обсудите последствия ошибки: насколько они были критичны, '
            'как повлияли на результат. Студентам это поможет развивать критическое мышление и логику.',
        ])

    buttons = [[
        InlineKeyboardButton(text='А если не сразу пойму, в чем ошибка?', callback_data=DUMMY),
    ]]
    keyboard = InlineKeyboardMarkup(buttons)

    await update.callback_query.message.reply_text(text, reply_markup=keyboard)

    return BLOCK5_INTRO_2


async def block5_intro_2(update: Update, context: ContextTypes.DEFAULT_TYPE) -> str:
    query = update.callback_query
    await query.answer()

    text = '\n'.join([
        'Такое со мной тоже случалось.',
        '',
        'Как бы вы поступили в такой ситуации? ',
        '',
        '1. Спросить у студентов, что они думают по этому поводу. ',
        '2. Сказать, что задание, скорее всего, составлено неверно. ',
        '3. Сказать, что нужно больше времени для того, чтобы разобраться в вопросе, и вернуться с ответом позже.',
    ])

    buttons = [[
        InlineKeyboardButton(text='1', callback_data=ANSWER_1),
        InlineKeyboardButton(text='2', callback_data=ANSWER_2),
        InlineKeyboardButton(text='3', callback_data=ANSWER_3),
    ]]
    keyboard = InlineKeyboardMarkup(buttons)

    await update.callback_query.message.reply_text(text, reply_markup=keyboard)

    return BLOCK5_INTRO_3


async def block5_intro_3(update: Update, context: ContextTypes.DEFAULT_TYPE) -> str:
    query = update.callback_query
    await query.answer()

    if query.data == ANSWER_1:
        text = '\n'.join([
            'Отличная идея. Можно предложить студентам вместе поразмышлять над ситуацией и попробовать найти ответ. '
            'Например, провести мини-исследование или обсуждение. Если всё-таки решение найти не удаётся, '
            'возьмите время на то, чтобы глубже разобраться в вопросе. Скажите студентам, когда сможете вернуться с '
            'ответом. Нет ничего страшного в том, чтобы посоветоваться с коллегами или погуглить. Также можно '
            'поступить, если вы не знаете точного ответа на вопрос студента.',
        ])
    elif query.data == ANSWER_2:
        text = '\n'.join([
            'Если вы сомневаетесь в правильности задания, не стоит делать поспешных выводов. Возможно, '
            'оно действительно составлено неверно, но может быть, что всё в порядке, просто вы раньше не сталкивались '
            'с подобным типом задач. Возьмите время на то, чтобы глубже разобраться в вопросе, и скажите студентам, '
            'когда сможете вернуться с ответом. Нет ничего страшного в том, чтобы посоветоваться с коллегами или '
            'погуглить. Также можно поступить, если вы не знаете точного ответа на вопрос студента.',
        ])
    else:
        text = '\n'.join([
            'Я бы тоже взял время на то, чтобы глубже разобраться в вопросе. Скажите студентам, когда сможете '
            'вернуться с ответом. Нет ничего страшного в том, чтобы посоветоваться с коллегами или погуглить. '
            'Предложить студентам вместе подумать над решением тоже кажется классной идеей. Можно провести совместное '
            'мини-исследование или обсуждение. Если ответ всё-таки не найдётся, вы уже знаете, что делать, '
            '— взять паузу и позже вернуться с ответом. Также можно поступить, если вы не знаете точного ответа на '
            'вопрос студента.',
        ])

    buttons = [[
        InlineKeyboardButton(text='Если я сомневаюсь в своих знаниях?', callback_data=DUMMY),
    ]]
    keyboard = InlineKeyboardMarkup(buttons)

    await update.callback_query.message.reply_text(text, reply_markup=keyboard)

    return BLOCK5_INTRO_4


async def block5_intro_4(update: Update, context: ContextTypes.DEFAULT_TYPE) -> str:
    query = update.callback_query
    await query.answer()

    text = '\n'.join([
        'Это мне тоже знакомо. В самом начале преподавания я оценивал свой опыт, '
        'насколько он релевантен программе, чтобы быть более уверенным в себе.',
    ])

    buttons = [[
        InlineKeyboardButton(text='Как это сделать?', callback_data=DUMMY),
    ]]
    keyboard = InlineKeyboardMarkup(buttons)

    await update.callback_query.message.reply_text(text, reply_markup=keyboard)

    return BLOCK5_INTRO_5


async def block5_intro_5(update: Update, context: ContextTypes.DEFAULT_TYPE) -> str:
    query = update.callback_query
    await query.answer()

    text = '\n'.join([
        'Есть несколько вариантов.',
        '   ',
        '<b>Первый</b>',
        'Если вы работаете в компании, которая занимается онлайн-обучением, '
        'наверняка у неё есть программа обучения студентов. Там вы можете посмотреть темы, которые студенты будут '
        'проходить, навыки, которыми студент будет обладать, окончив программу. Попробуйте соотнести свои знания '
        'и навыки с теми, которые есть в программе. Есть ли у вас достаточно знаний по этим темам? Сможете ли вы '
        'справиться с самыми сложными заданиями из программы? Также можете уточнить у команды курса или '
        'программы, есть ли у них чёткие требования к преподавателю и какие.',
    ])
    await context.bot.send_message(chat_id=update.callback_query.message.chat_id, text=text, parse_mode=ParseMode.HTML)
    await asleep(5)
    text = '\n'.join([
        '<b>Второй</b>',
        'Если есть возможность, '
        'поговорите с действующим или прошлым преподавателем на программе. Спросите о его опыте и знаниях, '
        'уточните, какие вопросы чаще всего задают студенты, с какими проблемами сталкиваются.',
        '   ',
        '<b>Третий</b>',
        'Попробуйте найти наставника или бадди, который поможет вам освоиться с преподаванием. Это можно сделать '
        'как внутри, так и вне компании. Наставник — более опытный профи, который может что-то подсказать и '
        'направить вас. Бадди — специалист примерно такого же уровня, как и вы. С ним можно обсудить возникающие '
        'трудности, вместе находить решения, делиться успехами и впечатлениями от процесса.',
    ])

    buttons = [[
        InlineKeyboardButton(text='А если я преподаю самостоятельно?', callback_data=DUMMY),
    ]]
    keyboard = InlineKeyboardMarkup(buttons)

    await update.callback_query.message.reply_text(text, reply_markup=keyboard, disable_web_page_preview=True,
                                                   parse_mode=ParseMode.HTML)

    return BLOCK5_INTRO_6


async def block5_intro_6(update: Update, context: ContextTypes.DEFAULT_TYPE) -> str:
    query = update.callback_query
    await query.answer()

    text = '\n'.join([
        'Тоже есть несколько путей. Например, можно попросить коллег из сферы оценить ваш профессиональный '
        'уровень.',
        '   ',
        'Можно самостоятельно оценить свои достижения. Сосредоточьтесь на фактах. Вспомните, '
        'какие обычно задачи вы решаете, к каким результатам это приводит, каким инструментарием вы владеете. '
        'Если у вас есть опыт выступлений, написания статей, ведения блога, не забудьте это учесть. Составьте '
        'подробный рассказ о себе как о профессионале и попробуйте его соотнести с вакансиями преподавателей в '
        'популярных онлайн-школах.',
    ])
    await context.bot.send_message(chat_id=update.callback_query.message.chat_id, text=text, parse_mode=ParseMode.HTML)
    await asleep(5)
    text = '\n'.join([
        'Можно найти программу вашего профиля на сайтах известных онлайн-школ и '
        'попробовать соотнести себя с указанными там темами и результатами обучения.',
        '   ',
        'Конечно, поиск бадди или '
        'наставника тоже может быть актуален.',
    ])

    buttons = [[
        InlineKeyboardButton(text='Если я волнуюсь перед занятием?', callback_data=DUMMY),
    ]]
    keyboard = InlineKeyboardMarkup(buttons)

    await update.callback_query.message.reply_text(text, reply_markup=keyboard, disable_web_page_preview=True,
                                                   parse_mode=ParseMode.HTML)

    return BLOCK5_INTRO_7


async def block5_intro_7(update: Update, context: ContextTypes.DEFAULT_TYPE) -> str:
    query = update.callback_query
    await query.answer()

    text = '\n'.join([
        'Понимаю, я тоже волнуюсь. Вот несколько техник, которые мне помогают с этим справляться.',
        '   ',
        '<b>Понять причину волнения</b> ',
        'Часто я переживаю из-за того, что скажу что-то не так или сделаю ошибку. Выше мы уже '
        'обсудили, как с этим можно справляться. Если вы переживаете из-за других причин, например большого '
        'количества людей — попробуйте подобрать для себя способ справиться именно с причиной волнения, '
        'а не его проявлениями.',
        '   ',
        '<b>Хорошо подготовиться</b> ',
        'Если вы хорошо владеете материалом, это уже больше '
        'половины успеха. Вам будет проще сориентироваться в любой ситуации.',
    ])
    await context.bot.send_message(chat_id=update.callback_query.message.chat_id, text=text, parse_mode=ParseMode.HTML)
    await asleep(5)
    text = '\n'.join([
        '<b>Тренироваться</b> ',
        'Если есть '
        'возможность, попробуйте рассказать материал меньшей аудитории — домашний питомец или компания друзей '
        'тоже подойдут.',
        '   ',
        '<b>Переключаться</b> ',
        'Выделите себе время перед занятием, чтобы настроиться, вспомнить основные '
        'тезисы и сделать все необходимые вам ритуалы. Мне хватает 10–15 минут, кому-то может понадобиться чуть '
        'больше времени. Если волнение всё ещё не унимается, воспользуйтесь дыхательными практиками или '
        'небольшими физическими упражнениями. Я, например, приседаю 10 раз и потом глубоко дышу. Это помогает '
        'отвлечься, снять мышечное напряжение и разгрузить голову.',
        '   ',
        'В любом случае мандраж после первых занятий '
        'проходит. Через какое-то время вы заметите, что преподавание становится рутиной и сильного стресса вы '
        'уже не испытываете. Постепенно ваши преподавательские навыки будут развиваться.',
    ])

    buttons = [[
        InlineKeyboardButton(text='Как развивать навыки преподавания?', callback_data=DUMMY),
    ]]
    keyboard = InlineKeyboardMarkup(buttons)

    await update.callback_query.message.reply_text(text, reply_markup=keyboard, disable_web_page_preview=True,
                                                   parse_mode=ParseMode.HTML)

    return BLOCK5_INTRO_8


async def block5_intro_8(update: Update, context: ContextTypes.DEFAULT_TYPE) -> str:
    query = update.callback_query
    await query.answer()

    text = '\n'.join([
        'Тоже есть несколько вариантов.',
        '   ',
        '1. Можно периодически сверяться с картой компетенций преподавателя. Она '
        'поможет понять, что получается здорово, что можно улучшить.',
        '   ',
        '2. Регулярно запрашивайте обратную связь '
        'от студентов и команды, с которой вы работаете над программой, если команда есть.',
        '   ',
        '3. Можно подписаться '
        'на каналы и блоги о преподавании и онлайн-образовании, активно участвовать в профессиональных '
        'сообществах и следить за трендами онлайн-образования. Мы сделали подборку, которую вы можете сохранить '
        'себе.',
        '   ',
        'https://t.me/edtrends',
        'https://t.me/ru_education',
        'https://t.me/ielearning',
        'https://t.me/schoolofeducation',
        'https://t.me/kaktomogu',
        'https://t.me/alliknowisthatidontknownothing',
        'https://t.me/myownconference',
        '   ',
        '4. Делитесь своим опытом: заведите блог, пишите статьи, выступайте на '
        'конференциях и форумах. Это помогает осмыслять свой опыт, структурировать знания и обращать внимание на '
        'опыт других людей.',
    ])

    buttons = [[
        InlineKeyboardButton(text='Не знаю, хватит ли времени', callback_data=DUMMY),
    ]]
    keyboard = InlineKeyboardMarkup(buttons)

    await update.callback_query.message.reply_text(text, reply_markup=keyboard, disable_web_page_preview=True,
                                                   parse_mode=ParseMode.HTML)

    return BLOCK5_INTRO_9


async def block5_intro_9(update: Update, context: ContextTypes.DEFAULT_TYPE) -> str:
    query = update.callback_query
    await query.answer()

    text = '\n'.join([
        'Начните с простого. Посмотрите на свой график и попробуйте определить, сколько часов в неделю вы готовы '
        'выделить на преподавание. Это фиксированное и регулярное время или возникающее стихийно?',
        '   ',
        'Спросите у '
        'коллег, сколько времени у них занимает преподавание. Не только проведение занятий, но и подготовка к '
        'ним. Если планируете работать в компании, уточните, что именно входит в функционал преподавателя. В чём '
        'и какие специалисты ему могут помочь. Какие дедлайны есть по задачам.',
        '   ',
        'Вся эта информация поможет вам '
        'понять, как можно встроить преподавание в свой график.',
    ])

    buttons = [[
        InlineKeyboardButton(text='Спасибо, попробую!', callback_data=DUMMY),
    ]]
    keyboard = InlineKeyboardMarkup(buttons)

    await update.callback_query.message.reply_text(text, reply_markup=keyboard, disable_web_page_preview=True,
                                                   parse_mode=ParseMode.HTML)

    return BLOCK5_FINISH_1


async def block5_finish_1(update: Update, context: ContextTypes.DEFAULT_TYPE) -> str:
    query = update.callback_query
    await query.answer()

    text = '\n'.join([
        'Отлично, можем двигаться дальше! Переходим к блоку преподаватель тоже человек? '
        'Или хотите посмотреть все разделы и выбрать подходящий?',
    ])

    buttons = [[
        InlineKeyboardButton(text='Буду заканчивать курс', callback_data=ANSWER_1)
    ], [
        InlineKeyboardButton(text='Хочу посмотреть все блоки и выбрать', callback_data=ANSWER_2),
    ]]
    keyboard = InlineKeyboardMarkup(buttons)

    await update.callback_query.message \
        .reply_text(text, reply_markup=keyboard)

    return BLOCK5_FINISH_2


async def block5_finish_2(update: Update, context: ContextTypes.DEFAULT_TYPE) -> str:
    query = update.callback_query
    await query.answer()

    text = '\n'.join([
        'Что выберем?',
    ])

    buttons = [[
        InlineKeyboardButton(text='Готовимся к занятию', callback_data=ANSWER_1),
    ], [
        InlineKeyboardButton(text='Проводим занятие', callback_data=ANSWER_2)
    ], [
        InlineKeyboardButton(text='А что по домашкам?', callback_data=ANSWER_3),
    ]]
    keyboard = InlineKeyboardMarkup(buttons)

    await update.callback_query.message.reply_text(text, reply_markup=keyboard)

    return BLOCK5_FINISH_3

block5_states = {

    BLOCK5_INTRO: [CallbackQueryHandler(block5_intro)],
    BLOCK5_INTRO_1: [CallbackQueryHandler(block5_intro_1)],
    BLOCK5_INTRO_2: [CallbackQueryHandler(block5_intro_2)],
    BLOCK5_INTRO_3: [CallbackQueryHandler(block5_intro_3)],
    BLOCK5_INTRO_4: [CallbackQueryHandler(block5_intro_4)],
    BLOCK5_INTRO_5: [CallbackQueryHandler(block5_intro_5)],
    BLOCK5_INTRO_6: [CallbackQueryHandler(block5_intro_6)],
    BLOCK5_INTRO_7: [CallbackQueryHandler(block5_intro_7)],
    BLOCK5_INTRO_8: [CallbackQueryHandler(block5_intro_8)],
    BLOCK5_INTRO_9: [CallbackQueryHandler(block5_intro_9)],

    BLOCK5_FINISH_1: [CallbackQueryHandler(block5_finish_1)],
    BLOCK5_FINISH_2: [
        CallbackQueryHandler(block1_final, pattern=ANSWER_1),
        CallbackQueryHandler(block5_finish_2, pattern=ANSWER_2),
    ],
    BLOCK5_FINISH_3: [
        CallbackQueryHandler(block2_intro, pattern=ANSWER_1),
        CallbackQueryHandler(block3_intro, pattern=ANSWER_2),
        CallbackQueryHandler(block4_intro, pattern=ANSWER_3),
    ],
}