from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.constants import ParseMode
from telegram.ext import (
    CallbackQueryHandler,
    ContextTypes,
    MessageHandler,
    filters,
)

from constants import *
from utils import asleep

from blocks.intro import block1_intro, block2_intro, block3_intro, block4_intro, block5_intro
from blocks.block_finish import block1_final, block1_finish_1


async def block1_introduction_surname(update: Update, context: ContextTypes.DEFAULT_TYPE) -> str:
    """Select an action: Adding parent/child or show data."""

    context.user_data[USER_DATA_NAME] = update.message.text
    text = '\n'.join([
        f'{context.user_data[USER_DATA_NAME]}, приятно познакомиться!',
        'Прежде чем мы начнём, у меня есть ещё три вопроса. '
        'Они помогут нам лучше понимать аудиторию курса и совершенствовать его.',
        '',
        'Введите свою фамилию.'
    ])

    await update.message.reply_text(text)

    return BLOCK1_INTRODUCTION_EMAIL


async def block1_introduction_email(update: Update, context: ContextTypes.DEFAULT_TYPE) -> str:
    """Select an action: Adding parent/child or show data."""

    context.user_data[USER_DATA_SURNAME] = update.message.text

    text = '\n'.join([
        'Укажите ваш email.',
        'Мы не будем отправлять вам рассылки, электронная почта нужна только для связи с вами.'
    ])
    await update.message.reply_text(text)

    return BLOCK1_INTRODUCTION_SPECIALITY


async def block1_introduction_speciality(update: Update, context: ContextTypes.DEFAULT_TYPE) -> str:
    """Select an action: Adding parent/child or show data."""

    context.user_data[USER_DATA_EMAIL] = update.message.text

    text = '\n'.join([
        'В каком направлении у вас есть экспертиза?'
    ])
    await update.message.reply_text(text)

    return BLOCK1_INTRODUCTION_LEVEL


async def block1_introduction_level(update: Update, context: ContextTypes.DEFAULT_TYPE) -> str:
    """Select an action: Adding parent/child or show data."""

    context.user_data[USER_DATA_SPECIALITY] = update.message.text

    text = '\n'.join([
        'Как бы вы оценили свой уровень?',
        '',
        '<b>Джун</b> — начинающий специалист. Вам требуется поддержка более опытного наставника.',
        '<b>Mидл</b> — опытный профи, не менее 2–3 лет в сфере. Можете самостоятельно решить все рабочие задачи.',
        '<b>Синьор</b> — больше 3 лет в сфере. Решите любую сложную и нестандартную задачу.',
    ])
    buttons = [
        [
            InlineKeyboardButton(text=JUNIOR, callback_data='JUNIOR'),
            InlineKeyboardButton(text=MIDDLE, callback_data='MIDDLE'),
            InlineKeyboardButton(text=SENIOR, callback_data='SENIOR'),
        ],
    ]
    keyboard = InlineKeyboardMarkup(buttons)
    await update.message.reply_text(text, reply_markup=keyboard, parse_mode=ParseMode.HTML)

    return BLOCK1_INTRODUCTION_EXPECTATIONS


async def block1_introduction_expectations(update: Update, context: ContextTypes.DEFAULT_TYPE) -> str:
    """Select an action: Adding parent/child or show data."""

    query = update.callback_query
    await query.answer()
    context.user_data[USER_DATA_EXPERIENCE] = query.data

    text = '\n'.join([
        'Последний вопрос: что вы ожидаете получить от прохождения курса?',
        'Напишите, пожалуйста, одним сообщением.',
    ])
    await context.bot.send_message(chat_id=update.effective_chat.id, text=text)

    return BLOCK1_INTRODUCTION_SUMMARY_1


async def block1_introduction_summary_1(update: Update, context: ContextTypes.DEFAULT_TYPE) -> str:
    context.user_data[USER_DATA_EXPECTATIONS] = update.message.text

    text = '\n'.join([
        'Спасибо, теперь у меня есть вся информация.',
        '',
        'Расскажу вам про обучение подробнее. На курсе вы узнаете:',
        '📌в чём особенность преподавания в онлайне и обучения взрослых;',
        '📌из каких этапов состоит работа преподавателя;',
        '📌что нужно делать на каждом из этапов.',
        '',
        'Я буду делиться своим опытом, но считаю важным донести не только свои мысли. '
        'Поэтому буду обращаться к экспертизе моих друзей-образованцев. '
        'Такой разносторонний взгляд на процесс обучения кажется мне очень важным.',
    ])

    button_text = 'За какое время я пройду курс?'
    keyboard = InlineKeyboardMarkup([[InlineKeyboardButton(text=button_text, callback_data=DUMMY)]])

    await update.message.reply_text(text, reply_markup=keyboard)

    return BLOCK1_INTRODUCTION_SUMMARY_2


async def block1_introduction_summary_2(update: Update, context: ContextTypes.DEFAULT_TYPE) -> str:
    query = update.callback_query
    await query.answer()
    text = '\n'.join([
        'Прохождение всего курса займёт около 2–3 часов.',
        'Вы можете пройти его за один вечер, а можете проходить постепенно в своём темпе.',
        '',
        'Вы готовы?',
    ])

    button_text = 'Вперед!'
    keyboard = InlineKeyboardMarkup([[InlineKeyboardButton(text=button_text, callback_data=DUMMY)]])

    await update.callback_query.message.reply_text(text=text, reply_markup=keyboard)

    return BLOCK1_INTRODUCTION_SUMMARY_3


async def block1_introduction_summary_3(update: Update, context: ContextTypes.DEFAULT_TYPE) -> str:
    query = update.callback_query
    await query.answer()

    text = '\n'.join([
        'Отлично. Поговорим о том, кто такой преподаватель в онлайне. '
        'Кто может стать преподавателем? Что для этого нужно знать и уметь?',
        '',
        'Мой друг и эксперт Нетологии Евгений Корытов классно рассказывает об этом.',
    ])
    await update.callback_query.message.reply_text(text=text)

    await asleep(4)

    await context.bot.copy_message(chat_id=update.effective_chat.id, from_chat_id=MEDIA_CHANNEL_ID,
                                   message_id=MEDIA_BLOCK1_VIDEO_1)
    await asleep(7)

    text = '\n'.join([
        'Что именно делает преподаватель, зависит от контекста. '
        'Например, от компании в которой вы работаете. '
        'В некоторых преподаватель — многорукий Шива: разрабатывает программу, '
        'пишет материал для занятий, проводит их, проверяет домашки и принимает итоговые работы студентов.',
    ])

    button_text = 'А что, бывает по-другому?'
    keyboard = InlineKeyboardMarkup([[InlineKeyboardButton(text=button_text, callback_data=DUMMY)]])

    await update.callback_query.message.reply_text(text, reply_markup=keyboard)

    return BLOCK1_INTRODUCTION_SUMMARY_4


async def block1_introduction_summary_4(update: Update, context: ContextTypes.DEFAULT_TYPE) -> str:
    query = update.callback_query
    await query.answer()

    text = """Да, всё возможно :)

В Нетологии и многих других компаниях преподаватели выбирают одну узкую роль или специализацию. Например, только проверяют работы студентов или ведут лекции.

Могу рассказать вам подробнее про роли преподавателей в Нетологии. Это займет пару минут и поможет вам лучше ориентироваться в том, что обычно делает преподаватель.

Можем пропустить и перейти к разговору о том, как учатся взрослые."""

    buttons = [[
        InlineKeyboardButton(text='Хочу узнать роли', callback_data=ANSWER_1),
    ], [
        InlineKeyboardButton(text='Пропустим', callback_data=ANSWER_2),
    ]]
    keyboard = InlineKeyboardMarkup(buttons)

    await update.callback_query.message.reply_text(text, reply_markup=keyboard)

    return BLOCK1_INTRODUCTION_ROLES_1


async def block1_introduction_roles_1(update: Update, context: ContextTypes.DEFAULT_TYPE) -> str:
    query = update.callback_query
    await query.answer()

    await context.bot.copy_message(chat_id=update.effective_chat.id, from_chat_id=MEDIA_CHANNEL_ID,
                                   message_id=MEDIA_PHOTO_1)

    text = '\n'.join([
        '<b>Методист или автор</b> создаёт контент программы и занятий: '
        'продумывает, что и в какой последовательности мы будем рассказывать '
        'студенту, какие подберём примеры и практические задания.',
        '',
        '<b>Лектор</b> проводит онлайн-занятия в режиме реального '
        'времени — вебинары. Ещё лектор может принимать участие '
        'в записи видеолекций, которые студенты смотрят в любое '
        'удобное для них время.',
        '',
        '<b>Тренер</b> проверяет домашние работы студентов и даёт '
        'подробную обратную связь в письменном виде.',
        '',
        '<b>Дипломный руководитель</b> проверяет итоговые работы '
        'студентов — дипломные проекты. Также он может '
        'консультировать студентов в процессе подготовки диплома.',
    ])

    buttons = [[
        InlineKeyboardButton(text='Кто работает с преподавателем?', callback_data='d'),
    ]]
    keyboard = InlineKeyboardMarkup(buttons)

    await update.callback_query.message.reply_text(text, reply_markup=keyboard,
                                                   parse_mode=ParseMode.HTML)

    return BLOCK1_INTRODUCTION_ROLES_2


