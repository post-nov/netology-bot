from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.constants import ParseMode
from telegram.ext import (
    CallbackQueryHandler,
    ContextTypes,
    MessageHandler,
    filters,
)

from blocks.intro import block2_intro, block3_intro, block4_intro, block5_intro
from blocks.block_finish import block1_final

from constants import *
from utils import asleep


async def block2_intro_1(update: Update, context: ContextTypes.DEFAULT_TYPE) -> str:
    query = update.callback_query
    await query.answer()

    text = '\n'.join([
        'Давайте разберёмся с подводной частью нашего айсберга. Как вы думаете, с чего лучше начать?',
        '   ',
        '1 – составить презентацию. ',
        '2 – поставить цель на занятие. ',
        '3 – понять целевую аудиторию. ',
        '4 – определиться с форматом.',
    ])

    buttons = [[
        InlineKeyboardButton(text='1', callback_data=ANSWER_1),
        InlineKeyboardButton(text='2', callback_data=ANSWER_2),
        InlineKeyboardButton(text='3', callback_data=ANSWER_3),
        InlineKeyboardButton(text='4', callback_data=ANSWER_4),
    ]]
    keyboard = InlineKeyboardMarkup(buttons)

    await update.callback_query.message.reply_text(text, reply_markup=keyboard)

    return BLOCK2_INTRO_2


async def block2_intro_2(update: Update, context: ContextTypes.DEFAULT_TYPE) -> str:
    query = update.callback_query
    await query.answer()

    if query.data == ANSWER_3:
        text = '\n'.join([
            'Верно! Начать подготовку лучше всего с понимания целевой аудитории курса или занятия. ',
            'Нужно понимать, для кого предназначается курс или занятие, и ответить на вопросы:',
            '– кто эти люди — возраст, профессия, география, интересы;',
            '– какие знания и опыт работы по теме они уже имеют.',
            '   ',
            'Это позволит грамотно подобрать для студентов материал.',
        ])
    else:
        text = '\n'.join([
            '<b>Начать подготовку лучше всего с понимания целевой аудитории курса или занятия.</b>',
            ' ',
            'Нужно понимать, для кого предназначается курс или занятие, и ответить на вопросы:',
            '– кто эти люди — возраст, профессия, география, интересы;',
            '– какие знания и опыт работы по теме они уже имеют.',
            '   ',
            'Это позволит грамотно подобрать для студентов материал. '
            'Согласитесь, человеку, который никогда не слышал, что такое инвестиции, будет сложно отличить облигации '
            'от акций. Поэтому не стоит сыпать терминами и нужно начать с азов. Если публика подготовлена, '
            'слушателям может быть скучно разбираться в основах.',
        ])

    await context.bot.send_message(chat_id=update.effective_chat.id, text=text, disable_web_page_preview=True,
                                   parse_mode=ParseMode.HTML)

    await asleep(10)

    text = '\n'.join([
        'Понимание аудитории также позволит грамотно подобрать формат подачи информации, насколько можно опираться на '
        'опыт участников, использовать профессиональный сленг.',
        '   ',
        'Также рекомендую узнать заранее и объём аудитории, '
        'и, возможно, мотивацию студентов к обучению.',
        '   ',
        'Представьте: вас просят провести мозговой штурм для решения '
        'сложного профессионального кейса. Вы думаете, что будете работать в общей конференции и в одиночку '
        'смодерируете участников, а оказывается, что их 70 человек. В таком случае изначальный план точно нужно '
        'корректировать.',
    ])

    buttons = [[
        InlineKeyboardButton(text='Буду узнавать аудиторию заранее', callback_data=DUMMY),
    ]]
    keyboard = InlineKeyboardMarkup(buttons)

    await update.callback_query.message.reply_text(text, reply_markup=keyboard)

    return BLOCK2_INTRO_3


async def block2_intro_3(update: Update, context: ContextTypes.DEFAULT_TYPE) -> str:
    query = update.callback_query
    await query.answer()

    text = '\n'.join([
        'Отлично! Когда вы представили вашу аудиторию, приступать к написанию занятия всё ещё рановато.',
        '   ',
        'Если вы '
        'ведете занятие в рамках курса, важно узнать его программу, чтобы:',
        '– понимать содержание курса и знания, которые получают студенты на каждом его этапе;',
        '– знать контекст, в который встроена ваша лекция: о чём '
        'говорили спикеры до вас и о чём будут говорить потом;',
        '– знать расписание, дедлайны, домашнее задание;',
        '– понимать, к какому результату должно привести обучение',
    ])

    buttons = [[
        InlineKeyboardButton(text='А как это работает на практике?', callback_data=DUMMY),
    ]]
    keyboard = InlineKeyboardMarkup(buttons)

    await update.callback_query.message.reply_text(text, reply_markup=keyboard)

    return BLOCK2_INTRO_4


async def block2_intro_4(update: Update, context: ContextTypes.DEFAULT_TYPE) -> str:
    query = update.callback_query
    await query.answer()

    text = '\n'.join([
        'Давайте попробуем посмотреть на примерах. Вы получаете такое предложение.',
        '   ',
        '«Привет! Нам нужно через неделю '
        'провести вебинар по основам Python. Времени всего 1,5 часа. Целевая аудитория — школьники 8–11 классов. '
        'Сможете взяться?»',
        '  ',
        'Что ответим?',
    ])

    buttons = [
        [InlineKeyboardButton(text='Да, конечно', callback_data=ANSWER_1)],
        [InlineKeyboardButton(text='Хочу уточнить пару моментов', callback_data=ANSWER_2)],
    ]
    keyboard = InlineKeyboardMarkup(buttons)

    await update.callback_query.message.reply_text(text, reply_markup=keyboard)

    return BLOCK2_INTRO_5


async def block2_intro_5(update: Update, context: ContextTypes.DEFAULT_TYPE) -> str:
    query = update.callback_query
    await query.answer()

    if query.data == ANSWER_1:
        text = '\n'.join([
            'Кажется, этой информации недостаточно. Лучше задать несколько уточняющих вопросов.',
            '   ',
            'Какие вопросы вы бы задали, чтобы получить больше информации? Напишите одним сообщением.',
        ])
    else:
        text = """Верно. Чтобы на лекции не было трудностей, лучше уточнить все вопросы на берегу.

Какие вопросы вы бы задали, чтобы получить больше информации? Напишите одним сообщением."""

    await update.callback_query.message.reply_text(text)

    return BLOCK2_INTRO_6


