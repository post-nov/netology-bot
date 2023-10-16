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

from blocks.intro import block2_intro, block3_intro, block4_intro, block5_intro
from blocks.block_finish import block1_final


async def block4_intro_1(update: Update, context: ContextTypes.DEFAULT_TYPE) -> str:
    query = update.callback_query
    await query.answer()

    text = '\n'.join([
        'Развивающая обратная связь формирует у человека ясное представление о его сильных сторонах, корректирует '
        'ошибки и подтягивает слабые стороны, задаёт направление дальнейших действий. Она возможна только тогда, '
        'когда <b>у участников образовательного процесса определены его цели</b>.',
        '  ',
        'Например, у студента есть цель — освоить '
        'анализ целевой аудитории, а у преподавателя — помочь студенту научиться анализировать её.',
    ])
    await context.bot.send_message(chat_id=update.effective_chat.id, text=text, disable_web_page_preview=True,
                                   parse_mode=ParseMode.HTML)

    await asleep(10)

    text = '\n'.join([
        '<b>Развивающая обратная связь:</b> ',
        '– указывает на положительные стороны, например, на количество верных ответов;',
        '– конструктивна, рекомендации помогают студенту улучшить результат; ',
        '– ориентирована на изменения в практике по сравнению с предыдущим результатом.',
        '  ',
        '<b>Неразвивающая обратная связь:</b> ',
        '– сосредоточена исключительно на неправильных ответах; ',
        '– не даёт информации и поддержки, студент не понимает, как улучшить результат; ',
        '– особое внимание уделяется сравнению людей друг с другом или оценкам и делению на уровни.',
    ])

    buttons = [[
        InlineKeyboardButton(text='Есть примеры?', callback_data=DUMMY),
    ]]
    keyboard = InlineKeyboardMarkup(buttons)

    await update.callback_query.message.reply_text(text, reply_markup=keyboard, disable_web_page_preview=True,
                                                   parse_mode=ParseMode.HTML)

    return BLOCK4_INTRO_2


async def block4_intro_2(update: Update, context: ContextTypes.DEFAULT_TYPE) -> str:
    query = update.callback_query
    await query.answer()

    text = '\n'.join([
        'Конечно! Например, мы даём обратную связь студенту Тане, которая выполняла домашнее задание по анализу '
        'целевой аудитории.',
        '   ',
        '<b>Неразвивающая обратная связь</b> ',
        'Таня, добрый день! Спасибо за выполненную работу. Ядро ЦА '
        'определено неверно, в остальном всё ок. ',
        'Переделайте, пожалуйста.',
    ])
    await context.bot.send_message(chat_id=update.callback_query.message.chat_id, text=text, parse_mode=ParseMode.HTML)
    await asleep(5)
    text = '\n'.join([
        '<b>Развивающая обратная связь</b> ',
        'Таня, добрый день! ',
        'Спасибо за выполненную работу. ',
        'У вас отлично получилось определить и сегментировать ЦА. ',
        'Хочется, чтобы вы сосредоточились на ядре целевой аудитории — его можно определить точнее. Попробуйте '
        'ответить на вопросы: ',
        '1. Кто чаще всего пользуется продуктом? ',
        '2. Кто принесёт больше всего прибыли? После '
        'ответа на них вы можете пересмотреть ядро ЦА. Это поможет сделать маркетинговую стратегию более точной и '
        'эффективной.',
        '   ',
        'Как думаете, после какой обратной связи Тане захочется продолжить обучение?',
    ])

    buttons = [
        [InlineKeyboardButton(text='Развивающей', callback_data=ANSWER_1)],
        [InlineKeyboardButton(text='Неразвивающей', callback_data=ANSWER_2)],
    ]
    keyboard = InlineKeyboardMarkup(buttons)

    await update.callback_query.message.reply_text(text, reply_markup=keyboard, disable_web_page_preview=True,
                                                   parse_mode=ParseMode.HTML)

    return BLOCK4_INTRO_4