async def block1_introduction_roles_2(update: Update, context: ContextTypes.DEFAULT_TYPE) -> str:
    query = update.callback_query
    await query.answer()

    text = '\n'.join([
        'Эксперты в Нетологии, как и во многих других образовательных компаниях, '
        'не работают в одиночку. Расскажу вам о команде, '
        'с которой эксперт чаще всего взаимодействует.',
    ])
    await update.callback_query.message.reply_text(text=text)

    await asleep(3)

    await context.bot.copy_message(chat_id=update.effective_chat.id, from_chat_id=MEDIA_CHANNEL_ID,
                                   message_id=MEDIA_PHOTO_2)

    text = '\n'.join([
        '<b>Методист</b> знает, как учатся люди. '
        'Может сказать, где студенты устанут или отвлекутся, '
        'как можно этого избежать и сделать процесс обучения эффективным и комфортным. '
        'Поможет структурировать контент, интересно его подать, придумать практику к теории.',
        '',
        '<b>Продюсер</b> отвечает головой за качество продукта и его соответствие '
        'запросам рынка и работодателей. Контролирует все сроки, ставит '
        'задачи команде, следит за качеством исполнения, внимательно относится к метрикам продукта.',
    ])

    await context.bot.send_message(chat_id=update.effective_chat.id, text=text, parse_mode=ParseMode.HTML)

    await asleep(5)

    text = '\n'.join([
        '<b>Модератор</b> помогает эксперту в проведении занятия – '
        'запускает начало занятия на платформе, помогает общаться со студентами.',
        '',
        '<b>Менеджер по работе с экспертами</b> поможет новому эксперту '
        'влиться в команду, погрузит во все процессы компании, объяснит, '
        'к кому можно обратиться за советом или помощью. Ответит на все '
        'вопросы или направит к нужным коллегам. Готов помочь разобраться в любой ситуации.',
        '',
        'Но что мы все о себе? Самое время подумать о студентах! '
        'Как думаете, отличается ли обучение в онлайне от офлайна?'
    ])
    buttons = [[
        InlineKeyboardButton(text='Да', callback_data=ANSWER_1),
        InlineKeyboardButton(text='Немного', callback_data=ANSWER_2),
        InlineKeyboardButton(text='Нет', callback_data=ANSWER_2),
    ]]
    keyboard = InlineKeyboardMarkup(buttons)

    await update.callback_query.message.reply_text(text, reply_markup=keyboard, disable_web_page_preview=True,
                                                   parse_mode=ParseMode.HTML)

    return BLOCK1_QUIZ_2


async def block1_quiz_1(update: Update, context: ContextTypes.DEFAULT_TYPE) -> str:
    query = update.callback_query
    await query.answer()

    text = '\n'.join([
        'Согласен, что мы все о себе? Самое время подумать о студентах! Как думаете, отличается ли обучение в '
        'онлайне от офлайна?'
    ])
    buttons = [[
        InlineKeyboardButton(text='Да', callback_data=ANSWER_1),
        InlineKeyboardButton(text='Немного', callback_data=ANSWER_2),
        InlineKeyboardButton(text='Нет', callback_data=ANSWER_2),
    ]]
    keyboard = InlineKeyboardMarkup(buttons)

    await update.callback_query.message.reply_text(text, reply_markup=keyboard)

    return BLOCK1_QUIZ_2


async def block1_quiz_2(update: Update, context: ContextTypes.DEFAULT_TYPE) -> str:
    query = update.callback_query
    await query.answer()

    if query.data == ANSWER_1:
        text = 'Да, вы правы. Разберёмся, в чём же отличия. ' \
               'Когда учишься в онлайне, легче отвлекаться. ' \
               'Представьте, вы включаете видеолекцию и решаете ' \
               'налить стакан воды, потом замечаете пыль на столе, ' \
               'потом приходит пуш из рабочего чата... И вот уже 10 ' \
               'минут лекции прошло, а вы обнаруживаете себя за сканвордом ' \
               'или переливанием жидкостей в колбочках на телефоне. При этом ' \
               'преподаватель может не видеть студента, поэтому вернуть его внимание сложнее.'
    else:
        text = 'Существенные отличия всё же есть, давайте вместе ' \
               'в них разберёмся. Когда учишься в онлайне, легче ' \
               'отвлекаться. Представьте, вы включаете видеолекцию и ' \
               'решаете налить стакан воды, потом замечаете пыль на столе, ' \
               'потом приходит пуш из рабочего чата... И вот уже 10 минут ' \
               'лекции прошло, а вы обнаруживаете себя за сканвордом или ' \
               'переливанием жидкостей в колбочках на телефоне. При этом ' \
               'преподаватель может не видеть студента, поэтому вернуть его внимание сложнее.'

    await update.callback_query.message.reply_text(text=text)

    await asleep(10)

    text = '\n'.join([
        'В онлайн-обучении студент чувствует себя дистанцированно, '
        'оторвано от группы. Ему сложнее активно включаться: задавать '
        'вопросы, разбираться в новых понятиях. Это сильно влияет на '
        'мотивацию, она падает, и человеку сложнее достигать целей обучения. '
        'Классные преподаватели знают эту особенность и стараются создать '
        'среду, в которой комфортно учиться.'
    ])
    buttons = [[
        InlineKeyboardButton(text='Но ведь у онлайна есть и плюсы?', callback_data=DUMMY),
    ]]
    keyboard = InlineKeyboardMarkup(buttons)

    await update.callback_query.message.reply_text(text, reply_markup=keyboard)

    return BLOCK1_QUIZ_3


async def block1_quiz_3(update: Update, context: ContextTypes.DEFAULT_TYPE) -> str:
    query = update.callback_query
    await query.answer()

    text = '\n'.join([
        'Да. Думаю, они уже пришли вам в голову :)',
        '',
        'Не нужно тратить время на дорогу: открываете глаза '
        '— и вам сразу доступен свет ученья. Больше нет '
        'привязки к географии. Многие специалисты преподают в онлайне '
        'для студентов из разных городов и стран.',
        '',
        'Легче подстроить график под учебу — многие вещи можно '
        'осваивать самому в удобное время. ',
        '',
        'Согласитесь, плюсы очень привлекательные?'
    ])
    buttons = [[
        InlineKeyboardButton(text='А что с минусами делать?', callback_data=DUMMY),
    ]]
    keyboard = InlineKeyboardMarkup(buttons)

    await update.callback_query.message.reply_text(text, reply_markup=keyboard)

    return BLOCK1_QUIZ_4


async def block1_quiz_4(update: Update, context: ContextTypes.DEFAULT_TYPE) -> str:
    query = update.callback_query
    await query.answer()

    text = """На этот вопрос мы будем искать ответ в течение всего курса. Сейчас нам важно запомнить, чем отличается обучение в онлайне. 

Кстати, чем? 

1 – студент не всегда понимает, зачем он учится и чего хочет достичь 
2 – студент чувствует себя дистанцированно, поэтому сложнее включаться в процесс обучения 
3 – студент считает обучение неэффективным 
4 – студенту сложнее удерживать внимание, потому что много отвлекающих факторов"""

    buttons = [[
        InlineKeyboardButton(text='1 и 3', callback_data=ANSWER_2),
        InlineKeyboardButton(text='2 и 4', callback_data=ANSWER_1),
    ], [
        InlineKeyboardButton(text='1 и 4', callback_data=ANSWER_2),
        InlineKeyboardButton(text='2 и 3', callback_data=ANSWER_2),
    ]]
    keyboard = InlineKeyboardMarkup(buttons)

    await update.callback_query.message.reply_text(text, reply_markup=keyboard)

    return BLOCK1_QUIZ_5


async def block1_quiz_5(update: Update, context: ContextTypes.DEFAULT_TYPE) -> str:
    query = update.callback_query
    await query.answer()

    if query.data == ANSWER_1:
        text = '\n'.join([
            'Верно! Осознать цель обучения важно и в онлайне, и в офлайне. '
            'Эффективность обучения, как показывают различные исследования, '
            'например <a href="https://iq.hse.ru/news/217043836.html/">от Центра '
            'социологии НИУ ВШЭ</a>, также не зависит от формата.',
        ])
    else:
        text = '\n'.join([
            'Не совсем. Студенту правда сложнее удерживать внимание и включаться в процесс обучения.',
            '',
            'Осознать цель обучения важно и в онлайне, и в офлайне. '
            'Эффективность обучения, как показывают различные исследования, '
            'например <a href="https://iq.hse.ru/news/217043836.html/">от Центра '
            'социологии НИУ ВШЭ</a>, также не зависит от формата.'
        ])
    await update.callback_query.message.reply_text(text=text, disable_web_page_preview=True, parse_mode=ParseMode.HTML)

    await asleep(10)

    text = '\n'.join([
        'Кроме специфики формата обучения преподавателю важно '
        'знать, как учатся взрослые. Вопросом обучения взрослых '
        'занимается такая наука, как <b>андрагогика</b>.'
    ])

    buttons = [[
        InlineKeyboardButton(text='Почему это важно?', callback_data=DUMMY),
    ]]
    keyboard = InlineKeyboardMarkup(buttons)

    await update.callback_query.message.reply_text(text, reply_markup=keyboard, parse_mode=ParseMode.HTML)

    return BLOCK1_QUIZ_6