async def block2_intro_5_1(update: Update, context: ContextTypes.DEFAULT_TYPE) -> str:
    context.user_data[USER_DATA_BLOCK2_POSSIBLE_ANSWER_1] = update.message.text

    text = '\n'.join([
        'Спасибо за ответ. Уверен, ваши вопросы  сделали картинку яснее.',
        '   ',
        'Обычно я задаю такие вопросы. ',
        '1. В рамках '
        'какого курса или мероприятия проводится занятие? Является ли занятие единственным или оно встроено в '
        'программу? ',
        '2. С какой целью проводится занятие? Какой результат вы хотите получить по итогам вебинара? И как '
        'вы планируете проверять его достижение? ',
        '3. В каком формате будет проходить занятие? ',
        '4. Сколько человек '
        'участвует? Есть ли какие-то базовые знания у аудитории? ',
        '5. Что именно вы хотите от меня получить – нужно ли '
        'готовить презентацию, план занятия, подробный сценарий? Буду ли я взаимодействовать с кем-то из вашей '
        'команды – например, методистом, дизайнером, редактором?',
        '   ',
        'Как думаете, важно задавать вопросы про цель и '
        'результат занятия и программы?',
    ])

    buttons = [
        [InlineKeyboardButton(text='Да, это важно', callback_data=ANSWER_1)],
        [InlineKeyboardButton(text='Если мало времени, не важно', callback_data=ANSWER_2)],
    ]
    keyboard = InlineKeyboardMarkup(buttons)

    await update.message.reply_text(text, reply_markup=keyboard)

    return BLOCK2_INTRO_7


async def block2_intro_5_2(update: Update, context: ContextTypes.DEFAULT_TYPE) -> str:
    query = update.callback_query
    await query.answer()

    if query.data == ANSWER_1:
        text = '\n'.join([
            'Согласен! Цель — это та заветная точка Б, к которой придёт студент после занятия. Чёткое понимание цели '
            'позволит сформулировать чёткий образовательный результат. Зная, к чему вам необходимо привести '
            'студентов, вы сможете качественнее построить занятие и убрать лишнее.'
        ])
    else:
        text = '\n'.join([
            'Все-таки понять цель важно. Это та заветная точка Б, к которой придёт студент после занятия. Чёткое '
            'понимание цели позволит сформулировать чёткий образовательный результат. Зная, к чему вам необходимо '
            'привести студентов, вы сможете качественнее построить занятие и убрать лишнее.'
        ])

    buttons = [[
        InlineKeyboardButton(text='Как его сформулировать?', callback_data=DUMMY),
    ]]
    keyboard = InlineKeyboardMarkup(buttons)

    await update.callback_query.message.reply_text(text, reply_markup=keyboard)

    return BLOCK2_INTRO_8


async def block2_intro_6(update: Update, context: ContextTypes.DEFAULT_TYPE) -> str:
    query = update.callback_query
    await query.answer()

    await context.bot.copy_message(chat_id=update.effective_chat.id, from_chat_id=MEDIA_CHANNEL_ID,
                                   message_id=MEDIA_PHOTO_6)

    text = '\n'.join([
        'Существуют разные подходы к постановке образовательных результатов. Я хочу познакомить вас с таксономией '
        'Блума. Американский психолог Бенджамин Блум создал систему, которая помогает структурировать процесс '
        'обучения и выявить, измерить и оценить уровень знаний, умений и навыков у обучающихся.',
        '   ',
        'Итак, таксономия '
        'Блума – это система образовательных целей, которая строится от простого к сложному, изображается в виде '
        'пирамиды.',
    ])

    buttons = [[
        InlineKeyboardButton(text='Подробнее про каждый уровень?', callback_data=DUMMY),
    ]]
    keyboard = InlineKeyboardMarkup(buttons)

    await update.callback_query.message.reply_text(text, reply_markup=keyboard)

    return BLOCK2_INTRO_9


async def block2_intro_7(update: Update, context: ContextTypes.DEFAULT_TYPE) -> str:
    query = update.callback_query
    await query.answer()

    text = '\n'.join([
        'Конечно!',
        '  ',
        'В основе прирамиды самый простой уровень образовательных целей – знание. На нем студент может '
        'запомнить и воспроизвести полученный материал. На этом уровне мы просим студента решить тест, '
        'соотнести термин и его определения.',
        '   ',
        'Вторая ступень более сложная – понимание. На этом этапе студент '
        'понимает материал и может его интерпретировать. Например, рассказать своими словами, сравнить, '
        'привести примеры.',
        '    ',
        'Третья ступень – применение. Студент может применять полученные знания на практике. Он '
        'может выполнить какую-либо задачу или решить кейс.',
    ])

    await context.bot.send_message(chat_id=update.effective_chat.id, text=text)

    await asleep(10)

    text = """<b>Четвертая ступень</b> – анализ. Если студенты достигли этой ступени, они могут разбить понятие или явление на составляющие части, структурировать его, понимать взаимосвязи этих частей. Здесь студент может структурировать, определить отличия и сходства, соотнести теорию с ее применением на практике.

<b>Пятая ступень</b> – синтез. Здесь студент должен научиться комбинировать, создавать идеи и концепции с помощью группировки, обобщения, планирования. Например, это может быть статья или доклад.

Последняя <b>шестая ступень</b> – оценка. Студенты могут не просто создать новое, а оценить / вынести суждения об идеях или методах, аргументировать свою позицию."""

    buttons = [[
        InlineKeyboardButton(text='Как студент движется по ступеням?', callback_data=DUMMY),
    ]]
    keyboard = InlineKeyboardMarkup(buttons)

    await update.callback_query.message.reply_text(text, reply_markup=keyboard, parse_mode=ParseMode.HTML)

    return BLOCK2_INTRO_10