async def block4_intro_3_1(update: Update, context: ContextTypes.DEFAULT_TYPE) -> str:
    query = update.callback_query
    await query.answer()

    if query.data == ANSWER_1:
        text = '\n'.join([
            'Тоже так считаю! Развивающая обратная связь:',
            '– помогает студенту справиться со страхом совершать ошибки, ',
            'делать что-то неправильно, тем самым делает процесс обучения более комфортным; ',
            '– показывает зоны роста и '
            'даёт конкретные рекомендации, которые позволяют эффективнее учиться, достичь своей цели; ',
            '– поддерживает '
            'мотивацию к обучению; – помогает учиться, снижает сопротивление к доработке задания.',
            '  ',
            'Есть алгоритм, '
            'который помогает преподавателю дать развивающую обратную связь.',
        ])
    else:
        text = '\n'.join([
            'Я всё-таки склоняюсь к тому, что после развивающей обратной связи. По моему опыту, она: ',
            '– помогает '
            'студенту справиться со страхом совершать ошибки, делать что-то неправильно, тем самым делает процесс '
            'обучения более комфортным; ',
            '– показывает зоны роста и даёт конкретные рекомендации, которые позволяют '
            'эффективнее учиться, достичь своей цели; ',
            '– поддерживает мотивацию к обучению;',
            '– помогает учиться, '
            'снижает сопротивление к доработке задания.',
            '  ',
            'Есть алгоритм, который помогает преподавателю дать '
            'развивающую обратную связь.',
        ])
    await context.bot.send_message(chat_id=update.callback_query.message.chat_id, text=text, parse_mode=ParseMode.HTML)

    await asleep(10)

    await context.bot.copy_message(chat_id=update.effective_chat.id, from_chat_id=MEDIA_CHANNEL_ID,
                                   message_id=MEDIA_PHOTO_10)

    text = '\n'.join([
        '<b>Шаг первый</b> — поздоровайтесь со студентом, если знаете имя, обратитесь по имени.',
        '',
        '<b>Шаг второй</b> — поблагодарите за работу. Помните, что обучение — это труд, и работа студента — результат этого '
        'труда. То, что для преподавателя может быть очевидным, для студента может оказаться сложной задачкой.',
        '   ',
        '<b>Шаг третий</b> — выделите положительные моменты в работе.',
        '   ',
        '<b>Шаг четвёртый</b> — скажите, что стоит улучшить в работе и '
        'каким образом. Важно! Не давайте студенту готовых решений или ответов. Направьте его советом, но не лишайте '
        'возможности самостоятельно найти ответ.',
        '   ',
        '<b>Шаг пятый</b> — опишите, как доработка задания повлияет на результат.',
    ])

    buttons = [[
        InlineKeyboardButton(text='А что делать, если в работе всё-всё идеально?',
                             callback_data=DUMMY),
    ]]
    keyboard = InlineKeyboardMarkup(buttons)

    await update.callback_query.message.reply_text(text, reply_markup=keyboard, disable_web_page_preview=True,
                                                   parse_mode=ParseMode.HTML)

    return BLOCK4_INTRO_3


async def block4_intro_3(update: Update, context: ContextTypes.DEFAULT_TYPE) -> str:
    query = update.callback_query
    await query.answer()

    text = '\n'.join([
        'Отличный вопрос!  ',
        'Обычно я в таких ситуациях даю общий комментарий, что работа выполнена здорово и очень '
        'профессионально. После отмечаю особенно удачные моменты.',
        '    ',
        'Если всё-таки у работы есть потенциал улучшения, '
        'который выходит за рамки задания, я прямо говорю это студенту. Что-то в роде: «Это не входит в задание, '
        'но если вам интересно, то можно было бы сделать ещё вот так. Подробнее об этом можно почитать здесь и '
        'посмотреть тут». Прикрепляю ссылки на материалы.',
    ])
    await context.bot.send_message(chat_id=update.callback_query.message.chat_id, text=text, parse_mode=ParseMode.HTML)
    await asleep(5)
    text = '\n'.join([
        'Если это невозможно, то просто предлагаю студенту '
        'изучить дополнительные материалы по теме: статьи, книги, интересные блоги.',
        '   ',
        ' В конце добавляю что-то, '
        'что может поддержать на сложном пути обучения. Например, «у вас отличный прогресс, рад за вас» или «успехов '
        'на курсе, у вас всё отлично получается».',
    ])

    buttons = [[
        InlineKeyboardButton(text='Если у студента много вопросов?',
                             callback_data=DUMMY),
    ]]
    keyboard = InlineKeyboardMarkup(buttons)

    await update.callback_query.message.reply_text(text, reply_markup=keyboard, disable_web_page_preview=True,
                                                   parse_mode=ParseMode.HTML)

    return BLOCK4_INTRO_5