async def block1_quiz_6(update: Update, context: ContextTypes.DEFAULT_TYPE) -> str:
    query = update.callback_query
    await query.answer()

    await context.bot.copy_message(chat_id=update.effective_chat.id, from_chat_id=MEDIA_CHANNEL_ID,
                                   message_id=MEDIA_PHOTO_3)
    text = '\n'.join([
        '<b>Андрагогика</b> сообщает нам, что мышление взрослого и его '
        'требования к обучению разительно отличаются от детей. '
        'Поэтому важно учитывать основные принципы андрагогики.'
    ])
    await context.bot.send_message(chat_id=update.effective_chat.id, text=text, parse_mode=ParseMode.HTML)

    await asleep(5)

    text = '\n'.join([
        'Поговорим о них подробнее.',
        '',
        '<b>Первый принцип</b> – взрослые хотят учиться тому, '
        'что связано с их работой или личными задачами. ',
        '',
        'Они приходят не за знаниями как таковыми, а за решением '
        'своих проблем. Будет здорово, если вы сможете фокусировать '
        'студентов на пользе обучения, связывать ее с '
        'продвижением по карьере или личным развитием.'
    ])
    buttons = [[
        InlineKeyboardButton(text='Попробую!',
                             callback_data=DUMMY),
    ], [
        InlineKeyboardButton(text='Уже использую это', callback_data=DUMMY),
    ]]
    keyboard = InlineKeyboardMarkup(buttons)

    await update.callback_query.message.reply_text(text, reply_markup=keyboard, parse_mode=ParseMode.HTML)

    return BLOCK1_QUIZ_7


async def block1_quiz_7(update: Update, context: ContextTypes.DEFAULT_TYPE) -> str:
    query = update.callback_query
    await query.answer()

    text = '\n'.join([
        '<b>Второй принцип</b> – обучение взрослых должно '
        'строиться на практике. Нет — длинным абстрактным теориям. Да — реальным кейсам!',
        '',
        'Для решения большинства задач, как личных, '
        'так и рабочих, важны навыки. Их можно тренировать '
        'и развивать с помощью практики, поэтому она так важна в обучении взрослых.'
    ])

    buttons = [[
        InlineKeyboardButton(text='Буду внедрять больше практики', callback_data=DUMMY),
    ], [
        InlineKeyboardButton(text='Строю свои занятия на практике',
                             callback_data=DUMMY),
    ]]
    keyboard = InlineKeyboardMarkup(buttons)

    await update.callback_query.message.reply_text(text, reply_markup=keyboard, parse_mode=ParseMode.HTML)

    return BLOCK1_QUIZ_8


async def block1_quiz_8(update: Update, context: ContextTypes.DEFAULT_TYPE) -> str:
    query = update.callback_query
    await query.answer()

    text = '\n'.join([
        '<b>Третий принцип</b> – нельзя игнорировать опыт студента.',
        ' ',
        'Студенты могут не иметь '
        'богатых профессиональных знаний в вашей области, '
        'но у них точно есть багаж жизненного опыта. '
        'Обращайтесь к нему – связывайте новый '
        'материал с понятными студентам явлениями.'
    ])

    buttons = [[
        InlineKeyboardButton(text='Интересная идея!', callback_data=DUMMY),
    ], [
        InlineKeyboardButton(text='Всегда практикую такой прием!', callback_data=DUMMY),
    ]]
    keyboard = InlineKeyboardMarkup(buttons)

    await update.callback_query.message.reply_text(text, reply_markup=keyboard, parse_mode=ParseMode.HTML)

    return BLOCK1_QUIZ_9


async def block1_quiz_9(update: Update, context: ContextTypes.DEFAULT_TYPE) -> str:
    query = update.callback_query
    await query.answer()

    text = '\n'.join([
        '<b>Четвертый принцип</b> – взрослые должны участвовать '
        'в планировании и оценке собственного обучения. ',
        '',
        'Они в состоянии определить свои цели на обучение и '
        'желаемые результаты от него. Преподавателю важно создать '
        'такую обстановку, в которой студент не будет чувствовать '
        'себя зависимым, ведомым – наоборот, где студент сможет '
        'проявлять свою активность и самостоятельность.'
    ])

    buttons = [[
        InlineKeyboardButton(text='Подумаю над этим', callback_data=DUMMY),
    ], [
        InlineKeyboardButton(text='Даю студентам возможность проявить себя', callback_data=DUMMY),
    ]]
    keyboard = InlineKeyboardMarkup(buttons)

    await update.callback_query.message.reply_text(text, reply_markup=keyboard, parse_mode=ParseMode.HTML)

    return BLOCK1_QUIZ_10


async def block1_quiz_10(update: Update, context: ContextTypes.DEFAULT_TYPE) -> str:
    query = update.callback_query
    await query.answer()

    text = '\n'.join([
        '<b>Пятый принцип</b> – со взрослыми надо общаться на '
        'равных.',
        ' ',
        'Им не нужна дидактика и нравоучения '
        '(смотрите пункт выше про собственный опыт), '
        'общайтесь с ними с позиции «взрослый — взрослый».'
    ])

    buttons = [[
        InlineKeyboardButton(text='Да, делаю так неосознанно', callback_data=DUMMY),
    ], [
        InlineKeyboardButton(text='Всегда следую этому принципу', callback_data=DUMMY),
    ]]
    keyboard = InlineKeyboardMarkup(buttons)

    await update.callback_query.message.reply_text(text, reply_markup=keyboard, parse_mode=ParseMode.HTML)

    return BLOCK1_QUIZ_11


async def block1_quiz_11(update: Update, context: ContextTypes.DEFAULT_TYPE) -> str:
    query = update.callback_query
    await query.answer()

    text = '\n'.join([
        'Проверим, получилось ли у вас запомнить '
        'основные принципы андрагогики? Все '
        'просто – я присылаю вам утверждение, '
        'если оно соотвествует принципу, вы '
        'отвечаете «правда», если нет – «ложь».'
    ])

    buttons = [[
        InlineKeyboardButton(text='Вперед', callback_data=DUMMY),
    ]]
    keyboard = InlineKeyboardMarkup(buttons)

    await update.callback_query.message.reply_text(text, reply_markup=keyboard)

    return BLOCK1_QUIZ_12


async def block1_quiz_12(update: Update, context: ContextTypes.DEFAULT_TYPE) -> str:
    query = update.callback_query
    await query.answer()

    text = '\n'.join([
        'Взрослые люди не любят, '
        'когда обращаются к их предыдущему опыту. '
        'Они приходят за новыми знаниями, а не за '
        'воспоминаниями о жизненных ситуациях.'
    ])

    buttons = [[
        InlineKeyboardButton(text='Правда', callback_data=ANSWER_1),
        InlineKeyboardButton(text='Ложь', callback_data=ANSWER_2),
    ]]
    keyboard = InlineKeyboardMarkup(buttons)

    await update.callback_query.message.reply_text(text, reply_markup=keyboard)

    return BLOCK1_QUIZ_13


async def block1_quiz_13(update: Update, context: ContextTypes.DEFAULT_TYPE) -> str:
    query = update.callback_query
    await query.answer()

    if query.data == ANSWER_1:
        text = '\n'.join([
            'Как раз наоборот! Взрослым важно, '
            'чтобы их опыт учитывали в обучении.'
        ])
    else:
        text = '\n'.join([
            'Верно! Взрослым важно, '
            'чтобы их опыт учитывали в обучении.'
        ])

    await update.callback_query.message.reply_text(text=text)

    await asleep(2)

    text = '\n'.join([
        'Для взрослых в обучении более '
        'важно научиться решать свои личные '
        'и профессиональные задачи, а не получить новые знания.'
    ])

    buttons = [[
        InlineKeyboardButton(text='Правда', callback_data=ANSWER_1),
        InlineKeyboardButton(text='Ложь', callback_data=ANSWER_2),
    ]]
    keyboard = InlineKeyboardMarkup(buttons)

    await update.callback_query.message.reply_text(text, reply_markup=keyboard)

    return BLOCK1_QUIZ_14