async def block2_intro_8(update: Update, context: ContextTypes.DEFAULT_TYPE) -> str:
    query = update.callback_query
    await query.answer()

    text = '\n'.join([
        'Отличный вопрос! Студент двигается в обучении постепенно, он не может со ступени знания сразу перескочить на '
        'применение.',
        '   ',
        'Важно проходить все этапы последовательно. Поэтому при разработке занятия полезно понимать, '
        'до какой ступени согласно таксономии Блума мы хотим довести студента и какой у него изначальный уровень. '
        'Согласно тому, до какой ступени сможет дойти студент, мы формируем и учебную цель.',
    ])

    buttons = [[
        InlineKeyboardButton(text='Можно примеры?', callback_data=DUMMY),
    ]]
    keyboard = InlineKeyboardMarkup(buttons)

    await update.callback_query.message.reply_text(text, reply_markup=keyboard)

    return BLOCK2_INTRO_11


async def block2_intro_9(update: Update, context: ContextTypes.DEFAULT_TYPE) -> str:
    query = update.callback_query
    await query.answer()

    text = '\n'.join([
        'Конечно!',
        '   ',
        'Хорошая учебная цель отвечает на три вопроса.',
        '1. Что именно сможет делать студент? ',
        '2. При каких '
        'условиях он это сможет делать? '
        '3. Насколько хорошо он это сможет делать?',
        '  ',
        'Допустим, мы решили создать '
        'кулинарный курс для начинающих. И на одном из занятий мы хотим научить студентов готовить пшенную кашу.',
        '  ',
        'Мы '
        'понимаем, что это уровень применения, то есть студенту на занятии нужно сначала узнать и понять, '
        'как готовить кашу, затем применить это на практике. Но как именно? Ведь можно приготовить кашу под '
        'пристальным присмотром шеф-повара, можно с закрытыми глазами, можно... как угодно еще!',
        '   ',
        'Здесь мы обращаемся '
        'к трем вопросам и формулируем точную цель: научить слушателей готовить вкусную пшенную кашу по рецепту и без '
        'ошибок. Что именно может сделать студент — готовить пшенную кашу, при каких условиях он может это сделать — '
        'по рецепту, насколько хорошо он может это сделать — вкусно и без ошибок.',
    ])

    buttons = [[
        InlineKeyboardButton(text='Зачем так точно формулировать цель?', callback_data=DUMMY),
    ]]
    keyboard = InlineKeyboardMarkup(buttons)

    await update.callback_query.message.reply_text(text, reply_markup=keyboard)

    return BLOCK2_INTRO_12


async def block2_intro_10(update: Update, context: ContextTypes.DEFAULT_TYPE) -> str:
    query = update.callback_query
    await query.answer()

    text = '\n'.join([
        'Хорошо сформулированная цель помогает нам не только понять, что именно сможет сделать студент после занятия '
        'или программы, но и как это оценить.',
        '   ',
        'Если мы решили, что студент сможет приготовить вкусную кашу по '
        'рецепту и без ошибок, значит, чтобы это оценить, нам нужно наблюдать процесс приготовления и попробовать '
        'кашу.',
        '  ',
        'То есть вариант, когда студент просто расскажет нам, как бы он эту кашу приготовил, не подойдет. '
        'Подробнее об этом мы поговорим чуть позже.',
        '  ',
        'А сейчас попробуем попрактиковаться в постановке цели?',
    ])

    buttons = [[
        InlineKeyboardButton(text='Пробуем!', callback_data=DUMMY),
    ]]
    keyboard = InlineKeyboardMarkup(buttons)

    await update.callback_query.message.reply_text(text, reply_markup=keyboard)

    return BLOCK2_PRACTICE_1


async def block2_practice_1(update: Update, context: ContextTypes.DEFAULT_TYPE) -> str:
    query = update.callback_query
    await query.answer()

    text = '\n'.join([
        'Отлично!',
        '   ',
        'Представьте, что мы учим студентов делать иллюстрации к постам для социальных сетей. Студенты уже '
        'знакомы с программой, в которой мы работаем — Figma. Сегодня мы покажем, как создать иллюстрацию с анонсом '
        'мероприятия и попросим студентов повторить наш результат.',
        '  ',
        'Давайте попробуем понять, что не так с этим '
        'образовательным результатом: студенты могут сделать иллюстрацию в Figma.',
        '   ',
        'Какие у вас есть идеи? Напишите одним сообщением.',
    ])

    await update.callback_query.message.reply_text(text)

    return BLOCK2_PRACTICE_2


async def block2_practice_2(update: Update, context: ContextTypes.DEFAULT_TYPE) -> str:
    context.user_data[USER_DATA_BLOCK2_QUIZ_1] = update.message.text

    text = '\n'.join([
        'Спасибо!',
        '  ',
        'У меня мысли такие:',
        '– не очень понятно, какую иллюстрацию и для чего нужно создать, они могут '
        'быть очень разными, поэтому лучше уточнить;',
        ' – степень результата не прозрачна: если студент сделает '
        'иллюстрацию только с помощью нашего видео, достигнем ли мы цели? А если он будет делать одну иллюстрацию в '
        'течение 4 часов? ',
        '  ',
        'Предлагаю вам попробовать самостоятельно сформулировать учебую цель. Возьмите простую '
        'задачу из вашей профессиональной деятельности и представьте, что вам нужно научить другого человека этой '
        'задаче. Как бы вы описали результат?',
    ])

    await update.message.reply_text(text)

    return BLOCK2_PRACTICE_3


async def block2_practice_3(update: Update, context: ContextTypes.DEFAULT_TYPE) -> str:
    text = '\n'.join([
        'Отлично! Теперь попробуйте проверить его с помощью трёх вопросов:',
        ' • что именно сможет делать студент, ',
        '• при каких условиях он это сможет делать, ',
        '• насколько хорошо он это сможет делать.',
        '  ',
        'Если ответы на них '
        'есть в результате, с ним всё должно быть в порядке.',
    ])

    buttons = [[
        InlineKeyboardButton(text='Теперь можно думать о содержании?', callback_data=DUMMY),
    ]]
    keyboard = InlineKeyboardMarkup(buttons)

    await update.message.reply_text(text, reply_markup=keyboard)

    return BLOCK2_PRACTICE_4