async def block4_intro_4(update: Update, context: ContextTypes.DEFAULT_TYPE) -> str:
    query = update.callback_query
    await query.answer()

    text = '\n'.join([
        'Бывает, что даже после развивающей обратной связи у студента остаются вопросы. Вы на них отвечаете, '
        'но кажется, что студенту это не помогает. Начинает накапливаться раздражение и усталость.',
        '   ',
        'Как обычно поступаю я?',
        '   ',
        'Сначала выполняю три привычных шага в любой ситуации, когда есть какой-то негатив или '
        'сопротивление. Они актуальны как для взаимодействия в режиме реального времени, например, на занятии, '
        'так же подходят и для письменной коммуникации.',
        '   ',
    ])
    await context.bot.send_message(chat_id=update.callback_query.message.chat_id, text=text, parse_mode=ParseMode.HTML)
    await asleep(5)
    text = '\n'.join([
        'Первый — выдохнуть и взять эмоции под контроль. ',
        'Второй — '
        'присоединиться, дать понять студенту, что я его слышу. Например, «мне жаль, что это произошло», «понимаю, '
        'вы потратили много времени» и т. д. ',
        'Третий — сфокусировать студента на рациональном. Говорю, '
        'что готов помочь разобраться и для этого мне нужно получить больше информации, если её недостаточно. В чём '
        'именно сложность, проблема? Почему не получается её решить? Что уже было сделано для решения?',
        '   ',
        'С одной '
        'стороны, это помогает мне лучше понять ситуацию и предложить оптимальное решение, с другой стороны, '
        'помогает студенту структурировать в голове всю информацию, проследить последовательность своих действий. '
        'Возможно, на этом этапе вопрос решится.',
    ])

    buttons = [[
        InlineKeyboardButton(text='А если вопрос не решился?',
                             callback_data=DUMMY),
    ]]
    keyboard = InlineKeyboardMarkup(buttons)

    await update.callback_query.message.reply_text(text, reply_markup=keyboard, disable_web_page_preview=True,
                                                   parse_mode=ParseMode.HTML)

    return BLOCK4_INTRO_6


async def block4_intro_5(update: Update, context: ContextTypes.DEFAULT_TYPE) -> str:
    query = update.callback_query
    await query.answer()

    text = '\n'.join([
        'Тогда предлагаю различные варианты развития событий. Например: ',
        '– обратиться к похожему заданию и сделать '
        'его, чтобы переключиться; ',
        '– ещё раз попробовать выполнить задание и фиксировать все вопросы, '
        'которые возникают по ходу его выполнения; ',
        '– посоветовать дополнительные материалы, которые помогут '
        'разобраться в теме; ',
        '– попробовать обратиться к одногруппникам, если они есть, или в профессиональное '
        'сообщество; ',
        '– если это возможно, отправить голосовое сообщение с пояснениями или записать скрин экрана.',
    ])
    await context.bot.send_message(chat_id=update.callback_query.message.chat_id, text=text, parse_mode=ParseMode.HTML)
    await asleep(5)
    text = '\n'.join([
        'Вариантов может быть много, главное, чтобы они были приемлемы и для студента, и для вас. Будет здорово, '
        'если вы заранее узнаете, какой «арсенал» решений у вас есть. Например, готовы ли вы будете записать '
        'поясняющее видео или предложить другое задание? Может быть в компании, в которой вы преподаёте, '
        'есть возможность обратиться за помощью в таких ситуациях?',
        '   ',
        'Используйте любые доступные вам решения и '
        'постарайтесь искренне помочь студенту :)',
    ])

    buttons = [[
        InlineKeyboardButton(text='Буду пробовать!',
                             callback_data=DUMMY),
    ]]
    keyboard = InlineKeyboardMarkup(buttons)

    await update.callback_query.message.reply_text(text, reply_markup=keyboard, disable_web_page_preview=True,
                                                   parse_mode=ParseMode.HTML)

    return BLOCK4_INTRO_7