async def block1_quiz_14(update: Update, context: ContextTypes.DEFAULT_TYPE) -> str:
    query = update.callback_query
    await query.answer()

    if query.data == ANSWER_1:
        text = '\n'.join([
            'Верно! Чаще всего взрослые приходят '
            'учиться тому, что связано с их '
            'личными или профессиональными запросами.'
        ])
    else:
        text = '\n'.join([
            'Это правда. Чаще всего взрослые приходят '
            'учиться тому, что связано с их личными '
            'или профессиональными запросами.'
        ])

    await update.callback_query.message.reply_text(text=text)

    await asleep(3)

    text = '\n'.join([
        'Чем больше теории – тем лучше! Взрослым '
        'важно понять, что перед ними настоящий '
        'академик и доктор наук.'
    ])

    buttons = [[
        InlineKeyboardButton(text='Правда', callback_data=ANSWER_1),
        InlineKeyboardButton(text='Ложь', callback_data=ANSWER_2),
    ]]
    keyboard = InlineKeyboardMarkup(buttons)

    await update.callback_query.message.reply_text(text, reply_markup=keyboard)

    return BLOCK1_QUIZ_15


async def block1_quiz_15(update: Update, context: ContextTypes.DEFAULT_TYPE) -> str:
    query = update.callback_query
    await query.answer()

    if query.data == ANSWER_1:
        text = '\n'.join([
            'Это ложь. Конечно, взрослым важно убедиться, '
            'что перед ними настоящий профессионал и совсем '
            'без теории обойтись не получится. Однако, чаще '
            'всего обучение взрослых ориентировано на получение '
            'навыков, поэтому лучше делать упор на практику.'
        ])
    else:
        text = '\n'.join([
            'Верно! Это ложь. Конечно, взрослым важно убедиться, '
            'что перед ними настоящий профессионал и совсем без '
            'теории обойтись не получится. Однако, чаще всего обучение '
            'взрослых ориентировано на получение навыков, поэтому '
            'лучше делать упор на практику.'
        ])

    await update.callback_query.message.reply_text(text=text)

    await asleep(3)

    text = '\n'.join([
        'Взрослому важно участвовать '
        'в планировании своего обучения, сверяться '
        'с целями и отслеживать прогресс.'
    ])

    buttons = [[
        InlineKeyboardButton(text='Правда', callback_data=ANSWER_1),
        InlineKeyboardButton(text='Ложь', callback_data=ANSWER_2),
    ]]
    keyboard = InlineKeyboardMarkup(buttons)

    await update.callback_query.message.reply_text(text, reply_markup=keyboard)

    return BLOCK1_QUIZ_16


async def block1_quiz_16(update: Update, context: ContextTypes.DEFAULT_TYPE) -> str:
    query = update.callback_query
    await query.answer()

    if query.data == ANSWER_1:
        text = '\n'.join([
            'Да, это правда. Здорово, когда у '
            'преподавателя получается помочь в этом студентам.'
        ])
    else:
        text = '\n'.join([
            'Это правда. Здорово, когда у преподавателя '
            'получается помочь в этом студентам.'
        ])

    await update.callback_query.message.reply_text(text=text)

    await asleep(3)

    text = '\n'.join([
        'Отлично! Можем двигаться дальше.',
        '',
        'Допустим, преподаватель учёл все эти принципы'
        ' и уже готов начать преподавать. Но тут скрывается'
        ' ещё один нюанс, о котором мы упомянули выше, — мотивация студента.'
    ])

    buttons = [[
        InlineKeyboardButton(text='В чём нюанс?', callback_data=DUMMY),
    ]]
    keyboard = InlineKeyboardMarkup(buttons)

    await update.callback_query.message.reply_text(text, reply_markup=keyboard)

    return BLOCK1_STUDENT_1


async def block1_student_1(update: Update, context: ContextTypes.DEFAULT_TYPE) -> str:
    query = update.callback_query
    await query.answer()

    text = """Мотивация бывает внешней и внутренней.

<b>Внешняя мотивация</b> возникает из-за обстоятельств, в которых находится человек. Например, надо ходить в школу для дальнейшей сдачи ЕГЭ или пойти в вуз на любую специальность, чтобы просто получить диплом.

<b>Внутренняя мотивация</b> исходит от самого человека и основывается на его ценностях и интересах. Например, пойти на онлайн-курс по дизайну сайтов, чтобы сменить профессию, или учить английский, чтобы больше и чаще путешествовать. Эта мотивация оказывается сильнее и может работать более долговременно."""

    await update.callback_query.message.reply_text(text=text, parse_mode=ParseMode.HTML)

    await asleep(10)

    text = '\n'.join([
        'Внешняя мотивация построена на внешних стимулах: '
        'оценки, дедлайны, рейтинги и т. д. Как правило, '
        'такая мотивация проходит быстро, и долго на ней держаться не получится.',
        '',
        'Внутренняя мотивация построена на личной цели обучения, '
        'получении удовольствия от процесса. Высокий уровень внутренней '
        'мотивации приводит к тому, что человек сам организовывает процесс'
        ' обучения, следит за дедлайнами, больше анализирует полученный опыт и'
        ' обращает внимание на свой прогресс. Поэтому лучше помогать студенту'
        ' обращаться к внутренней мотивации.'
    ])

    buttons = [[
        InlineKeyboardButton(text='Как это сделать?', callback_data=DUMMY),
    ]]
    keyboard = InlineKeyboardMarkup(buttons)

    await update.callback_query.message.reply_text(text, reply_markup=keyboard)

    return BLOCK1_STUDENT_2


async def block1_student_2(update: Update, context: ContextTypes.DEFAULT_TYPE) -> str:
    query = update.callback_query
    await query.answer()

    await context.bot.copy_message(chat_id=update.effective_chat.id, from_chat_id=MEDIA_CHANNEL_ID,
                                   message_id=MEDIA_PHOTO_4)
    text = '\n'.join([
        'В процессе обучения самоощущение студента '
        'меняется: он набирает больше знаний по теме, '
        'увереннее ориентируется в курсе. Меняется и '
        'его мотивация к обучению, даже внутренняя :)',
        '',
        'Согласно модели SSDL (the Staged Self Directed Learning), '
        'мотивация учащегося проходит 4 стадии:',
        '',
        '1. Зависимый. ',
        '2. Заинтересованный. ',
        '3. Вовлечённый. ',
        '4. Самоуправляемый.',
        '',
        'На каждой из стадий у студента появляются'
        ' новые запросы к обучению и, что особенно '
        'важно, к позиции преподавателя. Хорошему'
        ' преподавателю важно быть гибким и подстраивать '
        'свой стиль преподавания под запрос студента.',
        '',
        'Давайте рассмотрим подробнее каждую из этих стадий.'
    ])

    await context.bot.send_message(chat_id=update.effective_chat.id, text=text, parse_mode=ParseMode.HTML)

    await asleep(15)

    text = '\n'.join([
        '<b>Стадия «Зависимый»</b>',
        '',
        'Начало обучения, примерно 1⁄3 курса.',
        '',
        '<b>Студент:</b>',
        '– полон сил и желания учиться, полностью зависим от преподавателя;',
        '– хочет быть уверен, что преподаватель профи и '
        'отличный эксперт по теме, ему можно доверять;',
        '– нуждается в чётком инструктаже и подробной '
        'обратной связи на каждом шаге.',
        '',
        '<b>Преподаватель:</b>',
        '– формирует доверие к себе, как эксперту;',
        '– даёт чёткие инструкции и сопровождает каждый шаг студента;',
        '– объясняет ценность обучения и помогает '
        'сформулировать учебные цели.',
        '',
        'Какая стадия следующая?'
    ])

    buttons = [
        [InlineKeyboardButton(text='Заинтересованный', callback_data=DUMMY)],
        [InlineKeyboardButton(text='Вовлеченный', callback_data=DUMMY)],
        [InlineKeyboardButton(text='Самоуправляемый', callback_data=DUMMY)],
    ]
    keyboard = InlineKeyboardMarkup(buttons)

    await update.callback_query.message.reply_text(text, reply_markup=keyboard, parse_mode=ParseMode.HTML)

    return BLOCK1_STUDENT_3


async def block1_student_3(update: Update, context: ContextTypes.DEFAULT_TYPE) -> str:
    query = update.callback_query
    await query.answer()

    text = '\n'.join([
        '<b>Стадия «Заинтересованный»</b>',
        '',
        'Ближе к середине обучения, конец 1⁄3 курса.',
        '',
        '<b>Студент:</b>',
        '– испытывает когнитивное сопротивление — наш мозг не очень любит учиться новому;',
        '– спад активности.',
        '',
        '<b>Преподаватель:</b>',
        '– напоминает о целях обучения,'
        ' помогает сформулировать внутреннюю мотивацию '
        '— понять, зачем студент учится, ради чего;',
        ' – поощряет маленькие победы, больше акцента '
        'делает на успехах, а не ошибках.',
        '',
        'Вторая стадия самая сложная для студента, '
        'поэтому главная задача преподавателя — '
        'помочь преодолеть когнитивное '
        'сопротивление и перейти к стадии...'
    ])

    buttons = [
        [InlineKeyboardButton(text='Вовлеченный', callback_data=DUMMY)],
        [InlineKeyboardButton(text='Самоуправляемый', callback_data=DUMMY)],
    ]
    keyboard = InlineKeyboardMarkup(buttons)

    await update.callback_query.message.reply_text(text, reply_markup=keyboard, parse_mode=ParseMode.HTML)

    return BLOCK1_STUDENT_4