async def block2_practice_4(update: Update, context: ContextTypes.DEFAULT_TYPE) -> str:
    query = update.callback_query
    await query.answer()

    text = '\n'.join([
        'Почти. Прежде чем начинать продумывать занятие, вы также можете уточнить, что студенты уже знают по теме.',
        '   ',
        'Это поможет вам не повторять то, что студенты уже знают, и не спрашивать с них слишком много.',
        '   ',
        'Также важно '
        'вернуться к цели, вспомнить про таксономию Блума и понять, что именно должно быть включено в ваше занятие. '
        'Проверьте, не перескакиваете ли вы с уровня на уровень.',
    ])

    buttons = [[
        InlineKeyboardButton(text='Например?', callback_data=DUMMY),
    ]]
    keyboard = InlineKeyboardMarkup(buttons)

    await update.callback_query.message.reply_text(text, reply_markup=keyboard)

    return BLOCK2_PRACTICE_5


async def block2_practice_5(update: Update, context: ContextTypes.DEFAULT_TYPE) -> str:
    query = update.callback_query
    await query.answer()

    text = '\n'.join([
        'Вернемся к примеру с кашей :)',
        '   ',
        'Допустим, ваши студенты уже знают рецепт каши и могут его вам рассказать. Тогда в занятие не стоит включать '
        'ступень знания – то есть часть с рассказом рецепта, можно сразу перейти к ступени понимания. Например, '
        'попросить студентов объяснить своими словами, что и в каком порядке надо сделать, чтобы сварить кашу. После '
        'этого переходить к практике. Примерный план занятия готов!',
    ])
    await context.bot.send_message(chat_id=update.callback_query.message.chat_id, text=text, parse_mode=ParseMode.HTML)
    await asleep(5)
    text = '\n'.join([
        'Если же ваши студенты не знают рецепта и вы '
        'хотите, чтобы в конце занятия они все-таки смогли сварить кашу, значит начинать нужно с азов. Сначала знание '
        '– рассказываем о рецепте, потом понимание – просим объяснить своими словами или рассказать рецепт соседу, '
        'потом применение – пробуем варить кашу по рецепту.',
        '  ',
        'После того, как у вас есть представление о таком плане '
        'занятия, можно переходить к сценарию.',
        '   ',
        'Как подготовить хороший сценарий расскажет мой коллега, '
        'преподаватель Нетологии Евгений Корытов.',
    ])

    await context.bot.send_message(chat_id=update.effective_chat.id, text=text)

    await asleep(10)

    await context.bot.copy_message(chat_id=update.effective_chat.id, from_chat_id=MEDIA_CHANNEL_ID,
                                   message_id=MEDIA_BLOCK2_VIDEO_1)

    await asleep(10)

    await context.bot.copy_message(chat_id=update.effective_chat.id, from_chat_id=MEDIA_CHANNEL_ID,
                                   message_id=MEDIA_PHOTO_7)

    text = '\n'.join([
        'Вот такой структуры придерживаюсь я и мои коллеги. '
        'Обычно я составляю презентации для занятия. Поговорим о том, как подготовить презентацию?',
    ])

    buttons = [[
        InlineKeyboardButton(text='Да, интересно', callback_data=ANSWER_1),
        InlineKeyboardButton(text='Нет, спасибо', callback_data=ANSWER_2),
    ]]
    keyboard = InlineKeyboardMarkup(buttons)

    await update.callback_query.message.reply_text(text, reply_markup=keyboard)

    return BLOCK2_PRACTICE_6


async def block2_presentation_1(update: Update, context: ContextTypes.DEFAULT_TYPE) -> str:
    query = update.callback_query
    await query.answer()

    text = '\n'.join([
        'На мой взгляд, хорошая презентация на основе составленного ранее сценария должна соответствовать 6 правилам.',
        '   ',
        '<b>1 правило</b>',
        '«Один слайд — одна мысль». Разбивайте информацию на несколько слайдов и сделай дополнительный '
        'клик вместо того, чтобы сразу заваливать слушателей тонной информации.',
        '   ',
        '<b>2 правило</b> ',
        'Соблюдайте баланс между '
        'текстовым и визуальным контентом. Важно, чтобы преподавателя было интересно слушать и чтобы слайды не '
        'дублировали речь.',
        '   ',
        '<b>3 правило</b> ',
        'Краткость. Избегайте слайдов с абзацами сплошного текста и длинными списками '
        'из 7 и более пунктов. Такие слайды воспринимаются хуже всего. Убирайте лишнее, выделяйте главное.',
    ])
    await context.bot.send_message(chat_id=update.effective_chat.id, text=text, parse_mode=ParseMode.HTML)

    await asleep(10)

    text = '\n'.join([
        '<b>4 правило</b> ',
        'Вовлечение. При подготовке подумайте о том, как привлечь внимание слушателя. Это можно сделать с помощью '
        'яркой визуализации, интересных метафор, интерактива со студентам.',
        '   ',
        '<b>5 правило</b>',
        'Структура. Каждый слайд должен '
        'быть логически связан с предыдущим, как страницы в книге.',
        '   ',
        '<b>6 правило</b>',
        'Точность. Подтверждайте свои слова и '
        'утверждения, особенно цифры.',
    ])

    buttons = [[
        InlineKeyboardButton(text='Можно пример?', callback_data=ANSWER_1),
    ]]
    keyboard = InlineKeyboardMarkup(buttons)

    await update.callback_query.message.reply_text(text, reply_markup=keyboard, parse_mode=ParseMode.HTML)

    return BLOCK2_PRESENTATION_2


async def block2_presentation_2(update: Update, context: ContextTypes.DEFAULT_TYPE) -> str:
    query = update.callback_query
    await query.answer()

    text = '\n'.join([
        'Конечно! Я собрал основные правила по созданию презентаций в презентацию :) Её можно использовать как '
        'шаблон. Даже если презентация на вашем занятии не обязательна, вы можете использовать её как ориентир для '
        'хорошей структуры.',
        '  ',
        'Но на этом подготовка не заканчивается. Часто к занятию нужно составить домашнее задание.',
    ])

    buttons = [
        [InlineKeyboardButton(text='Посмотреть презентацию',
                              url='https://docs.google.com/presentation/d/1TrM4FfN_e-tYqrm4839fXmgqTVsQKaAiydUCcjEPjVg/edit')],
        [InlineKeyboardButton(text='Как составить домашнее задание?', callback_data=ANSWER_1)],
    ]
    keyboard = InlineKeyboardMarkup(buttons)

    await update.callback_query.message.reply_text(text, reply_markup=keyboard)

    return BLOCK2_HOMEWORK_1