async def block4_intro_6(update: Update, context: ContextTypes.DEFAULT_TYPE) -> str:
    query = update.callback_query
    await query.answer()

    text = '\n'.join([
        'Здорово!',
        '   ',
        'Мы обсудили, как дать студенту развивающую обратную связь. Можем потренироваться на кейсах.',
        '   ',
        'Я '
        'покажу вам обратную связь на несколько работ. Вы определите, что в этой обратной связи здорово, а что можно '
        'было бы сделать по-другому.',
    ])

    buttons = [[
        InlineKeyboardButton(text='Поехали!',
                             callback_data=DUMMY),
    ]]
    keyboard = InlineKeyboardMarkup(buttons)

    await update.callback_query.message.reply_text(text, reply_markup=keyboard, disable_web_page_preview=True,
                                                   parse_mode=ParseMode.HTML)

    return BLOCK4_INTRO_8


async def block4_intro_7(update: Update, context: ContextTypes.DEFAULT_TYPE) -> str:
    query = update.callback_query
    await query.answer()

    text = '\n'.join([
        'Кейс 1',
        '   ',
        'Юлия, добрый день!',
        '   ',
        'Спасибо за проделанную работу и ваши идеи. У вас есть правильные и интересные '
        'мысли, но сейчас работе не хватает структурности.',
        '   ',
        '1. Выпишите не менее 10 параметров списком. ',
        '2. '
        'Сформулируйте чёткую стратегическую цель и подумайте, какие параметры лучше всего помогут вам сегментировать '
        'аудиторию для этой цели. Выпишите эти параметры (их будет не больше 1–2) и опишите пару примеров сегментов '
        'по ним.',
        '   ',
        'Всего доброго!',
        '   ',
        '<b>Что в этой обратной связи здорово, а что можно было бы сделать по-другому?</b> ',
        'Напишите ответ одним сообщением.',
    ])

    await update.callback_query.message.reply_text(text, disable_web_page_preview=True, parse_mode=ParseMode.HTML)

    return BLOCK4_INTRO_9


async def block4_intro_8(update: Update, context: ContextTypes.DEFAULT_TYPE) -> str:
    context.user_data[USER_DATA_BLOCK4_CASE_1] = update.message.text

    text = '\n'.join([
        'Кейс 1',
        '   ',
        '<b>Что было здорово:</b> ',
        '– обращение по имени и приветствие; ',
        '– благодарность за работу; ',
        '– есть положительная обратная связь на мысли студента; ',
        '– конкретные шаги, которые помогут улучшить работу.',
        '   ',
        '<b>Что можно улучшить:</b> ',
        '– отметить, какие именно мысли правильные и интересные;',
        '– уточнить, по какому методу или принципу можно сформулировать стратегическую цель, чтобы она была чёткой; ',
        '– уточнить, почему 1–2 параметра получится в итоге; ',
        '– объяснить, как после этих шагов изменится результат, чему это поможет; ',
        '– в конце ещё раз поддержать студента.',
    ])

    buttons = [[
        InlineKeyboardButton(text='Второй кейс в студию!', callback_data=DUMMY),
    ]]
    keyboard = InlineKeyboardMarkup(buttons)
    await update.message.reply_text(text, reply_markup=keyboard, disable_web_page_preview=True,
                                    parse_mode=ParseMode.HTML)

    return BLOCK4_INTRO_10


async def block4_intro_9(update: Update, context: ContextTypes.DEFAULT_TYPE) -> str:
    query = update.callback_query
    await query.answer()

    text = '\n'.join([
        'Кейс 2',
        '   ',
        'Иван, добрый день!',
        '   ',
        'Великолепный баннер! Полное попадание по всем пунктам технического задания. Вы очень аккуратно заменили '
        'телефон у девушки. Здорово, что вы сделали описание для заказчика — для дизайнера навык аргументировать свои '
        'решения очень важен.',
        '    ',
        'Вы проделали великолепную работу!',
        '   ',
        '<b>Что в этой обратной связи здорово, а что можно было бы сделать по-другому?</b> ',
        'Напишите ответ одним сообщением.',
    ])

    await update.callback_query.message.reply_text(text, disable_web_page_preview=True, parse_mode=ParseMode.HTML)

    return BLOCK4_INTRO_11