async def block1_student_4(update: Update, context: ContextTypes.DEFAULT_TYPE) -> str:
    query = update.callback_query
    await query.answer()

    text = '\n'.join([
        '<b>«Вовлечённости»</b>',
        '',
        'Середина обучения, но стадия может не '
        'наступить, если студент застрял на предыдущей.',
        '',
        '<b>Студент:</b>',
        '- мотивация стабилизируется и усиливается;',
        '– чувствует ответственность за результат;',
        '– самостоятельный и менее зависимый от эксперта;',
        '– готов выполнять более сложные проекты, работать в команде.',
        '',
        '<b>Преподаватель:</b>',
        '– поощряет самостоятельность;',
        '– даёт сложные задания, дополнительные материалы;',
        '– координирует групповую работу.'
    ])

    buttons = [[
        InlineKeyboardButton(text='Когда студент самоуправляемый?', callback_data=DUMMY),
    ]]
    keyboard = InlineKeyboardMarkup(buttons)

    await update.callback_query.message.reply_text(text, reply_markup=keyboard, parse_mode=ParseMode.HTML)

    return BLOCK1_STUDENT_5


async def block1_student_5(update: Update, context: ContextTypes.DEFAULT_TYPE) -> str:
    query = update.callback_query
    await query.answer()

    text = '\n'.join([
        '<b>Стадия «Самоуправляемый»</b>',
        '',
        'Конец обучения, но стадия может '
        'не наступить, если студент застрял '
        'на предыдущих.',
        '',
        '<b>Студент:</b>',
        '– высокая мотивация;',
        '– полная самостоятельность;',
        '– интерес к сложным задачам вне рамок обучения.',
        '',
        '<b>Преподаватель:</b>',
        '- меньше включён в работу студента, больше направляет и советует;',
        '– помогает сформировать траекторию развития после обучения;',
        '– проводит совместную рефлексию.'
    ])

    buttons = [[
        InlineKeyboardButton(text='Как использовать эти стадии?', callback_data=DUMMY),
    ]]
    keyboard = InlineKeyboardMarkup(buttons)

    await update.callback_query.message.reply_text(text, reply_markup=keyboard, parse_mode=ParseMode.HTML)

    return BLOCK1_STUDENT_6


async def block1_student_6(update: Update, context: ContextTypes.DEFAULT_TYPE) -> str:
    query = update.callback_query
    await query.answer()

    text = '\n'.join([
        'Например, можно поделить курс на стадии и '
        'спрогнозировать мотивационную стратегию. '
        'В зависимости от того, на каком этапе '
        'находится занятие, вы можете предположить, '
        'какая стратегия будет оптимальной: дать'
        ' больше или меньше поддержки, подобрать сложность заданий.'
    ])

    buttons = [[
        InlineKeyboardButton(text='Если мои занятия в начале курса?', callback_data=DUMMY),
    ]]
    keyboard = InlineKeyboardMarkup(buttons)

    await update.callback_query.message.reply_text(text, reply_markup=keyboard)

    return BLOCK1_STUDENT_7


async def block1_student_7(update: Update, context: ContextTypes.DEFAULT_TYPE) -> str:
    query = update.callback_query
    await query.answer()

    text = '\n'.join([
        'Как считаете, в начале обучения важно:',
        '1 – дать студенту больше поддержки: '
        'например, четкие инструкции и алгоритмы,'
        ' более простые задания, примеры их выполнения ',
        '2 – дать возможность проявить самостоятельность: '
        'давать сложные задания, призывать к '
        'самостоятельному поиску ответов'
    ])

    buttons = [[
        InlineKeyboardButton(text='1', callback_data=ANSWER_1),
        InlineKeyboardButton(text='2', callback_data=ANSWER_2),
    ]]
    keyboard = InlineKeyboardMarkup(buttons)

    await update.callback_query.message.reply_text(text, reply_markup=keyboard)

    return BLOCK1_STUDENT_8


async def block1_student_8(update: Update, context: ContextTypes.DEFAULT_TYPE) -> str:
    query = update.callback_query
    await query.answer()

    if query.data == ANSWER_1:
        text = '\n'.join([
            'Верно! В начале обучения студентов '
            'ждет много нового. Как известно, наш'
            ' мозг любит сопротивляться новизне. '
            'Поэтому важно дать больше поддержки, '
            'чтобы помочь преодолеть это сопротивление.'
        ])
    else:
        text = '\n'.join([
            'Не совсем. В начале обучения студентов ждет много нового. Как известно, наш мозг любит сопротивляться '
            'новизне. Поэтому важно дать больше поддержки, чтобы помочь преодолеть это сопротивление.'
        ])

    buttons = [[
        InlineKeyboardButton(text='Если мои занятия в середине курса?',
                             callback_data=ANSWER_1),
    ]]
    keyboard = InlineKeyboardMarkup(buttons)

    await update.callback_query.message.reply_text(text, reply_markup=keyboard)

    return BLOCK1_STUDENT_9


async def block1_student_9(update: Update, context: ContextTypes.DEFAULT_TYPE) -> str:
    query = update.callback_query
    await query.answer()

    text = '\n'.join([
        'Уделите особое внимание успехам учащихся. '
        'Если обучение уже запущено, вы можете '
        'ориентироваться на живую обратную связь: '
        'чего не хватает студентам, как они чувствует '
        'себя в процессе обучения.',
        '',
        '<b>Как думаете, что можно сделать в такой ситуации?</b>'
        ' Выберите все, что кажется вам подходящим ',
        '1 – попробовать обратиться к целям обучения, помочь студентам свериться с ними и оценить свой прогресс ',
        '2 – усложнить задания, дистанцироваться от студентов, чтобы они стали более самостоятельны ',
        '3 – уделить больше '
        'внимания успехам, чаще хвалить и фокусировать студентов на достижениях ',
        '4 – предложить студентам групповые '
        'проекты, которые не будут курироваться экспертом, наблюдать, как они справятся ',
        '5 – спросить у студентов, '
        'какие сложности сейчас есть, как им можно помочь'
    ])

    buttons = [[
        InlineKeyboardButton(text='1, 2, 4', callback_data=ANSWER_2),
        InlineKeyboardButton(text='3, 4, 5', callback_data=ANSWER_2),
    ], [
        InlineKeyboardButton(text='1, 3, 5', callback_data=ANSWER_1),
        InlineKeyboardButton(text='2, 4, 5', callback_data=ANSWER_2),
    ]]
    keyboard = InlineKeyboardMarkup(buttons)

    await update.callback_query.message.reply_text(text, reply_markup=keyboard, parse_mode=ParseMode.HTML)

    return BLOCK1_STUDENT_10


async def block1_student_10(update: Update, context: ContextTypes.DEFAULT_TYPE) -> str:
    query = update.callback_query
    await query.answer()

    if query.data == ANSWER_1:
        text = '\n'.join([
            'Верно! Стоит напомнить студентам о целях и отметить их достижения, но дистанцироваться не стоит. Если вы '
            'хотите организовать групповую работу или усложнить задания, поддержка преподавателя точно понадобится!',
            ' ',
            'Например, вы можете объяснить студентам, как именно стоит работать над этой задачей в команде, '
            'что стоит учесть.',
            ' ',
            'Также вы можете объяснить, какие навыки и знания студенты получат, если выполнят это '
            'сложное задание, как оно поможет им в решении реальных задач.',
            '',
            'Если вы запросили обратную связь об '
            'обучении у студентов, не забудьте отреагировать на нее: поблагодарить и сообщить студентам, '
            'что получилось учесть и каким образом.'
        ])
    else:
        text = '\n'.join([
            'Не совсем. Действительно, стоит напомнить студентам о целях и отметить их достижения, '
            'но дистанцироваться не стоит. Если вы хотите организовать групповую работу или усложнить задания, '
            'поддержка преподавателя точно понадобится! Например, вы можете объяснить студентам, как именно стоит '
            'работать над этой задачей в команде, что стоит учесть. Также вы можете объяснить, какие навыки и знания '
            'студенты получат, если выполнят это сложное задание, как оно поможет им в решении реальных задач. Если '
            'вы запросили обратную связь об обучении у студентов, не забудьте отреагировать на нее: поблагодарить и '
            'сообщить студентам, что получилось учесть и каким образом.'
        ])

    buttons = [[
        InlineKeyboardButton(text='Если студенты инициативны?',
                             callback_data=DUMMY),
    ]]
    keyboard = InlineKeyboardMarkup(buttons)

    await update.callback_query.message.reply_text(text, reply_markup=keyboard)

    return BLOCK1_STUDENT_11