async def block2_homework_1(update: Update, context: ContextTypes.DEFAULT_TYPE) -> str:
    query = update.callback_query
    await query.answer()

    text = '\n'.join([
        'Часто к занятию нужно составить домашнее задание.',
        '   ',
        'Зачем оно нужно?',
        '  ',
        ' С одной стороны оно помогает '
        'студенту закрепить пройденный материал или попробовать применить его на практике.',
        '  ',
        'С другой – помогает '
        'преподавателю или команде курса понять, насколько студент усвоил материал.',
        '   ',
        'Для составления задания я '
        'часто обращаюсь к таксономии Блума.',
    ])

    buttons = [[
        InlineKeyboardButton(text='Да, помню пример с кашей :)', callback_data=DUMMY),
    ]]
    keyboard = InlineKeyboardMarkup(buttons)

    await update.callback_query.message.reply_text(text, reply_markup=keyboard)

    return BLOCK2_HOMEWORK_2


async def block2_homework_2(update: Update, context: ContextTypes.DEFAULT_TYPE) -> str:
    query = update.callback_query
    await query.answer()

    text = '\n'.join([
        'Это здорово! Думаю, основной принцип вы уже уловили – нам важно, чтобы задание, как и цель занятия, '
        'соответствовали одному и тому же уровню пирамиды Блума.',
        '  ',
        '<b>Уровень знания</b> – назвать, перечислить, запомнить. ',
        '<b>Уровень понимания</b> – рассказать своими словами, обсудить, определить, привести пример, соотнести.',
        '   ',
        'Для этих '
        'уровней подойдут тесты, задания с открытыми вопросами, устные ответы на вопросы, задания с текстом, '
        'например, вставить пропуски.',
        '  ',
        '<b>Уровень применения</b> – применить, решить, сделать, использовать, вычислить, '
        'изменить, завершить.',
        '   ',
        'Например, решить задачу или кейс, применить алгоритм на практике, завершить решение '
        'или начатую работу.',
    ])

    await context.bot.send_message(chat_id=update.effective_chat.id, text=text, disable_web_page_preview=True,
                                   parse_mode=ParseMode.HTML)

    await asleep(10)

    text = '\n'.join([
        '<b>Уровень анализа</b> – проанализировать, сгруппировать, сравнить, связать, упорядочить, проверить.',
        '   ',
        'Для этого '
        'уровня можно предложить студенту сравнивать разные явления, создавать интеллект-карты, которые демонстрируют '
        'взаимосвязь явлений и понятий.',
        '   ',
        '<b>Уровень синтеза</b> – сгруппировать, скомбинировать, разработать, предложить, '
        'перегруппировать, установить, заменить.',
        '   ',
        'На этом уровне студенту можно предлагать создавать новое на основе '
        'уже имеющихся знаний и навыков. Например, предложить новый алгоритм для решение какой-либо задачи.',
        '   ',
        '<b>Уровень оценки</b> – доказать, сделать выводы, обосновать, порекомендовать,'
        ' суммировать, проверить, оценить.',
        ' ',
        'На а этом '
        'уровне студенту можно предложить оценить концепции, теории и явления с профессиональной точки зрения и '
        'обосновать эту оценку.',
    ])

    buttons = [[
        InlineKeyboardButton(text='Ага, спасибо!', callback_data=DUMMY),
    ]]
    keyboard = InlineKeyboardMarkup(buttons)

    await update.callback_query.message.reply_text(text, reply_markup=keyboard, disable_web_page_preview=True,
                                                   parse_mode=ParseMode.HTML)

    return BLOCK2_HOMEWORK_3


async def block2_homework_3(update: Update, context: ContextTypes.DEFAULT_TYPE) -> str:
    query = update.callback_query
    await query.answer()

    text = '\n'.join([
        'Предлагаю посмотреть на примерах, каких ошибок в создании заданий стоит избегать.',
    ])

    buttons = [[
        InlineKeyboardButton(text='Попробуем!', callback_data=DUMMY),
    ]]
    keyboard = InlineKeyboardMarkup(buttons)

    await update.callback_query.message.reply_text(text, reply_markup=keyboard, disable_web_page_preview=True,
                                                   parse_mode=ParseMode.HTML)

    return BLOCK2_HOMEWORK_4


async def block2_homework_4(update: Update, context: ContextTypes.DEFAULT_TYPE) -> str:
    query = update.callback_query
    await query.answer()

    text = '\n'.join([
        'Представим, что я преподаю для новичков. Обязательно ли строить свое задание на материале, '
        'который разбирался на занятии? Или я могу попросить студентов найти что-то самостоятельно?',
        '   ',
        '1. '
        'Необязательно говорить о некоторых фактах и знаниях, которые нужны для решения домашнего задания, '
        'напрямую. Студент может сам сопоставить несколько фактов из лекции, проанализировать их и прийти к нужному '
        'решению. ',
        '  ',
        '2. Можно приложить к занятию дополнительные материалы и построить всё домашнее задание на их '
        'основе. ',
        '  ',
        '3. После занятия и отработки практики на занятии студент должен быть способен выполнить домашнее '
        'задание, не прибегая к дополнительным ресурсам.',
    ])

    buttons = [[
        InlineKeyboardButton(text='1', callback_data=ANSWER_1),
        InlineKeyboardButton(text='2', callback_data=ANSWER_2),
        InlineKeyboardButton(text='3', callback_data=ANSWER_3),
    ]]
    keyboard = InlineKeyboardMarkup(buttons)

    await update.callback_query.message.reply_text(text, reply_markup=keyboard, disable_web_page_preview=True,
                                                   parse_mode=ParseMode.HTML)

    return BLOCK2_HOMEWORK_5