async def block4_intro_10(update: Update, context: ContextTypes.DEFAULT_TYPE) -> str:
    context.user_data[USER_DATA_BLOCK4_CASE_2] = update.message.text

    text = '\n'.join([
        'Кейс 2',
        '   ',
        '<b>Что было здорово:</b> ',
        '– обращение по имени и приветствие; ',
        '– отмечено, почему именно работа хорошая, '
        'что получилось отлично; ',
        '– есть связка с реальными рабочими задачами: навык аргументации важен в работе с '
        'клиентом; ',
        '– в конце ещё раз поддержали студента и дали общую высокую оценку работе.',
        '   ',
        '<b>Что можно улучшить:</b> ',
        '– '
        'поблагодарить студента за работу; ',
        '– дать дополнительные материалы по теме.',
    ])

    buttons = [[
        InlineKeyboardButton(text='Последний кейс', callback_data=DUMMY),
    ]]
    keyboard = InlineKeyboardMarkup(buttons)
    await update.message.reply_text(text, reply_markup=keyboard, disable_web_page_preview=True,
                                    parse_mode=ParseMode.HTML)

    return BLOCK4_INTRO_12


async def block4_intro_11(update: Update, context: ContextTypes.DEFAULT_TYPE) -> str:
    query = update.callback_query
    await query.answer()

    text = '\n'.join([
        'Кейс 3',
        '   ',
        'Илья, добрый день!',
        '   ',
        'Получилась очень интересная анимация. Понравилось и сама анимация, и то, '
        'что мячик крутится, когда его сдувает ветер.  Вот как это происходит в классической анимации: при падении '
        'мячик вертикально растягивается, упал — сплющился, отскочил — растянулся, достиг наивысшей точки, '
        'восстановив свои размеры. Не забывайте соблюдать законы анимации, в том числе и сохранение объёмов: если по '
        'одной оси объект изменился, то и по другой он пропорционально изменится.',
        '   ',
        'Изучите ещё вот этот урок, '
        'в нём показаны очень хорошие техники для работы с шейповой анимацией (ссылка на урок).',
        '   ',
        'По анимации текста '
        'посмотрите вот эти уроки (ссылка на уроки).',
        '   ',
        '<b>Что в этой обратной связи здорово, а что можно было бы сделать по-другому?</b> ',
        'Напишите ответ одним сообщением.',
    ])

    await update.callback_query.message.reply_text(text, disable_web_page_preview=True, parse_mode=ParseMode.HTML)

    return BLOCK4_INTRO_13


async def block4_intro_12(update: Update, context: ContextTypes.DEFAULT_TYPE) -> str:
    context.user_data[USER_DATA_BLOCK4_CASE_3] = update.message.text

    text = '\n'.join([
        'Кейс 3',
        '   ',
        '<b>Что было здорово:</b>',
        ' – обращение по имени и приветствие; ',
        '– отмечено, почему именно работа хорошая, что получилось отлично; ',
        '– есть развернутый комментарий от эксперта по тому, как работает анимация; ',
        '– есть рекомендации, на что обратить внимание; – есть дополнительные материалы по теме.',
        '   ',
        '<b>Что можно улучшить:</b> ',
        '– поблагодарить студента за работу; ',
        '– сделать больше акцента на том, что и как именно можно улучшить, с помощью каких приёмов; ',
        '– рассказать, как это отразится на результате; в конце ещё раз поддержать студента '
        'или пожелать успехов.',
    ])

    await context.bot.send_message(chat_id=update.effective_chat.id, text=text, disable_web_page_preview=True,
                                   parse_mode=ParseMode.HTML)

    await asleep(10)

    text = '\n'.join([
        'Спасибо за решение кейсов! Классная тренировка получилась.',
        ' ',
        '<b>Подведём короткий итог.</b>',
        'Для проверки домашних заданий важно: ',
        '– давать развивающую обратную связь студенту; ',
        '– поддержать его мотивацию к обучению; ',
        '– помочь '
        'разобраться с любым вопросом по заданию.',
        '   ',
        'Поделитесь, пожалуйста, что для вас было интересно узнать про '
        'проверку заданий?',
        'Напишите ответ одним сообщением.',
    ])

    await update.message.reply_text(text, disable_web_page_preview=True, parse_mode=ParseMode.HTML)

    return BLOCK4_INTRO_14