async def block1_student_11(update: Update, context: ContextTypes.DEFAULT_TYPE) -> str:
    query = update.callback_query
    await query.answer()

    text = """В таком случае стоит предоставить студентам больше самостоятельности, больше направлять и советовать.   

<b>Подведем короткий итог и определимся, кто такой преподаватель в онлайне?</b> Какого преподавателя мы могли бы назвать классным? Выбирайте преподавателя, у которого сами хотели бы поучиться."""

    await update.callback_query.message.reply_text(text=text, parse_mode=ParseMode.HTML)

    await asleep(5)

    await context.bot.copy_message(chat_id=update.effective_chat.id, from_chat_id=MEDIA_CHANNEL_ID,
                                   message_id=MEDIA_TEACHERS_1)

    text = '\n'.join([
        '1 — фанат теории и эссе на тему «Если бы, то...» ',
        '2 — профи, не прощающий ошибок',
        '3 — практик, призывающий своих учеников пробовать и оттачивать навыки'
    ])

    buttons = [[
        InlineKeyboardButton(text='1', callback_data=ANSWER_1),
        InlineKeyboardButton(text='2', callback_data=ANSWER_2),
        InlineKeyboardButton(text='3', callback_data=ANSWER_3),
    ]]
    keyboard = InlineKeyboardMarkup(buttons)

    await update.callback_query.message.reply_text(text, reply_markup=keyboard, parse_mode=ParseMode.HTML)

    return BLOCK1_STUDENT_12


async def block1_student_12(update: Update, context: ContextTypes.DEFAULT_TYPE) -> str:
    query = update.callback_query
    await query.answer()

    answer_sentence_map = {
        ANSWER_1: 'фанат теории и эссе на тему «Если бы, то...»',
        ANSWER_2: 'профи, не прощающий ошибок',
        ANSWER_3: 'практик, призывающий своих учеников пробовать и оттачивать навыки',
    }
    context.user_data[USER_DATA_BLOCK1_TEACHER_SENTENCES] = [answer_sentence_map[query.data]]

    await context.bot.copy_message(chat_id=update.effective_chat.id, from_chat_id=MEDIA_CHANNEL_ID,
                                   message_id=MEDIA_TEACHERS_2)

    text = '\n'.join([
        '1 — понимает ценность и сложности онлайн-обучения и помогает студентам учиться в онлайне эффективно',
        '2 — «Что такое онлайн?»',
        '3 — забивает на студентов не только в онлайне :)',
    ])
    buttons = [[
        InlineKeyboardButton(text='1', callback_data=ANSWER_1),
        InlineKeyboardButton(text='2', callback_data=ANSWER_2),
        InlineKeyboardButton(text='3', callback_data=ANSWER_3),
    ]]
    keyboard = InlineKeyboardMarkup(buttons)

    await update.callback_query.message.reply_text(text, reply_markup=keyboard)

    return BLOCK1_STUDENT_13


async def block1_student_13(update: Update, context: ContextTypes.DEFAULT_TYPE) -> str:
    query = update.callback_query
    await query.answer()

    answer_sentence_map = {
        ANSWER_1: 'понимает ценность и сложности онлайн-обученияи помогает студентам  учиться в онлайне эффективно',
        ANSWER_2: '«Что такое онлайн?»',
        ANSWER_3: 'забивает на студентов не только в онлайне :)',
    }
    context.user_data[USER_DATA_BLOCK1_TEACHER_SENTENCES].append(answer_sentence_map[query.data])

    await context.bot.copy_message(chat_id=update.effective_chat.id, from_chat_id=MEDIA_CHANNEL_ID,
                                   message_id=MEDIA_TEACHERS_3)

    text = """1 — отличный профи, который не заботится о мотивации студентов и комфортной среде для обучения
2 — с эмпатией относится к студентам, думает об их мотивации и вовлечённости, помогает реализовать свои таланты
3 — использует жёсткие методы мотивации студентов: ультиматумы и провокации"""

    buttons = [[
        InlineKeyboardButton(text='1', callback_data=ANSWER_1),
        InlineKeyboardButton(text='2', callback_data=ANSWER_2),
        InlineKeyboardButton(text='3', callback_data=ANSWER_3),
    ]]
    keyboard = InlineKeyboardMarkup(buttons)

    await update.callback_query.message.reply_text(text, reply_markup=keyboard)

    return BLOCK1_STUDENT_14


async def block1_student_14(update: Update, context: ContextTypes.DEFAULT_TYPE) -> str:
    query = update.callback_query
    await query.answer()

    answer_sentence_map = {
        ANSWER_1: 'отличный профи, который не заботится о мотивации студентов и комфортной среде для обучения',
        ANSWER_2: 'с эмпатией относится к студентам, думает об их мотивации и вовлечении, '
                  'помогает реализовать свои таланты',
        ANSWER_3: 'использует жёсткие методы мотивации студентов: ультиматумы и провокации',
    }
    context.user_data[USER_DATA_BLOCK1_TEACHER_SENTENCES].append(answer_sentence_map[query.data])

    await context.bot.copy_message(chat_id=update.effective_chat.id, from_chat_id=MEDIA_CHANNEL_ID,
                                   message_id=MEDIA_TEACHERS_4)


    text = '\n'.join([
        '1 — гиперопекающий, не дающий студентам шанса проявить инициативу, ошибиться или сделать что-то самим ',
        '2 — тиран, у которого выживает сильнейший',
        '3 — признающий самостоятельность учеников, дающий при этом поддержку и необходимые знания',
    ])

    buttons = [[
        InlineKeyboardButton(text='1', callback_data=ANSWER_1),
        InlineKeyboardButton(text='2', callback_data=ANSWER_2),
        InlineKeyboardButton(text='3', callback_data=ANSWER_3),
    ]]
    keyboard = InlineKeyboardMarkup(buttons)

    await update.callback_query.message.reply_text(text, reply_markup=keyboard)

    return BLOCK1_STUDENT_15


async def block1_student_15(update: Update, context: ContextTypes.DEFAULT_TYPE) -> str:
    query = update.callback_query
    await query.answer()

    answer_sentence_map = {
        ANSWER_1: 'гиперопекающий, не дающий студентам шанса проявить инициативу, ошибиться или сделать что-то самим',
        ANSWER_2: 'тиран, у которого выживает сильнейший',
        ANSWER_3: 'признающий самостоятельность учеников, дающий при этом поддержку и необходимые знания',
    }
    context.user_data[USER_DATA_BLOCK1_TEACHER_SENTENCES].append(answer_sentence_map[query.data])

    await context.bot.copy_message(chat_id=update.effective_chat.id, from_chat_id=MEDIA_CHANNEL_ID,
                                   message_id=MEDIA_TEACHERS_5)

    text = '\n'.join([
        '1 — умеет структурировать контент и знает, как построить занятие и вовлечь в него студентов  ',
        '2 — обладает кучей регалий, рассказывает странные и спорные вещи, но с невероятным артистизмом  ',
        '3 — сам настолько увлечён своим делом, что практически не замечает учеников в процессе',
    ])

    buttons = [[
        InlineKeyboardButton(text='1', callback_data=ANSWER_1),
        InlineKeyboardButton(text='2', callback_data=ANSWER_2),
        InlineKeyboardButton(text='3', callback_data=ANSWER_3),
    ]]
    keyboard = InlineKeyboardMarkup(buttons)

    await update.callback_query.message.reply_text(text, reply_markup=keyboard)

    return BLOCK1_STUDENT_16


async def block1_student_16(update: Update, context: ContextTypes.DEFAULT_TYPE) -> str:
    query = update.callback_query
    await query.answer()

    answer_sentence_map = {
        ANSWER_1: 'умеет структурировать контент и знает, как построить занятие и вовлечь в него студентов',
        ANSWER_2: 'обладает кучей регалий, рассказывает странные и спорные вещи, но с невероятным артистизмом',
        ANSWER_3: 'сам настолько увлечён своим делом, что практически не замечает учеников в процессе',
    }
    context.user_data[USER_DATA_BLOCK1_TEACHER_SENTENCES].append(answer_sentence_map[query.data])

    sentences = '\n'.join([f'- {i}' for i in context.user_data[USER_DATA_BLOCK1_TEACHER_SENTENCES]])
    text = f'Итак, для вас отличный преподаватель:\n{sentences}'

    buttons = [[
        InlineKeyboardButton(text='Неплохо получилось!', callback_data=DUMMY),
    ]]
    keyboard = InlineKeyboardMarkup(buttons)

    await update.callback_query.message.reply_text(text, reply_markup=keyboard)

    return BLOCK1_STUDENT_17