async def block2_homework_5(update: Update, context: ContextTypes.DEFAULT_TYPE) -> str:
    query = update.callback_query
    await query.answer()

    if query.data == ANSWER_1:
        text = '\n'.join([
            'Это неплохой вариант для профессиональной аудитории, у которой уже есть знания и навыки, но для новичков '
            'точно не подойдёт. Если человек только начал изучать какую-то область, ему очень важно получать все '
            'необходимые знания на занятии.',
        ])
    elif query.data == ANSWER_2:
        text = '\n'.join([
            'Если студент может самостоятельно посмотреть материалы и выполнить какое-то задание, у него может '
            'возникнуть справедливый вопрос, зачем он приходил на занятие. Лучше все необходимые знания для решения '
            'домашнего задания давать на занятии. А дополнительные материалы использовать для усложнённых вариантов '
            'заданий или расширения кругозора студентов.',
        ])
    else:
        text = '\n'.join([
            'Действительно, для новичков все необходимые для выполнения домашней работы знания должны быть даны в '
            'занятии.',
            '',
            'Однако, для более продвинутой аудитории можно использовать типы заданий, в которых студенты '
            'могут проявить свою самостоятельность.',
        ])

    await context.bot.send_message(chat_id=update.effective_chat.id, text=text, disable_web_page_preview=True,
                                   parse_mode=ParseMode.HTML)

    await asleep(5)

    text = '\n'.join([
        'В каких случаях нам нужно добавить в текст задания критерии оценки?',
        '   ',
        '1 — При самостоятельной проверке критерии полезны. Но для заданий, которые будут проверены преподавателем, '
        'они избыточны.',
        ' ',
        '2 — Критерии могут быть полезны и для заданий, которые проверяет преподаватель.',
    ])

    buttons = [[
        InlineKeyboardButton(text='1', callback_data=ANSWER_1),
        InlineKeyboardButton(text='2', callback_data=ANSWER_2),
    ]]
    keyboard = InlineKeyboardMarkup(buttons)

    await update.callback_query.message.reply_text(text, reply_markup=keyboard, disable_web_page_preview=True,
                                                   parse_mode=ParseMode.HTML)

    return BLOCK2_HOMEWORK_6


async def block2_homework_6(update: Update, context: ContextTypes.DEFAULT_TYPE) -> str:
    query = update.callback_query
    await query.answer()

    if query.data == ANSWER_1:
        text = '\n'.join([
            'Даже для заданий с проверкой критерии могут быть полезны. Студент будет опираться на них при выполнении '
            'домашнего задания. К ним же он будет апеллировать, если оценка покажется ему несправедливой. А '
            'преподавателю они могут помочь быстро сформулировать обратную связь, ценную для студента: что именно '
            'получилось отлично, а что стоит улучшить. Критерии особенно пригодятся при оценке объёмных работ.',
        ])
    else:
        text = '\n'.join([
            'Конечно! Студент будет опираться на них при выполнении домашнего задания. К ним же он будет '
            'апеллировать, если оценка покажется ему несправедливой. А преподавателю они могут помочь быстро '
            'сформулировать обратную связь, ценную для студента: что именно получилось отлично, а что стоит улучшить. '
            'Критерии особенно пригодятся при оценке объёмных работ.',
        ])

    await context.bot.send_message(chat_id=update.effective_chat.id, text=text, disable_web_page_preview=True,
                                   parse_mode=ParseMode.HTML)

    await asleep(5)

    text = '\n'.join([
        'Например, преподаватель провёл онлайн-лекцию для студентов по определению целевой аудитории: рассказал о '
        'ядре ЦА, сегментации и методике 5W. После этого студенты в мини-группах обсудили, как они поняли эту '
        'методику и решили кейс: провели сегментацию, определили ядро целевой аудитории магазина детских игрушек, '
        'по методике 5W составили портреты этой аудитории.',
    ])
    await context.bot.send_message(chat_id=update.callback_query.message.chat_id, text=text, parse_mode=ParseMode.HTML)
    await asleep(5)
    text = '\n'.join([
        'Домашнее задание звучит так. Дайте определение понятиям '
        '«ядро целевой аудитории» и «сегментация». Опишите своими словами метод 5W. Сдайте задание в Google '
        'Документах. Не забудьте открыть доступ для всех пользователей по ссылке.',
        '   ',
        '<b>Как считаете, нужно ли в этом задании что-то улучшить?</b> ',
        '',
        '1. По-моему, всё отлично. ',
        '2. Да, можно дать студентам более продвинутое задание, '
        'направленное на отработку практических навыков. ',
        '3. Да, можно дать студентам образец выполнения задания и '
        'подробнее описать требования',
    ])

    buttons = [[
        InlineKeyboardButton(text='1', callback_data=ANSWER_1),
        InlineKeyboardButton(text='2', callback_data=ANSWER_2),
        InlineKeyboardButton(text='3', callback_data=ANSWER_3),
    ]]
    keyboard = InlineKeyboardMarkup(buttons)

    await update.callback_query.message.reply_text(text, reply_markup=keyboard, disable_web_page_preview=True,
                                                   parse_mode=ParseMode.HTML)

    return BLOCK2_HOMEWORK_7