async def block4_intro_13(update: Update, context: ContextTypes.DEFAULT_TYPE) -> str:
    context.user_data[USER_DATA_BLOCK4_THOUGHTS] = update.message.text

    text = '\n'.join([
        'А что вы уже знали и использовали в работе?',
    ])

    await update.message.reply_text(text, disable_web_page_preview=True, parse_mode=ParseMode.HTML)

    return BLOCK4_FINISH_1


async def block4_finish_1(update: Update, context: ContextTypes.DEFAULT_TYPE) -> str:
    text = '\n'.join([
        'Отлично, можем двигаться дальше! Переходим к блоку преподаватель тоже человек? '
        'Или хотите посмотреть все разделы и выбрать подходящий?',
    ])

    buttons = [[
        InlineKeyboardButton(text='К следующему этапу!', callback_data=ANSWER_1),
    ], [
        InlineKeyboardButton(text='Хочу посмотреть все блоки и выбрать', callback_data=ANSWER_2),
    ], [
        InlineKeyboardButton(text='Буду заканчивать курс', callback_data=ANSWER_3)
    ]]
    keyboard = InlineKeyboardMarkup(buttons)

    await update.message.reply_text(text, reply_markup=keyboard)

    return BLOCK4_FINISH_2


async def block4_finish_2(update: Update, context: ContextTypes.DEFAULT_TYPE) -> str:
    query = update.callback_query
    await query.answer()

    text = '\n'.join([
        'Что выберем?',
    ])

    buttons = [[
        InlineKeyboardButton(text='Готовимся к занятию', callback_data=ANSWER_1),
    ], [
        InlineKeyboardButton(text='Проводим занятие', callback_data=ANSWER_2),
        InlineKeyboardButton(text='Преподаватель тоже человек!', callback_data=ANSWER_3),
    ]]
    keyboard = InlineKeyboardMarkup(buttons)

    await update.callback_query.message.reply_text(text, reply_markup=keyboard)

    return BLOCK4_FINISH_2

block4_states = {

    BLOCK4_INTRO: [CallbackQueryHandler(block4_intro)],
    BLOCK4_INTRO_1: [CallbackQueryHandler(block4_intro_1)],
    BLOCK4_INTRO_2: [CallbackQueryHandler(block4_intro_2)],
    BLOCK4_INTRO_3: [CallbackQueryHandler(block4_intro_3)],
    BLOCK4_INTRO_4: [CallbackQueryHandler(block4_intro_3_1)],
    BLOCK4_INTRO_5: [CallbackQueryHandler(block4_intro_4)],
    BLOCK4_INTRO_6: [CallbackQueryHandler(block4_intro_5)],
    BLOCK4_INTRO_7: [CallbackQueryHandler(block4_intro_6)],
    BLOCK4_INTRO_8: [CallbackQueryHandler(block4_intro_7)],
    BLOCK4_INTRO_9: [MessageHandler(filters.TEXT & ~filters.COMMAND, block4_intro_8)],
    BLOCK4_INTRO_10: [CallbackQueryHandler(block4_intro_9)],
    BLOCK4_INTRO_11: [MessageHandler(filters.TEXT & ~filters.COMMAND, block4_intro_10)],
    BLOCK4_INTRO_12: [CallbackQueryHandler(block4_intro_11)],
    BLOCK4_INTRO_13: [MessageHandler(filters.TEXT & ~filters.COMMAND, block4_intro_12)],
    BLOCK4_INTRO_14: [MessageHandler(filters.TEXT & ~filters.COMMAND, block4_intro_13)],

    BLOCK4_FINISH_1: [MessageHandler(filters.TEXT & ~filters.COMMAND, block4_finish_1)],
    BLOCK4_FINISH_2: [
        CallbackQueryHandler(block5_intro, pattern=ANSWER_1),
        CallbackQueryHandler(block4_finish_2, pattern=ANSWER_2),
        CallbackQueryHandler(block1_final, pattern=ANSWER_3),
    ],
    BLOCK4_FINISH_3: [
        CallbackQueryHandler(block2_intro, pattern=ANSWER_1),
        CallbackQueryHandler(block3_intro, pattern=ANSWER_2),
        CallbackQueryHandler(block5_intro, pattern=ANSWER_3),
    ],
}