async def block1_student_17(update: Update, context: ContextTypes.DEFAULT_TYPE) -> str:
    query = update.callback_query
    await query.answer()

    text = '\n'.join([
        'Мы тоже так считаем. Наше видение отличного преподавателя мы уложили в этот чек-лист. Вы можете сохранить '
        'его и свериться с ним, чтобы понять, что вы уже знаете, что пробовали, а что предстоит изучить.'
    ])

    buttons = [[
        InlineKeyboardButton(text='Скачать чек-лист!', callback_data=ANSWER_1),
        InlineKeyboardButton(text='Идем дальше', callback_data=ANSWER_2),
    ]]
    keyboard = InlineKeyboardMarkup(buttons)

    await update.callback_query.message.reply_text(text, reply_markup=keyboard)

    return BLOCK1_STUDENT_18


async def block1_student_18(update: Update, context: ContextTypes.DEFAULT_TYPE) -> str:
    query = update.callback_query
    await query.answer()

    if query.data == ANSWER_1:
        await context.bot.copy_message(chat_id=update.effective_chat.id, from_chat_id=MEDIA_CHANNEL_ID,
                                       message_id=MEDIA_DOC_1)

    text = '\n'.join([
        'Кажется, с тем, кто такой преподаватель, всё ясно. '
        'Но что ближе вам – проверять работы студентов, проводить '
        'вебинары или все вместе?',
        ' ',
        'Можем попробовать в этом разобраться вместе. '
        'Я предложу несколько тезисов, а вы отметите, насколько они вам близки. Посмотрим, что получится в итоге.'
    ])

    buttons = [[
        InlineKeyboardButton(text='Поехали', callback_data=ANSWER_1),
        InlineKeyboardButton(text='Идем дальше',
                             callback_data=ANSWER_5),
    ]]
    keyboard = InlineKeyboardMarkup(buttons)

    await update.callback_query.message.reply_text(text, reply_markup=keyboard)

    return BLOCK1_TEACHER_1


async def block1_teacher_1(update: Update, context: ContextTypes.DEFAULT_TYPE) -> str:
    query = update.callback_query
    await query.answer()

    if query.data == ANSWER_5:
        return await block1_teacher_7(update, context)

    text = '\n'.join([
        'На работе вы с удовольствием проводите онбординг для новичка, '
        'подробно объясняете процессы, помогаете вникнуть в задачи.',
        '',
        '1 — да / если бы была такая возможность, то так оно и было бы',
        '2 — нет, это мне не близко'
    ])

    buttons = [[
        InlineKeyboardButton(text='1', callback_data=ANSWER_1),
        InlineKeyboardButton(text='2', callback_data=ANSWER_2),
    ]]
    keyboard = InlineKeyboardMarkup(buttons)

    await update.callback_query.message.reply_text(text, reply_markup=keyboard)

    return BLOCK1_TEACHER_2


async def block1_teacher_2(update: Update, context: ContextTypes.DEFAULT_TYPE) -> str:
    query = update.callback_query
    await query.answer()

    context.user_data[USER_DATA_BLOCK1_TEACHER_QUIZ] = dict()
    context.user_data[USER_DATA_BLOCK1_TEACHER_QUIZ][LECTOR] = 1 if query.data == ANSWER_1 else 0

    text = '\n'.join([
        'Если вашему коллеге непонятна задача или он начинает вникать в '
        'совершенно в новую область и задаёт много вопросов, вы '
        'можете спокойно к этому отнестись и помочь разобраться.',
        '',
        '1 — да / если бы была такая возможность, то так оно и было бы',
        '2 — нет, это мне не близко'
    ])

    buttons = [[
        InlineKeyboardButton(text='1', callback_data=ANSWER_1),
        InlineKeyboardButton(text='2', callback_data=ANSWER_2),
    ]]
    keyboard = InlineKeyboardMarkup(buttons)

    await update.callback_query.message.reply_text(text, reply_markup=keyboard)

    return BLOCK1_TEACHER_3


async def block1_teacher_3(update: Update, context: ContextTypes.DEFAULT_TYPE) -> str:
    query = update.callback_query
    await query.answer()

    context.user_data[USER_DATA_BLOCK1_TEACHER_QUIZ][LECTOR] += 1 if query.data == ANSWER_1 else 0

    text = '\n'.join([
        'Когда коллеги обращаются к вам за обратной связью по их работе, вы отмечаете, '
        'что вам понравилось, а что можно было бы сделать по-другому. '
        'Вам нравится давать фидбэк, который помогает людям расти и развиваться.',
        '',
        '1 — да / если бы была такая возможность, то так оно и было бы',
        '2 — нет, это мне не близко'
    ])

    buttons = [[
        InlineKeyboardButton(text='1', callback_data=ANSWER_1),
        InlineKeyboardButton(text='2', callback_data=ANSWER_2),
    ]]
    keyboard = InlineKeyboardMarkup(buttons)

    await update.callback_query.message.reply_text(text, reply_markup=keyboard)

    return BLOCK1_TEACHER_4


async def block1_teacher_4(update: Update, context: ContextTypes.DEFAULT_TYPE) -> str:
    query = update.callback_query
    await query.answer()

    context.user_data[USER_DATA_BLOCK1_TEACHER_QUIZ][COACH] = 1 if query.data == ANSWER_1 else 0

    text = '\n'.join([
        'Если ваш коллега совершает ошибку, вы можете бережно помочь ему разобраться'
        ' в ситуации — понять, что к этой ошибке привело и что нужно сделать, чтобы исправить ситуацию.'
        '',
        '1 — да / если бы была такая возможность, то так оно и было бы',
        '2 — нет, это мне не близко'
    ])

    buttons = [[
        InlineKeyboardButton(text='1', callback_data=ANSWER_1),
        InlineKeyboardButton(text='2', callback_data=ANSWER_2),
    ]]
    keyboard = InlineKeyboardMarkup(buttons)

    await update.callback_query.message.reply_text(text, reply_markup=keyboard)

    return BLOCK1_TEACHER_5


async def block1_teacher_5(update: Update, context: ContextTypes.DEFAULT_TYPE) -> str:
    query = update.callback_query
    await query.answer()

    context.user_data[USER_DATA_BLOCK1_TEACHER_QUIZ][COACH] += 1 if query.data == ANSWER_1 else 0

    text = """Вам нравится обсуждать с друзьями или коллегами разные темы. Вы можете объяснить самое непонятное и сложное явление простыми словами, подобрать яркие примеры и аргументировать свою позицию.

1 — да / если бы была такая возможность, то так оно и было бы
2 — нет, это мне не близко"""

    buttons = [[
        InlineKeyboardButton(text='1', callback_data=ANSWER_1),
        InlineKeyboardButton(text='2', callback_data=ANSWER_2),
    ]]
    keyboard = InlineKeyboardMarkup(buttons)

    await update.callback_query.message.reply_text(text, reply_markup=keyboard)

    return BLOCK1_TEACHER_6


async def block1_teacher_6(update: Update, context: ContextTypes.DEFAULT_TYPE) -> str:
    query = update.callback_query
    await query.answer()

    context.user_data[USER_DATA_BLOCK1_TEACHER_QUIZ][AUTHOR] = 1 if query.data == ANSWER_1 else 0

    text = '\n'.join([
        'Вы пишете статьи или ведёте свой канал / блог о'
        ' профессиональной деятельности, где рассказываете о тонкостях профессии. '
        'Или задумывались о таком виде деятельности, потому что у вас классно'
        ' получается структурировать свои знания и есть желание делиться ими.',
        '',
        '1 — да / если бы была такая возможность, то так оно и было бы',
        '2 — нет, это мне не близко'
    ])

    buttons = [[
        InlineKeyboardButton(text='1', callback_data=ANSWER_1),
        InlineKeyboardButton(text='2', callback_data=ANSWER_2),
    ]]
    keyboard = InlineKeyboardMarkup(buttons)

    await update.callback_query.message.reply_text(text, reply_markup=keyboard)

    return BLOCK1_TEACHER_7