async def block2_homework_7(update: Update, context: ContextTypes.DEFAULT_TYPE) -> str:
    query = update.callback_query
    await query.answer()

    if query.data == ANSWER_1:
        text = '\n'.join([
            'Не совсем. Студенты уже применяли теоретические знания на практике во время занятия. Домашнее задание не '
            'предлагает им улучшить или продолжить тренировать практические навыки по определению, сегментации и '
            'описанию ЦА. Скорее оно ориентировано на уровень понимания и вполне подошло бы после видеолекции, '
            'чтобы проверить, действительно ли студенты усвоили материал.',
            '   ',
            'В этой ситуации больше подойдёт задание, '
            'ориентированное на уровень применения: сегментируйте целевую аудиторию, определите ядро и составьте '
            'портреты ЦА по методике 5W для конкретных компаний. Оно поможет студенту закрепить навыки, полученные на '
            'занятии, ещё раз отработать их на практике, но уже в другом контексте.',
        ])
    elif query.data == ANSWER_2:
        text = '\n'.join([
            'Отличная идея! ',
            '   ',
            'Если студенты уже практиковались на занятии, пробовали применять какие-то инструменты, '
            'почему бы не закрепить это в домашнем задании? Оно поможет студенту закрепить навыки, ещё раз отработать '
            'их на практике, но уже в другом контексте.',
        ])
    else:
        text = '\n'.join([
            'Кажется, здесь этого не требуется. Формат, в котором нужно сдать задание, описан — Google Документы с '
            'открытым доступом. Образец выполнения вряд ли понадобится студенту, ведь задание достаточно простое и '
            'направлено на интерпретацию, уровень понимания. Если студенту дать образец, это фактически будет готовый '
            'ответ на задание.',
            ' ',
            'В этой ситуации больше подойдёт задание, ориентированное на уровень применения: '
            'сегментируйте целевую аудиторию, определите ядро и составьте портреты ЦА по методике 5W для конкретных '
            'компаний. Оно поможет студенту закрепить навыки, полученные на занятии, ещё раз отработать их на '
            'практике, но уже в другом контексте.',
        ])

    await context.bot.send_message(chat_id=update.effective_chat.id, text=text, disable_web_page_preview=True,
                                   parse_mode=ParseMode.HTML)

    await asleep(5)

    text = '\n'.join([
        'И последний кейс.',
        '   ',
        'Курс состоит в основном из видеолекций, которые студенты проходят асинхронно, то есть в '
        'удобное им время. В одной из них преподаватель разбирает основы типографики — оформления печатного текста — '
        'на примере лендингов различных компаний. Показывает, как правильно подобрать шрифт, сколько шрифтов на одном '
        'сайте можно использовать, как работать с интервалами, заголовками и т. д.',
    ])
    await context.bot.send_message(chat_id=update.callback_query.message.chat_id, text=text, parse_mode=ParseMode.HTML)
    await asleep(5)
    text = '\n'.join([
        'Домашнее задание после этой лекции.',
        '   ',
        'У вас есть тексты для сайтов судостроительной компании и кофейни, а также черновые макеты '
        'лендингов — найти их можно по ссылке. Расположите эти тексты на макетах, подберите подходящие шрифты, '
        'добавьте изображения. Сдайте работу в формате ссылки на проект в Figma.',
        '   ',
        '<b>Что можно изменить в задании, чтобы его улучшить?</b>',
        '   ',
        '1. Убрать работу с расположением текста и изображениями.',
        '2. Можно упростить задание — оставить один макет, а не два. ',
        '3. Можно усложнить задание — добавить ещё 1–2 макета компаний, отличающихся '
        'по тематике, чтобы студент больше потренировался.',
    ])

    buttons = [[
        InlineKeyboardButton(text='1', callback_data=ANSWER_1),
        InlineKeyboardButton(text='2', callback_data=ANSWER_2),
        InlineKeyboardButton(text='3', callback_data=ANSWER_3),
    ]]
    keyboard = InlineKeyboardMarkup(buttons)

    await update.callback_query.message.reply_text(text, reply_markup=keyboard, disable_web_page_preview=True,
                                                   parse_mode=ParseMode.HTML)

    return BLOCK2_HOMEWORK_8


async def block2_homework_8(update: Update, context: ContextTypes.DEFAULT_TYPE) -> str:
    query = update.callback_query
    await query.answer()

    if query.data == ANSWER_1:
        text = '\n'.join([
            'Хорошее решение! Студенту на лекции рассказали, как правильно подобрать шрифт, сколько шрифтов можно '
            'использовать, как работать с заголовками. Но о расположении текста на лендинге или работе с '
            'изображениями на лекции не говорилось. Скорее всего, студент не сможет выполнить это задание, '
            'т. к. полученных на занятии знаний недостаточно. ',
            '  ',
            'Какое задание будет более удачным?  Можно дать '
            'студенту два готовых макета лендингов, попросить подобрать более подходящий шрифт и обосновать свой '
            'выбор. Это поможет студенту сфокусироваться на основной задаче — работе со шрифтом. С таким заданием '
            'студенту будет справиться намного легче, ведь на лекции преподаватель рассказывает об этом на примерах.',
        ])
    elif query.data == ANSWER_2:
        text = '\n'.join([
            'Кажется, в этот раз со сложностью задания действительно перебор. Но дело не в количестве макетов. '
            'Студенту на лекции рассказали, как правильно подобрать шрифт, сколько шрифтов можно использовать, '
            'как работать с заголовками. Но о расположении текста на лендинге или работе с изображениями на лекции не '
            'говорилось. Скорее всего, студент не сможет выполнить это задание, так как полученных на занятии знаний '
            'недостаточно.',
            '  ',
            'Какое задание будет более удачным?  Можно дать студенту два готовых макета лендингов, '
            'попросить подобрать более подходящий шрифт и обосновать свой выбор. Это поможет студенту сфокусироваться '
            'на основной задаче — работе со шрифтом. С таким заданием студенту будет справиться намного легче, '
            'ведь на лекции преподаватель рассказывает об этом.',
        ])
    else:
        text = '\n'.join([
            'Кажется, в этот раз со сложностью задания уже и так перебор. Дело даже не в количестве макетов. Студенту '
            'на лекции рассказали, как правильно подобрать шрифт, сколько шрифтов можно использовать, как работать с '
            'заголовками. Но о расположении текста на лендинге или работе с изображениями на лекции не говорилось. '
            'Скорее всего, студент не сможет выполнить это задание, т. к. полученных на занятии знаний недостаточно. '
            'Какое задание будет более удачным?',
            'Можно дать студенту два готовых макета лендингов, попросить подобрать '
            'более подходящий шрифт и обосновать свой выбор. Это поможет студенту сфокусироваться на основной задаче '
            '— работе со шрифтом. С таким заданием студенту будет справиться намного легче, ведь на лекции '
            'преподаватель рассказывает об этом.',
        ])

    await context.bot.send_message(chat_id=update.effective_chat.id, text=text, disable_web_page_preview=True,
                                   parse_mode=ParseMode.HTML)

    await asleep(10)
    text = '\n'.join([
        'Итак, создавая домашнее задание, стоит опираться на:',
        '– цель занятия;',
        '– навыки, которые студент должен получить в процессе;',
        '– формат занятия;',
        '– чёткие критерии оценки.',
        '   ',
        'Не забудьте дать студенту чёткую и '
        'понятную инструкцию: в каком формате и когда нужно сдать задание.',
        '   ',
        'Мы обсудили подготовку к занятию и '
        'поговорили о том:',
        '– что нужно знать о целевой аудитории и самом курсе перед тем как планировать занятие, ',
        '– как поставить цель на занятие и сформировать образовательный результат, ',
        '– как составить сценарий занятия, ',
        '– как подготовить презентацию, ',
        '– как придумать ДЗ.',
    ])
    await context.bot.send_message(chat_id=update.callback_query.message.chat_id, text=text, parse_mode=ParseMode.HTML)
    await asleep(5)
    text = '\n'.join([
        'Хочу получить от вас обратную связь. Два коротких '
        'вопроса и будем двигаться дальше. ',
        '  ',
        'Что вы уже знали или использовали в своей работе?',
    ])

    await update.callback_query.message.reply_text(text, disable_web_page_preview=True, parse_mode=ParseMode.HTML)

    return BLOCK2_HOMEWORK_9