async def block1_teacher_7(update: Update, context: ContextTypes.DEFAULT_TYPE) -> str:
    query = update.callback_query
    await query.answer()

    if query.data in [ANSWER_1, ANSWER_2]:
        context.user_data[USER_DATA_BLOCK1_TEACHER_QUIZ][AUTHOR] += 1 if query.data == ANSWER_1 else 0

        teacher_quiz = context.user_data[USER_DATA_BLOCK1_TEACHER_QUIZ]
        if teacher_quiz[LECTOR] == teacher_quiz[COACH] == teacher_quiz[AUTHOR]:
            text = '\n'.join([
                f'Кажется, вам может быть интересна роль {LECTOR}а.',
                '   ',
                'В '
                'Нетологии лектор проводит лекции в реальном времени или записывает обучающие видео для студентов. '
                'Тренер '
                'или дипломный руководитель проверяет работы студентов и даёт развивающую обратную связь. Автор создаёт'
                'обучающий контент.',
                '   ',
                'Вы можете начать преподавать вместе с Нетологией – '
                'оставьте заявку по <a href="https://netology.ru/experts#contact">ссылке</a>.',
            ])
        else:
            most_favourite = max(teacher_quiz, key=teacher_quiz.get)
            least_favourite = min(teacher_quiz, key=teacher_quiz.get)
            text = '\n'.join([
                f'Кажется, вам может быть интересна роль <b>{most_favourite}а</b>.',
                f'Может быть роль <b>{least_favourite}а</b> будет вам не очень интересна.',
                '   ',
                'Все рекомендации условны. Если вам интересна любая роль '
                'или преподавание в целом – это замечательно! Стоит пробовать и поближе познакомиться с тем, '
                'что вам предстоит делать в рамках этих ролей.',
                '   ',
                'В Нетологии лектор проводит лекции в реальном времени '
                'или записывает обучающие видео для студентов. Тренер или дипломный руководитель проверяет работы '
                'студентов и даёт развивающую обратную связь. Автор создаёт обучающий контент.',
                '   ',
                'Вы можете начать '
                'преподавать вместе с Нетологией – '
                'оставьте заявку по <a href="https://netology.ru/experts#contact">ссылке</a>.',
            ])

        await context.bot.send_message(chat_id=update.effective_chat.id, text=text, disable_web_page_preview=True,
                                       parse_mode=ParseMode.HTML)

        await asleep(5)

    text = '\n'.join([
        'У нас есть несколько вариантов развития событий. ',
        '',
        'Первый: я могу рассказать о всём опыте преподавания поэтапно.'
        ' Как подготовиться к занятию, провести его, придумать классные '
        'домашки и дать развивающую обратную связь студентам. В конце поговорим'
        ' о том, что преподаватель — тоже человек, он может ошибаться и не знать всего '
        'на свете. Это нормально. Важно знать, как поддержать себя и не обесценивать свою экспертизу.'
        '',
        'Второй: могу рассказать только про конкретный аспект преподавания, '
        'который вам наиболее интересен. Например, про разработку контента или проведение занятия.',
        '   ',
        'По какому пути пойти — решать вам.',
    ])

    buttons = [[
        InlineKeyboardButton(text='Буду заканчивать курс', callback_data=ANSWER_1)
    ], [
        InlineKeyboardButton(text='К следующему этапу!', callback_data=ANSWER_2)
    ], [
        InlineKeyboardButton(text='Хочу выбрать сам', callback_data=ANSWER_3)
    ]]
    keyboard = InlineKeyboardMarkup(buttons)

    await update.callback_query.message.reply_text(text, reply_markup=keyboard)

    return BLOCK1_FINISH_1


block1_states = {

    BLOCK1_INTRO: [
        MessageHandler(filters.TEXT & ~filters.COMMAND, block1_intro)],
    BLOCK1_INTRODUCTION_SURNAME: [
        MessageHandler(filters.TEXT & ~filters.COMMAND, block1_introduction_surname)],
    BLOCK1_INTRODUCTION_EMAIL: [MessageHandler(filters.TEXT & ~filters.COMMAND, block1_introduction_email)],
    BLOCK1_INTRODUCTION_SPECIALITY: [
        MessageHandler(filters.TEXT & ~filters.COMMAND, block1_introduction_speciality)],
    BLOCK1_INTRODUCTION_LEVEL: [MessageHandler(filters.TEXT & ~filters.COMMAND, block1_introduction_level)],
    BLOCK1_INTRODUCTION_EXPECTATIONS: [CallbackQueryHandler(block1_introduction_expectations)],

    BLOCK1_INTRODUCTION_SUMMARY_1: [
        MessageHandler(filters.TEXT & ~filters.COMMAND, block1_introduction_summary_1)],
    BLOCK1_INTRODUCTION_SUMMARY_2: [CallbackQueryHandler(block1_introduction_summary_2)],
    BLOCK1_INTRODUCTION_SUMMARY_3: [CallbackQueryHandler(block1_introduction_summary_3)],
    BLOCK1_INTRODUCTION_SUMMARY_4: [CallbackQueryHandler(block1_introduction_summary_4)],

    BLOCK1_INTRODUCTION_ROLES_1: [
        CallbackQueryHandler(block1_introduction_roles_1, pattern=ANSWER_1),
        CallbackQueryHandler(block1_quiz_1, pattern=ANSWER_2),
    ],
    BLOCK1_INTRODUCTION_ROLES_2: [CallbackQueryHandler(block1_introduction_roles_2)],

    BLOCK1_QUIZ_1: [CallbackQueryHandler(block1_quiz_1)],
    BLOCK1_QUIZ_2: [CallbackQueryHandler(block1_quiz_2)],
    BLOCK1_QUIZ_3: [CallbackQueryHandler(block1_quiz_3)],
    BLOCK1_QUIZ_4: [CallbackQueryHandler(block1_quiz_4)],
    BLOCK1_QUIZ_5: [CallbackQueryHandler(block1_quiz_5)],
    BLOCK1_QUIZ_6: [CallbackQueryHandler(block1_quiz_6)],
    BLOCK1_QUIZ_7: [CallbackQueryHandler(block1_quiz_7)],
    BLOCK1_QUIZ_8: [CallbackQueryHandler(block1_quiz_8)],
    BLOCK1_QUIZ_9: [CallbackQueryHandler(block1_quiz_9)],
    BLOCK1_QUIZ_10: [CallbackQueryHandler(block1_quiz_10)],
    BLOCK1_QUIZ_11: [CallbackQueryHandler(block1_quiz_11)],
    BLOCK1_QUIZ_12: [CallbackQueryHandler(block1_quiz_12)],
    BLOCK1_QUIZ_13: [CallbackQueryHandler(block1_quiz_13)],
    BLOCK1_QUIZ_14: [CallbackQueryHandler(block1_quiz_14)],
    BLOCK1_QUIZ_15: [CallbackQueryHandler(block1_quiz_15)],
    BLOCK1_QUIZ_16: [CallbackQueryHandler(block1_quiz_16)],

    BLOCK1_STUDENT_1: [CallbackQueryHandler(block1_student_1)],
    BLOCK1_STUDENT_2: [CallbackQueryHandler(block1_student_2)],
    BLOCK1_STUDENT_3: [CallbackQueryHandler(block1_student_3)],
    BLOCK1_STUDENT_4: [CallbackQueryHandler(block1_student_4)],
    BLOCK1_STUDENT_5: [CallbackQueryHandler(block1_student_5)],
    BLOCK1_STUDENT_6: [CallbackQueryHandler(block1_student_6)],
    BLOCK1_STUDENT_7: [CallbackQueryHandler(block1_student_7)],
    BLOCK1_STUDENT_8: [CallbackQueryHandler(block1_student_8)],
    BLOCK1_STUDENT_9: [CallbackQueryHandler(block1_student_9)],
    BLOCK1_STUDENT_10: [CallbackQueryHandler(block1_student_10)],
    BLOCK1_STUDENT_11: [CallbackQueryHandler(block1_student_11)],
    BLOCK1_STUDENT_12: [CallbackQueryHandler(block1_student_12)],
    BLOCK1_STUDENT_13: [CallbackQueryHandler(block1_student_13)],
    BLOCK1_STUDENT_14: [CallbackQueryHandler(block1_student_14)],
    BLOCK1_STUDENT_15: [CallbackQueryHandler(block1_student_15)],
    BLOCK1_STUDENT_16: [CallbackQueryHandler(block1_student_16)],
    BLOCK1_STUDENT_17: [CallbackQueryHandler(block1_student_17)],
    BLOCK1_STUDENT_18: [CallbackQueryHandler(block1_student_18)],

    BLOCK1_TEACHER_1: [CallbackQueryHandler(block1_teacher_1)],
    BLOCK1_TEACHER_2: [CallbackQueryHandler(block1_teacher_2)],
    BLOCK1_TEACHER_3: [CallbackQueryHandler(block1_teacher_3)],
    BLOCK1_TEACHER_4: [CallbackQueryHandler(block1_teacher_4)],
    BLOCK1_TEACHER_5: [CallbackQueryHandler(block1_teacher_5)],
    BLOCK1_TEACHER_6: [CallbackQueryHandler(block1_teacher_6)],
    BLOCK1_TEACHER_7: [CallbackQueryHandler(block1_teacher_7)],

    BLOCK1_FINISH_1: [
        CallbackQueryHandler(block1_final, pattern=ANSWER_1),
        CallbackQueryHandler(block2_intro, pattern=ANSWER_2),
        CallbackQueryHandler(block1_finish_1, pattern=ANSWER_3),
    ],
    BLOCK1_FINISH_2: [
        CallbackQueryHandler(block2_intro, pattern=ANSWER_1),
        CallbackQueryHandler(block3_intro, pattern=ANSWER_2),
        CallbackQueryHandler(block4_intro, pattern=ANSWER_3),
        CallbackQueryHandler(block5_intro, pattern=ANSWER_4),
    ],

}