async def block2_homework_9(update: Update, context: ContextTypes.DEFAULT_TYPE) -> str:
    text = '\n'.join([
        'Спасибо, что поделились! А что было для вас интересным, с чем вы раньше не сталкивались?',
    ])

    await update.message.reply_text(text, disable_web_page_preview=True, parse_mode=ParseMode.HTML)

    return BLOCK2_FINISH_1


async def block2_finish_1(update: Update, context: ContextTypes.DEFAULT_TYPE) -> str:
    text = '\n'.join([
        'Супер! Переходим к следующему этапу – проведению занятия? '
        'Или хотите посмотреть все разделы и выбрать подходящий?',
    ])
    buttons = [[
        InlineKeyboardButton(text='К следующему этапу', callback_data=ANSWER_1)
    ], [
        InlineKeyboardButton(text='Хочу посмотреть все блоки и выбрать', callback_data=ANSWER_2),
    ], [
        InlineKeyboardButton(text='Буду заканчивать курс', callback_data=ANSWER_3),
    ]]
    keyboard = InlineKeyboardMarkup(buttons)

    await update.message.reply_text(text, reply_markup=keyboard)

    return BLOCK2_FINISH_2


async def block2_finish_2(update: Update, context: ContextTypes.DEFAULT_TYPE) -> str:
    query = update.callback_query
    await query.answer()

    text = '\n'.join([
        'Что выберем?',
    ])

    buttons = [[
        InlineKeyboardButton(text='Проводим занятие', callback_data=ANSWER_1),
    ], [
        InlineKeyboardButton(text='А что по домашкам?', callback_data=ANSWER_2)
    ], [
        InlineKeyboardButton(text='Преподаватель тоже человек!', callback_data=ANSWER_3),
    ]]
    keyboard = InlineKeyboardMarkup(buttons)

    await update.callback_query.message.reply_text(text, reply_markup=keyboard)

    return BLOCK2_FINISH_3


block2_states = {
    BLOCK2_INTRO: [CallbackQueryHandler(block2_intro)],
    BLOCK2_INTRO_1: [CallbackQueryHandler(block2_intro_1)],
    BLOCK2_INTRO_2: [CallbackQueryHandler(block2_intro_2)],
    BLOCK2_INTRO_3: [CallbackQueryHandler(block2_intro_3)],
    BLOCK2_INTRO_4: [CallbackQueryHandler(block2_intro_4)],
    BLOCK2_INTRO_5: [CallbackQueryHandler(block2_intro_5)],
    BLOCK2_INTRO_6: [MessageHandler(filters.TEXT & ~filters.COMMAND, block2_intro_5_1)],
    BLOCK2_INTRO_7: [CallbackQueryHandler(block2_intro_5_2)],
    BLOCK2_INTRO_8: [CallbackQueryHandler(block2_intro_6)],
    BLOCK2_INTRO_9: [CallbackQueryHandler(block2_intro_7)],
    BLOCK2_INTRO_10: [CallbackQueryHandler(block2_intro_8)],
    BLOCK2_INTRO_11: [CallbackQueryHandler(block2_intro_9)],
    BLOCK2_INTRO_12: [CallbackQueryHandler(block2_intro_10)],

    BLOCK2_PRACTICE_1: [CallbackQueryHandler(block2_practice_1)],
    BLOCK2_PRACTICE_2: [MessageHandler(filters.TEXT & ~filters.COMMAND, block2_practice_2)],
    BLOCK2_PRACTICE_3: [MessageHandler(filters.TEXT & ~filters.COMMAND, block2_practice_3)],
    BLOCK2_PRACTICE_4: [CallbackQueryHandler(block2_practice_4)],
    BLOCK2_PRACTICE_5: [CallbackQueryHandler(block2_practice_5)],
    BLOCK2_PRACTICE_6: [
        CallbackQueryHandler(block2_presentation_1, pattern=ANSWER_1),
        CallbackQueryHandler(block2_homework_1, pattern=ANSWER_2),
    ],

    BLOCK2_PRESENTATION_1: [CallbackQueryHandler(block2_presentation_1)],
    BLOCK2_PRESENTATION_2: [CallbackQueryHandler(block2_presentation_2)],

    BLOCK2_HOMEWORK_1: [CallbackQueryHandler(block2_homework_1)],
    BLOCK2_HOMEWORK_2: [CallbackQueryHandler(block2_homework_2)],
    BLOCK2_HOMEWORK_3: [CallbackQueryHandler(block2_homework_3)],
    BLOCK2_HOMEWORK_4: [CallbackQueryHandler(block2_homework_4)],
    BLOCK2_HOMEWORK_5: [CallbackQueryHandler(block2_homework_5)],
    BLOCK2_HOMEWORK_6: [CallbackQueryHandler(block2_homework_6)],
    BLOCK2_HOMEWORK_7: [CallbackQueryHandler(block2_homework_7)],
    BLOCK2_HOMEWORK_8: [CallbackQueryHandler(block2_homework_8)],
    BLOCK2_HOMEWORK_9: [MessageHandler(filters.TEXT & ~filters.COMMAND, block2_homework_9)],

    BLOCK2_FINISH_1: [MessageHandler(filters.TEXT & ~filters.COMMAND, block2_finish_1)],
    BLOCK2_FINISH_2: [
        CallbackQueryHandler(block3_intro, pattern=ANSWER_1),
        CallbackQueryHandler(block2_finish_2, pattern=ANSWER_2),
        CallbackQueryHandler(block1_final, pattern=ANSWER_3),
    ],
    BLOCK2_FINISH_3: [
        CallbackQueryHandler(block3_intro, pattern=ANSWER_1),
        CallbackQueryHandler(block4_intro, pattern=ANSWER_2),
        CallbackQueryHandler(block5_intro, pattern=ANSWER_3),
    ],
}
