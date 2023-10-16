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


async def block3_intro_1(update: Update, context: ContextTypes.DEFAULT_TYPE) -> str:
    query = update.callback_query
    await query.answer()

    text = '\n'.join([
        'Согласен!',
        '  ',
        'Когда место выбрано, <b>проверьте скорость интернета</b>. Используйте Speedtest: нажмите на ссылку, затем «Начать '
        'тест». Для комфортного проведения занятия скорость должна быть не ниже 20 Мб.',
        '   ',
        '<b>Проверьте камеру и микрофон</b>. '
        'Можно использовать Zoom: скачайте приложение, нажмите «Начать новую конференцию», зайдите в настройки видео '
        'и звука. Попробуйте записать аудио, проверьте, нет ли посторонних шумов. Включите камеру и посмотрите, '
        'хорошо ли вас видно. Если ведёте занятие с ноутбука, проверьте его заряд и держите при себе блок питания.',
    ])

    buttons = [[
        InlineKeyboardButton(text='Что делать, если есть проблема?', callback_data=DUMMY),
    ]]
    keyboard = InlineKeyboardMarkup(buttons)

    await update.callback_query.message.reply_text(text, reply_markup=keyboard, disable_web_page_preview=True,
                                                   parse_mode=ParseMode.HTML)

    return BLOCK3_INTRO_2


async def block3_intro_2(update: Update, context: ContextTypes.DEFAULT_TYPE) -> str:
    query = update.callback_query
    await query.answer()

    text = '\n'.join([
        'Не паниковать :) Она может возникнуть у любого человека. Важно предупредить студентов, что у вас возникла '
        'техническая проблема и сейчас вы попытаетесь её решить. Чтобы избежать технических сбоев, используйте '
        'браузеры Chrome и Mozila FireFox. Safari не всегда работает стабильно.',
        '   ',
        'Если проблема всё-таки случилась, '
        'закройте лишние программы и вкладки, затем попробуйте перезагрузить браузер или сам компьютер.',
        ' ',
        'Если '
        'проблема со звуком, проверьте, тот ли микрофон указан в настройках платформы. Попробуйте отрегулировать его '
        'чувствительность.',
        '  ',
        'Может быть, у вас не очень хорошая скорость интернета и связь прерывается. Если вы не '
        'можете подключиться к другой сети, выключите видео.',
        ' ',
        'На занятиях могут присутствовать кураторы или '
        'специалисты технической поддержки. Если они есть, обратитесь к ним за помощью. Если нет — сообщите '
        'студентам, что занятие нужно перенести и вы вернётесь с новыми датой и временем позже.',
    ])

    buttons = [[
        InlineKeyboardButton(text='Как мне выглядеть в кадре?', callback_data=DUMMY),
    ]]
    keyboard = InlineKeyboardMarkup(buttons)

    await update.callback_query.message.reply_text(text, reply_markup=keyboard, disable_web_page_preview=True,
                                                   parse_mode=ParseMode.HTML)

    return BLOCK3_INTRO_3


async def block3_intro_3(update: Update, context: ContextTypes.DEFAULT_TYPE) -> str:
    query = update.callback_query
    await query.answer()

    text = '\n'.join([
        'Заранее продумайте внешний вид. Конечно, никто не будет ждать от вас смокинга или вечернего платья, '
        'но и пижаму могут оценить не все.',
        '   ',
        'Я предпочитаю естественность, без обилия макияжа и замысловатой одежды, '
        'но вы вольны следовать своему стилю или опираться на рекомендации компании, в которой работаете. Вам должно '
        'быть комфортно.',
        '   ',
        'Для меня очень важно удобство, поэтому чаще всего я использую повседневный стиль – '
        'футболки, свитшоты и толстовки, придерживаюсь светлых или приглушённых цветов в одежде, например, '
        'тёмно-синего, бежевого, серого, черного, темно-зеленого. Однако, я знаю преподавателей, '
        'которые предпочитаюсь более яркие цвета, например голубой, зелёный, жёлтый, фиолетовый.',
    ])

    buttons = [[
        InlineKeyboardButton(text='Как одежда не подходит?', callback_data=DUMMY),
    ]]
    keyboard = InlineKeyboardMarkup(buttons)

    await update.callback_query.message.reply_text(text, reply_markup=keyboard, disable_web_page_preview=True,
                                                   parse_mode=ParseMode.HTML)

    return BLOCK3_INTRO_4


async def block3_intro_4(update: Update, context: ContextTypes.DEFAULT_TYPE) -> str:
    query = update.callback_query
    await query.answer()

    text = '''Я бы не рекомендовал вести занятие в такой: 
– кислотных цветов, с яркими принтами; 
– с мелким узором: клетка, рубчик, огурцы, ёлочка, горошек и т. д.; 
– с пайетками, бисером, стеклярусом или из блестящих тканей.   

Такая одежда будет рябить в кадре.'''

    buttons = [[
        InlineKeyboardButton(text='Как держаться перед камерой?', callback_data=DUMMY),
    ]]
    keyboard = InlineKeyboardMarkup(buttons)

    await update.callback_query.message.reply_text(text, reply_markup=keyboard, disable_web_page_preview=True,
                                                   parse_mode=ParseMode.HTML)

    return BLOCK3_INTRO_5


async def block3_intro_5(update: Update, context: ContextTypes.DEFAULT_TYPE) -> str:
    query = update.callback_query
    await query.answer()

    text = '\n'.join([
        'Если вы работаете в компании, наверняка у неё есть правила проведения занятий. Вы можете с ними '
        'ознакомиться. В любом случае, есть общие рекомендации, и я с удовольствием поделюсь ими.',
        '  ',
        'Располагайтесь в '
        'кадре по грудь. Постарайтесь сделать так, чтобы вас не отвлекали посторонние разговоры, звонки или доставка. '
        'Приготовьте стакан воды на случай, если захочется пить, а вот есть и курить перед камерой не рекомендую. '
        'Старайтесь всё время смотреть на экран компьютера. Так вы создаёте ощущение зрительного контакта со '
        'студентами.',
    ])

    await context.bot.send_message(chat_id=update.effective_chat.id, text=text)

    await asleep(10)

    text = '\n'.join([
        'Сидите прямо, не облокачивайтесь на руки и не ложитесь на стол. Это поможет вам сохранить концентрацию и '
        'внимание, а студентам покажет, что вы заинтересованы в занятии.',
        '   ',
        'Заранее закройте личные проекты, чаты, '
        'отключите уведомления, если пользуетесь демонстрацией экрана. Пусть ваши секреты останутся при вас. 🙂',
        '   ',
        'Я '
        'люблю жестикулировать, шутить и улыбаться на занятии – если вам это комфортно, не сдерживайте себя. Студенты '
        'оценят ваш позитивный настрой.',
    ])

    buttons = [[
        InlineKeyboardButton(text='Что еще ценят студенты в общении?', callback_data=DUMMY),
    ]]
    keyboard = InlineKeyboardMarkup(buttons)

    await update.callback_query.message.reply_text(text, reply_markup=keyboard, disable_web_page_preview=True,
                                                   parse_mode=ParseMode.HTML)

    return BLOCK3_INTRO_6


async def block3_intro_6(update: Update, context: ContextTypes.DEFAULT_TYPE) -> str:
    query = update.callback_query
    await query.answer()

    text = '\n'.join([
        '<b>Студенты ценят, когда преподаватель общается с ними на равных</b>. '
        'Согласитесь, не очень приятно, когда вас '
        'считают несмышлёнышем и одаривают знаниями и опытом. Намного приятнее учиться у человека, который уважает '
        'ваше стремление к развитию и видит в вас взрослого.',
        '  ',
        'Бережность в коммуникации создаёт благоприятную и '
        'безопасную атмосферу на занятии, при которой студентам проще преодолеть стеснение, задавать вопросы, '
        'активно включаться в процесс обучения. Преподаватель по умолчанию уважает студентов вне зависимости от их '
        'пола, расы, политических взглядов, религии и прочих аспектов жизни.',
        '   ',
        'Также <b>не забывайте давать обратную связь на лекции</b>: например, '
        'благодарить студентов за вопросы, хвалить за активность на занятии.',
    ])

    await context.bot.send_message(chat_id=update.effective_chat.id, text=text, disable_web_page_preview=True,
                                   parse_mode=ParseMode.HTML)

    await asleep(10)

    text = '\n'.join([
        '<b>Здорово, когда преподаватель предупреждает студентов об особенностях своей коммуникации</b>. Например, '
        'когда я увлекаюсь материалом, могу говорить очень быстро, и студенты не всегда успевают воспринимать то, '
        'что я говорю. Я предупреждаю студентов об этом и прошу их писать мне в чате или даже перебить и попросить '
        'сбавить темп.',
        '   ',
        'Конечно, студенты рады, когда <b>преподаватель дружелюбен и открыт</b>, готов помочь разобраться с '
        'любым вопросом и не раздражается, если вопросов много. В процессе обучения не всегда всё может быть понятно '
        'с первого раза.',
        '   ',
        'Хороший преподаватель в общении со студентами учитывает групповую динамику, '
        'полностью контролирует процесс занятия и помогает студентам достичь целей.',
    ])

    buttons = [[
        InlineKeyboardButton(text='Как это сделать?', callback_data=DUMMY),
    ]]
    keyboard = InlineKeyboardMarkup(buttons)

    await update.callback_query.message.reply_text(text, reply_markup=keyboard, disable_web_page_preview=True,
                                                   parse_mode=ParseMode.HTML)

    return BLOCK3_INTRO_7


async def block3_intro_7(update: Update, context: ContextTypes.DEFAULT_TYPE) -> str:
    query = update.callback_query
    await query.answer()

    text = '\n'.join([
        'С помощью фасилитации.',
        '  ',
        'Фасилитация — набор инструментов и практик, которые помогают организовать групповое '
        'взаимодействие. ',
        ' ',
        'Каждая группа проживает целую жизнь — от рождения до распада, от старта курса до его '
        'окончания.',
        '   ',
        'За время существования группы возникают дополнительные процессы — групповая динамика: '
        'образование подгрупп по интересам, возникновение симпатий и антипатий, сплочение и конфликты, '
        'принятие групповых решений, выделение лидеров.',
        '   ',
        'Групповая динамика может развиваться сама по себе, '
        'но в сфере онлайн-обучения это происходит плохо: студенты не всегда могут хорошо взаимодействовать в группе, '
        'чувствуют себя одиноко и обособленно, теряют интерес к обучению. Это влияет на продуктивность группы в целом.',
    ])

    buttons = [[
        InlineKeyboardButton(text='Что с этим делать преподавателю?', callback_data=DUMMY),
    ]]
    keyboard = InlineKeyboardMarkup(buttons)

    await update.callback_query.message.reply_text(text, reply_markup=keyboard, disable_web_page_preview=True,
                                                   parse_mode=ParseMode.HTML)

    return BLOCK3_INTRO_8


async def block3_intro_8(update: Update, context: ContextTypes.DEFAULT_TYPE) -> str:
    query = update.callback_query
    await query.answer()

    text = '\n'.join([
        'Взять групповую динамику в свои руки и стать нейтральным лидером для группы студентов, направлять её к цели '
        'и помогать получить ожидаемый результат.',
        '   ',
        'Такого человека называют фасилитатором. Он сочетает роли '
        'руководителя, лидера и одновременно участника группы. Создаёт комфортную атмосферу для обмена идеями, '
        'вовлекает участников группы в обсуждение, поддерживает его темп. Эту роль нужно брать на себя на каждом '
        'занятии.',
    ])

    buttons = [[
        InlineKeyboardButton(text='Давайте обо всем по порядку', callback_data=DUMMY),
    ]]
    keyboard = InlineKeyboardMarkup(buttons)

    await update.callback_query.message.reply_text(text, reply_markup=keyboard, disable_web_page_preview=True,
                                                   parse_mode=ParseMode.HTML)

    return BLOCK3_INTRO_9


async def block3_intro_9(update: Update, context: ContextTypes.DEFAULT_TYPE) -> str:
    query = update.callback_query
    await query.answer()

    text = '\n'.join([
        'Конечно! Так и поступим.',
        '   ',
        'Во-первых, важно управлять настроением группы:',
        '– определять настроение группы;',
        '– нейтрализовывать скепсис и враждебность;',
        '– работать с возражениями и разногласиями;',
        '– конструктивно работать с критикой в свой адрес;',
        '– предотвращать потенциальные конфликты.',
        '   ',
        'Во-вторых, контролировать ход занятия:',
        '– чётко формулировать инструкции;',
        '– удерживать фокус группы на достижении результата;',
        '– проводить занятия по разработанному плану;',
        '– гибко реагировать в случае изменения ситуации.',
        '   ',
        'В-третьих, помогать в достижении результата:',
        '– поддерживать включённость группы в работу;',
        '– помогать студентам в формулировании выводов, промежуточных и окончательных итогов.',
    ])

    await context.bot.send_message(chat_id=update.effective_chat.id, text=text)

    await asleep(10)

    text = '\n'.join([
        'Предлагаю обсудить занятие от начала до конца и понять, где и какие задачи важно выполнить преподавателю. '
        'Частично мы уже говорили об этом на этапе подготовки занятия.',
        '   ',
        'В начале урока важно сделать три вещи. ',
        '1. Снять напряжение от неизвестности и скепсис. ',
        '2. Помочь студентам сфокусироваться на цели занятия. ',
        '3. Создать безопасную обстановку, в которой студентам будет проще проявлять себя.',
    ])
    buttons = [[
        InlineKeyboardButton(text='Логично!', callback_data=DUMMY),
    ]]
    keyboard = InlineKeyboardMarkup(buttons)

    await update.callback_query.message.reply_text(text, reply_markup=keyboard, disable_web_page_preview=True,
                                                   parse_mode=ParseMode.HTML)

    return BLOCK3_INTRO_10


async def block3_intro_10(update: Update, context: ContextTypes.DEFAULT_TYPE) -> str:
    query = update.callback_query
    await query.answer()

    text = '\n'.join([
        'Я делаю три простых шага.',
        '   ',
        '<b>Шаг 1</b> ',
        'Чтобы снять скепсис, рассказываю о своём опыте и предлагаю студентам '
        'удобный способ знакомства. Если времени мало и группа большая, пишем в чате имя, город, несколько интересных '
        'фактов о себе, сферу деятельности или причину, по которой человек решил обучаться на этой программе. '
        'Обязательно реагирую на ответы и благодарю студентов.',
        '   ',
        '<b>Шаг 2</b>',
        'Чтобы снять напряжение от неизвестности и '
        'помочь держать фокус на цели, сообщаю тему занятия и его план, проговариваю, чему научатся студенты. Для '
        'большего вовлечения предлагаю поделиться своими ожиданиями — что студенты хотели бы сегодня узнать. Сделать '
        'это можно в разных форматах — в чате или на виртуальной доске. Главное — даю студентам обратную связь на их '
        'ответы. Рассказываю, что получится сегодня узнать и обсудить. Если есть ожидания, которые выходят за рамки '
        'занятия, подсказываю студентам, в каких источниках об этом можно узнать, или говорю, в каком уроке программы '
        'будет информация об этом.',
    ])

    buttons = [[
        InlineKeyboardButton(text='А шаг 3?', callback_data=DUMMY),
    ]]
    keyboard = InlineKeyboardMarkup(buttons)

    await update.callback_query.message.reply_text(text, reply_markup=keyboard, disable_web_page_preview=True,
                                                   parse_mode=ParseMode.HTML)

    return BLOCK3_INTRO_11


async def block3_intro_11(update: Update, context: ContextTypes.DEFAULT_TYPE) -> str:
    query = update.callback_query
    await query.answer()

    text = '\n'.join([
        'Да, чуть не пропустил!',
        '   ',
        '<b>Шаг 3</b> ',
        'Чтобы создать безопасную и комфортную обстановку, устанавливаю правила. '
        'Проговариваю, когда и в каком порядке можно задавать вопросы, каким образом участники обращаются к друг '
        'другу и как взаимодействуют. Если студенты будут видеть, что правила соблюдаются, то обстановка на занятии '
        'будет предсказуемой и управляемой, студенты будут чувствовать себя комфортно.',
    ])

    buttons = [[
        InlineKeyboardButton(text='С началом понятно, а что дальше?', callback_data=DUMMY),
    ]]
    keyboard = InlineKeyboardMarkup(buttons)

    await update.callback_query.message.reply_text(text, reply_markup=keyboard, disable_web_page_preview=True,
                                                   parse_mode=ParseMode.HTML)

    return BLOCK3_INTRO_12


async def block3_intro_12(update: Update, context: ContextTypes.DEFAULT_TYPE) -> str:
    query = update.callback_query
    await query.answer()

    text = '\n'.join([
        'Дальше важно поддерживать включённость группы в работу, возвращать внимание студентов к занятию. Чтобы это '
        'получалось, я использую такие приемы.',
        '   ',
        '1. Меняю динамику занятия каждые 20–30 минут. Например, '
        'даю студентам 20 минут теории в формате обычной лекции, а дальше предлагаю им в течение 20 минут попробовать '
        'применить эти знания на практике — обсудить, разобрать кейсы, решить практические задачи.',
        '   ',
        '2. Обращаюсь к '
        'опыту студента. Даже во время объяснения теории задаю вопросы: сталкивались ли вы с подобным опытом? Есть ли '
        'у вас примеры из жизни для иллюстрации какого-либо понятия или явления?',
        '   ',
        '3. Помогаю студентам подводить '
        'промежуточный итог. Например, после теории спрашиваю, всё ли понятно. Что стало самым неожиданным? Что вы '
        'уже знали? После практики уточняю, что вызвало больше всего сложностей, что показалось самым интересным.',
        '   ',
        '4. Говорю со студентами на одном языке, не сыплю профессиональными терминами, чтобы не вызвать сложности с '
        'восприятием материала и потерю мотивации.',
    ])

    buttons = [[
        InlineKeyboardButton(text='Может быть, есть что-то ещё?', callback_data=DUMMY),
    ]]
    keyboard = InlineKeyboardMarkup(buttons)

    await update.callback_query.message.reply_text(text, reply_markup=keyboard, disable_web_page_preview=True,
                                                   parse_mode=ParseMode.HTML)

    return BLOCK3_INTRO_13


async def block3_intro_13(update: Update, context: ContextTypes.DEFAULT_TYPE) -> str:
    query = update.callback_query
    await query.answer()

    text = '\n'.join([
        'Конечно. <b>Вы можете делиться своим личным опытом</b> — студентов это поддержит на пути обучения. Например, '
        'расскажите, как вам было сложно справляться с какими-либо заданиями, что вам помогло с ними справиться. Как '
        'вы помогали себе в процессе обучения — например, всегда задавали вопросы, если что-то осталось непонятно,',
        '   ',
        '<b>Используйте разные методики для подачи материала и взаимодействия со студентами</b>. '
        'Например, разборы кейсов, '
        'дискуссии, тесты, фишбоуны, друдлы и другие варианты. Мы собрали интересные методики в методическом '
        '<a href="https://netology.ru/educational-toolbox/">тулбоксе</a>. '
        'Можете познакомиться с ним и использовать в работе.',
        '   ',
        '<b>Можете спросить совета у коллег</b>. Я поделюсь '
        'с вами видео, в котором знакомый вам Евгений Корытов делится своим опытом.',
    ])

    await context.bot.send_message(chat_id=update.effective_chat.id, text=text, disable_web_page_preview=True,
                                   parse_mode=ParseMode.HTML)

    await asleep(10)

    await context.bot.copy_message(chat_id=update.effective_chat.id, from_chat_id=MEDIA_CHANNEL_ID,
                                   message_id=MEDIA_BLOCK3_VIDEO_2)

    await asleep(10)

    text = '\n'.join([
        'В конце занятия важно подвести итоги.',
        '   ',
        'Дайте возможность студентам задать все волнующие их вопросы.',
        '   ',
        'После '
        'повторите основные тезисы, проведите рефлексию. Например, вы можете попросить поделиться в чате ответами на '
        'три вопроса: что студент перестанет делать после занятия, что продолжит, а что начнёт.',
        '   ',
        'Также вы можете: ',
        '– '
        'предложить студентам продолжить фразы: «Сегодня я научился/лась...», «больше всего мне запомнилось ...», '
        '«я удивлён(на) тем, что...», «мне понравилось, что...»; ',
        '– попросить студентов составить в конце занятия '
        'майндмэп с его основными тезисами и понятиями.',
    ])
    buttons = [[
        InlineKeyboardButton(text='Кажется, чего-то не хватает...', callback_data=DUMMY),
    ]]
    keyboard = InlineKeyboardMarkup(buttons)

    await update.callback_query.message.reply_text(text, reply_markup=keyboard, disable_web_page_preview=True,
                                                   parse_mode=ParseMode.HTML)

    return BLOCK3_INTRO_14


async def block3_intro_14(update: Update, context: ContextTypes.DEFAULT_TYPE) -> str:
    query = update.callback_query
    await query.answer()

    text = '\n'.join([
        'Вы правы. Важно поблагодарить студентов и попрощаться. Если это возможно, оставьте свои контакты или '
        'скажите, к кому студенты могут обратиться с вопросами. Это поможет студенту понять, что он не один и ему '
        'готовы помочь учиться эффективно.',
    ])

    buttons = [[
        InlineKeyboardButton(text='Тоже так считаю', callback_data=DUMMY),
    ]]
    keyboard = InlineKeyboardMarkup(buttons)

    await update.callback_query.message.reply_text(text, reply_markup=keyboard, disable_web_page_preview=True,
                                                   parse_mode=ParseMode.HTML)

    return BLOCK3_INTRO_15


async def block3_intro_15_1(update: Update, context: ContextTypes.DEFAULT_TYPE) -> str:
    query = update.callback_query
    await query.answer()

    text = '\n'.join([
        'У меня есть список вещей, которые я не делаю на своих занятиях. У каждого преподавателя он может быть разным '
        '– все зависит от того, где вы преподаете и что считаете уместным на программе.',
        '   ',
        'Будет здорово, '
        'если вы заранее подумаете про такие моменты. Вот список того, что я не делаю на занятиях.',
        '   ',
        'Не рекламирую '
        'компании, курсы, инструменты. Я могу что-то посоветовать, сказать, чем лично и пользуюсь, выразить свое '
        'мнение достаточно сдержанно, но агитировать студентов к покупке кажется мне лишним.',
    ])
    await context.bot.send_message(chat_id=update.callback_query.message.chat_id, text=text, parse_mode=ParseMode.HTML)
    await asleep(10)
    text = '\n'.join([
        'Не оставляю студентов '
        'без ответа. Если я не знаю ответа на вопрос по содержанию – обещаю посмотреть и вернуться. Если вопрос про '
        'процесс обучения и технические вещи – либо адресую студента к коллеге, который может помочь, либо говорю, '
        'что узнаю ответ и вернусь. Студенту важно понимать, что ему готовы помочь.',
        '   ',
        'Не критикую коллег и процессы '
        'программы, на которой преподаю. Мое мнение может расходиться с другим экспертом. Если такое случается, '
        'я не буду говорить студентам, что преподаватель не прав или плохо разбирается в этой сфере. Попрошу команду '
        'курса нас связать и договориться о том, какую позицию транслировать студентам. То же самое касается '
        'процессов – если меня что-то беспокоит, я не буду делиться переживаниями со студентами, а в первую очередь '
        'поговорю с командой.',
        '   ',
        'Сейчас я предлагаю вам подвести итоги и выполнить небольшое задание.',
    ])
    buttons = [[
        InlineKeyboardButton(text='Поехали!', callback_data=DUMMY),
    ]]
    keyboard = InlineKeyboardMarkup(buttons)

    await update.callback_query.message.reply_text(text, reply_markup=keyboard, disable_web_page_preview=True,
                                                   parse_mode=ParseMode.HTML)

    return BLOCK3_INTRO_16


async def block3_intro_15_2(update: Update, context: ContextTypes.DEFAULT_TYPE) -> str:
    query = update.callback_query
    await query.answer()

    text = '\n'.join([
        '<b>Мы выяснили, что перед проведением занятия нужно:</b> ',
        '– подобрать подходящее место; ',
        '– продумать внешний вид; ',
        '– проверить интернет, камеру и микрофон.',
        '   ',
        '<b>В начале занятия важно:</b> ',
        '– познакомиться со студентами, рассказать о своей экспертизе; ',
        '– сообщить цель занятия и его план (можно собрать ожидания студентов); ',
        '– установить правила занятия.',
        '   ',
    ])
    await context.bot.send_message(chat_id=update.callback_query.message.chat_id, text=text, parse_mode=ParseMode.HTML)
    await asleep(5)
    text = '\n'.join([
        '<b>В основной части нужно:</b> ',
        '– говорить со студентами на одном языке, приводить понятные и интересные примеры; ',
        '– управлять динамикой урока; ',
        '– удерживать внимание студентов; ',
        '– вовлекать студентов во взаимодействие.',
        '   ',
        '<b>В конце стоит:</b> ',
        '– дать возможность задать вопросы; ',
        '– проговорить основные тезисы занятия; ',
        '– провести рефлексию; ',
        '– поблагодарить студентов за работу и попрощаться.',
    ])
    buttons = [[
        InlineKeyboardButton(text='Да, все так!', callback_data=DUMMY),
    ]]
    keyboard = InlineKeyboardMarkup(buttons)

    await update.callback_query.message.reply_text(text, reply_markup=keyboard, disable_web_page_preview=True,
                                                   parse_mode=ParseMode.HTML)

    return BLOCK3_INTRO_17


async def block3_intro_16(update: Update, context: ContextTypes.DEFAULT_TYPE) -> str:
    query = update.callback_query
    await query.answer()

    text = '\n'.join([
        'Про задание. Предложу посмотреть две короткие лекции и написать, что вам в них понравилось, что следовало бы '
        'улучшить.',
        '   ',
        'На что стоит обратить внимание при просмотре.',
        '   ',
        '1. Технические настройки. ',
        '2. Структура урока: что преподаватель делает в начале, основной части и конце занятия. ',
        '3. Как преподаватель взаимодействует со студентами? ',
        '4. Какие действия преподавателя вам кажутся не очень уместными?',
        '   ',
        'Если сейчас вы пользуетесь '
        'телефоном, при просмотре роликов расположите его горизонтально – так будет удобнее :)',
    ])

    await context.bot.send_message(chat_id=update.effective_chat.id, text=text)

    await asleep(10)

    await context.bot.copy_message(chat_id=update.effective_chat.id, from_chat_id=MEDIA_CHANNEL_ID,
                                   message_id=MEDIA_BLOCK3_VIDEO_3)

    await asleep(10)

    await context.bot.copy_message(chat_id=update.effective_chat.id, from_chat_id=MEDIA_CHANNEL_ID,
                                   message_id=MEDIA_BLOCK3_VIDEO_4)

    await asleep(10)

    text = '\n'.join([
        'Сверим часы? Введите ответ в поле для текста. '
        'Сначала напишите о первой лекции, затем в том же сообщении о второй.',
    ])
    await update.callback_query.message.reply_text(text)

    return BLOCK3_INTRO_18


async def block3_intro_17(update: Update, context: ContextTypes.DEFAULT_TYPE) -> str:
    context.user_data[USER_DATA_BLOCK3_LECTURE] = update.message.text

    text = '\n'.join([
        'Спасибо! Поделюсь своими мыслями.',
        '  ',
        'Лекция №1.',
        '   ',
        'Что мне показалось удачным в лекции: ',
        '– эксперт говорит чётко, достаточно громко и с оптимальной скоростью; ',
        '– у эксперта хороший внешний вид: аккуратные волосы, нейтральная одежда; ',
        '– видео и звук неплохие, можно добавить больше освещения и использовать гарнитуру, чтобы было ещё лучше; ',
        '– эксперт визуализировал свой материал.',
    ])

    buttons = [[
        InlineKeyboardButton(text='Что можно было бы улучшить?', callback_data=DUMMY),
    ]]
    keyboard = InlineKeyboardMarkup(buttons)

    await update.message.reply_text(text, reply_markup=keyboard)

    return BLOCK3_INTRO_19


async def block3_intro_18(update: Update, context: ContextTypes.DEFAULT_TYPE) -> str:
    query = update.callback_query
    await query.answer()

    text = '\n'.join([
        'Лекция №1.',
        '   ',
        'Что я бы порекомендовал сделать лучше:',
        '– подобрать более нейтральный фон; ',
        '– выделить пару минут на то, чтобы спросить, какой у всех настрой, что сегодня ждут студенты от занятия; ',
        '– сообщить план занятия; ',
        '– эксперт не очень подробно объясняет теорию: было бы здорово использовать примеры, больше времени уделять '
        'каждому пункту; ',
        '– эксперт не взаимодействует со студентами: не вовлекает их в занятие, не обращается к их '
        'опыту, игнорирует вопросы. Есть большой риск, что студентам будет не понятен материал, не очень понравится '
        'занятие в целом, и мотивация к обучению упадёт; ',
        '– у эксперта возникли технические сложности. Хорошо, '
        'что получилось быстро вернуться, но лучше избегать таких ситуаций; ',
        '– поработать над подачей: меньше обращать '
        'внимание на ограничения во времени и больше сосредотачиваться на поддерживающей и дружелюбной позиции, '
        'готовности помочь студентам; – можно давать меньше информации на одном слайде, чтобы она проще считывалась.',
    ])

    buttons = [[
        InlineKeyboardButton(text='Что удалось во второй лекции?', callback_data=DUMMY),
    ]]
    keyboard = InlineKeyboardMarkup(buttons)

    await update.callback_query.message.reply_text(text, reply_markup=keyboard)

    return BLOCK3_INTRO_20


async def block3_intro_19(update: Update, context: ContextTypes.DEFAULT_TYPE) -> str:
    query = update.callback_query
    await query.answer()

    text = '\n'.join([
        'Лекция №2.',
        '   ',
        'Что мне показалось удачным в лекции:',
        '– эксперт говорит чётко, достаточно громко и с оптимальной скоростью; ',
        '– у эксперта хороший внешний вид: аккуратные волосы, нейтральная одежда; ',
        '– видео и звук неплохие, можно добавить больше освещения и использовать гарнитуру, чтобы было ещё лучше; ',
        '– у эксперта понятная презентация: не перегружена текстом; ',
        '– эксперт не игнорирует вопросы и акцентирует внимание студентов на важных поинтах с помощью указки.',
    ])

    buttons = [[
        InlineKeyboardButton(text='Что можно улучшить?', callback_data=DUMMY),
    ]]
    keyboard = InlineKeyboardMarkup(buttons)

    await update.callback_query.message.reply_text(text, reply_markup=keyboard)

    return BLOCK3_INTRO_21


async def block3_intro_20(update: Update, context: ContextTypes.DEFAULT_TYPE) -> str:
    query = update.callback_query
    await query.answer()

    text = '\n'.join([
        'Лекция №2.',
        '   ',
        'Что я бы порекомендовал сделать лучше: ',
        '– подобрать более нейтральный фон; ',
        '– выделить пару минут на то, чтобы спросить, какой у всех настрой, что сегодня ждут студенты от занятия; ',
        '– сообщить план занятия; ',
        '– перед проведением занятия внимательно ознакомиться с презентацией; ',
        '– занять более открытую и уважительную '
        'позицию по отношению к студентам: отвечать на их вопросы корректно и без претензий, уважать студентов, '
        'стремиться помочь; ',
        '– не отвлекаться на звонки во время занятия; ',
        '– не рекламировать услуги своей компании: это выглядит странно.',
    ])

    await context.bot.send_message(chat_id=update.effective_chat.id, text=text)

    await asleep(10)

    text = '\n'.join([
        'В процессе общения со студентами вы можете столкнуться с их возражениями или некорректными замечаниями. Мне '
        'кажется важным поговорить об этом. Когда я первый раз оказался в такой ситуации, я не знал, как правильно '
        'реагировать.',
        '   ',
        'Конечно, я и мои коллеги сталкиваемся с этим не часто, но преподавателю важно уметь корректно '
        'общаться в любой ситуации.',
    ])

    buttons = [
        [InlineKeyboardButton(text='Тоже так считаю!', callback_data=ANSWER_1)],
        [InlineKeyboardButton(text='Не думаю, что мне это пригодится', callback_data=ANSWER_5)],
    ]
    keyboard = InlineKeyboardMarkup(buttons)

    await update.callback_query.message.reply_text(text, reply_markup=keyboard)

    return BLOCK3_CONFLICT_1


async def block3_conflict_1(update: Update, context: ContextTypes.DEFAULT_TYPE) -> str:
    query = update.callback_query
    await query.answer()

    await context.bot.copy_message(chat_id=update.effective_chat.id, from_chat_id=MEDIA_CHANNEL_ID,
                                   message_id=MEDIA_PHOTO_8)

    text = '\n'.join([
        'Бывает, что студент может не согласиться с вашим тезисом или мнением. В такой ситуации важно дать студенту '
        'понять, что он услышан, поблагодарить за мнение или вопрос.',
        '   ',
        'Если студент нарушил установленное правило — '
        'например перебил или не очень аккуратно высказался в адрес другого, важно ему напомнить, '
        'как мы взаимодействуем с друг другом на занятии, каким образом задаём вопросы.',
        '   ',
        'Студенту нужно помочь '
        'разобраться в теме, мягко направить, не отрицая его позицию. Согласитесь, если вам будут резко говорить, '
        'что вы не правы, это вызовет желание защищать свою позицию. Дайте студенту озвучить своё мнение, '
        'при необходимости напомните о правилах коммуникации. Затем задайте студенту наводящие вопросы. Пусть он '
        'ответит на них и сам попробует найти ошибку в своих рассуждениях.',
    ])

    buttons = [[
        InlineKeyboardButton(text='Если это не помогло?', callback_data=DUMMY),
    ]]
    keyboard = InlineKeyboardMarkup(buttons)

    await update.callback_query.message.reply_text(text, reply_markup=keyboard)

    return BLOCK3_CONFLICT_2


async def block3_conflict_2(update: Update, context: ContextTypes.DEFAULT_TYPE) -> str:
    query = update.callback_query
    await query.answer()

    text = """Если это не помогло, сообщите, почему ваша точка зрения отличается от точки зрения студента. Можно сказать, что в процессе обучения вы можете столкнуться с тем, что другой человек делает что-то по-другому, это нормально. Но вы исходите из определённых принципов и подходов, потому что они научно доказаны или признаны в профессиональной сфере. Будет здорово, если вы приведёте наглядный пример, почему профи делают именно так, а не иначе. Если и это не помогает, корректно сообщите студенту, что время занятия ограничено и нужно двигаться дальше. Предложите варианты для продолжения обсуждения: например, после занятия, в личных сообщениях или на следующем занятии."""

    buttons = [[
        InlineKeyboardButton(text='Можно пример?', callback_data=DUMMY),
    ]]
    keyboard = InlineKeyboardMarkup(buttons)

    await update.callback_query.message.reply_text(text, reply_markup=keyboard)

    return BLOCK3_CONFLICT_3


async def block3_conflict_3(update: Update, context: ContextTypes.DEFAULT_TYPE) -> str:
    query = update.callback_query
    await query.answer()

    text = '\n'.join([
        'Конечно.'
        'Студент Ваня перебивает вас во время лекции и говорит: «Вообще-то эта технология давно устарела, '
        'сейчас все вот так делают». И рассказывает об околонаучном подходе, который профи не практикуют.',
        '   ',
        '<b>Как вы бы ему ответили?</b> ',
        '',
        '1. «Ваня, спасибо, что поделились своей точкой зрения. Напомню, что мы не перебиваем друг '
        'друга. Будет здорово, если вы в следующий раз напишете вопрос в чат или подождёте, пока я закончу мысль. Я '
        'понимаю ход вашей мысли, но мне кажется этот подход сомнительным по нескольким причинам (перечислите их). Я '
        'работаю в другом подходе, который предполагает научную достоверность и определённые принципы (перечислите '
        'их). Конечно, люди могут выбирать самостоятельно, чему им следовать. Я выбираю такой подход и транслирую '
        'его».',
        '   ',
        '2. «Ваня, в следующий раз не перебивайте меня, пожалуйста, дождитесь, пока я закончу или напишите в '
        'чат. То, что вы говорите, не имеет никакого практического применения у профессионалов или даже лженаучно. '
        'Если вы будете следовать этим идеям, то не сможете состояться в профессии, к сожалению. Вы не правы, '
        'рекомендую вам почитать об этом (рекомендуете источники)».',
    ])

    buttons = [[
        InlineKeyboardButton(text='1', callback_data=ANSWER_1),
        InlineKeyboardButton(text='2', callback_data=ANSWER_2),
    ]]
    keyboard = InlineKeyboardMarkup(buttons)

    await update.callback_query.message.reply_text(text, reply_markup=keyboard, parse_mode=ParseMode.HTML)

    return BLOCK3_CONFLICT_4


async def block3_conflict_4(update: Update, context: ContextTypes.DEFAULT_TYPE) -> str:
    query = update.callback_query
    await query.answer()

    if query.data == ANSWER_1:
        text = '\n'.join([
            'Отлично. Вы поблагодарили студента и корректно напомнили о важных правилах. Важно, что вы не отрицаете '
            'его точку зрения, а говорите, почему вы считаете по-другому. Это поможет студенту услышать вас и понять, '
            'что вы исходите из другого подхода и будете придерживаться его на занятиях.',
        ])
    else:
        text = '\n'.join([
            'Я бы остановился на первом варианте. Напоминание о правилах звучит неплохо, но  дальше следует отрицание '
            'точки зрения студента. Согласитесь, если вам не дали понять, что вы услышаны, а просто сказали, '
            'что вы не правы, хочется стоять на своём ещё сильнее. Важно дать понять студенту, что вы слышите его, '
            'но руководствуетесь другими принципами и на занятии будете придерживаться именно их.',
        ])

    buttons = [[
        InlineKeyboardButton(text='Что делать с негативом?',
                             callback_data=DUMMY),
    ]]
    keyboard = InlineKeyboardMarkup(buttons)

    await update.callback_query.message.reply_text(text, reply_markup=keyboard)

    return BLOCK3_CONFLICT_5


async def block3_conflict_5(update: Update, context: ContextTypes.DEFAULT_TYPE) -> str:
    query = update.callback_query
    await query.answer()

    await context.bot.copy_message(chat_id=update.effective_chat.id, from_chat_id=MEDIA_CHANNEL_ID,
                                   message_id=MEDIA_PHOTO_9)

    text = '\n'.join([
        'Помните, что вряд ли студент хочет намеренно вам навредить или испортить вам настроение. Скорее всего, '
        'он растерян или расстроен и использует те инструменты коммуникации, которые ему доступны в таком '
        'состоянии.',
        '   ',
        '<b>Соблюдайте четыре простых шага.</b> ',
        '',
        '1. Выдохните, всё в порядке. ',
        '2. Поблагодарите студента за обратную связь и выразите сожаление, что он испытал негативные эмоции. ',
        '3. Сфокусируйте студента на конкретной проблеме и получите информацию: что именно было не так, почему. ',
        '4. Предложите варианты решения ситуации.',
    ])

    buttons = [[
        InlineKeyboardButton(text='Можно пример?', callback_data=DUMMY),
    ]]
    keyboard = InlineKeyboardMarkup(buttons)

    await update.callback_query.message.reply_text(text, reply_markup=keyboard, parse_mode=ParseMode.HTML)

    return BLOCK3_CONFLICT_6


async def block3_conflict_6(update: Update, context: ContextTypes.DEFAULT_TYPE) -> str:
    query = update.callback_query
    await query.answer()

    text = '\n'.join([
        'Конечно. Представьте, что студентка Таня дала такую обратную связь в конце занятия: «Прошло так себе. Мне '
        'было сложно, я не получила ответы на вопросы».',
        '   ',
        '<b>Как вы бы ответили?</b> ',
        '',
        '1. «Таня, спасибо, что поделились '
        'обратной связью. Мне жаль, что у вас остались такие впечатления о занятии. Можете уточнить, на какие вопросы '
        'вам хотелось бы получить ответ? Мы можем вместе подумать над тем, как исправить ситуацию».',
        '   ',
        '2. «Здравствуйте! Я учту ваше мнение. Плохо, что у вас остались такие впечатления о занятии. Какие именно '
        'вопросы были вам непонятны? Давайте попробуем разобраться».',
    ])

    buttons = [[
        InlineKeyboardButton(text='1', callback_data=ANSWER_1),
        InlineKeyboardButton(text='2', callback_data=ANSWER_2),
    ]]
    keyboard = InlineKeyboardMarkup(buttons)

    await update.callback_query.message.reply_text(text, reply_markup=keyboard, parse_mode=ParseMode.HTML)

    return BLOCK3_CONFLICT_7


async def block3_conflict_7(update: Update, context: ContextTypes.DEFAULT_TYPE) -> str:
    query = update.callback_query
    await query.answer()

    if query.data == ANSWER_1:
        text = '\n'.join([
            'Отлично. Сначала поблагодарите студента за мнение. Затем выразите своё отношение к ситуации и покажите, '
            'что вам не всё равно. После можно фокусировать студента на конкретной проблеме и предложить способ '
            'решения.',
        ])
    elif query.data == ANSWER_2:
        text = '\n'.join([
            'Я бы предпочёл первый вариант. «Я учту ваше мнение» может восприниматься как высокомерность или '
            'безразличие — заготовленная, дежурная фраза. Здесь важно показать, что мнение студента для вас '
            'действительно важно, поэтому лучше поблагодарить за него. «Плохо, что у вас остались такие впечатления о '
            'занятии» — здесь мы даём оценку чувствам студента, что недопустимо, это может спровоцировать конфликт. '
            'Поэтому лучше выразить сожаление, что студент испытал такие эмоции. «Какие именно вопросы были вам '
            'непонятны?» — в целом формулировка нейтральная, но в контексте сообщения может считываться негативно, '
            'как претензия.',
        ])
    else:
        text = None

    if text:
        await context.bot.send_message(chat_id=update.effective_chat.id, text=text)
        await asleep(7)

        text = '\n'.join([
            'Не стоит бояться студентов, которые задают вопросы, дают обратную связь и вступают с вами в диалог. Они '
            'помогают вам развиваться не только как преподавателю, но и как профессионалу. Например, вы можете узнать '
            'совершенно неожиданный взгляд на проблему или явление, найти новые аргументы, почему что-то хорошо, '
            'а что-то — не очень удачное решение. ',
            'Все мы учимся, и в этом процессе нам важно чувствовать поддержку. '
            'Если вы создадите безопасную, открытую и доверительную атмосферу на занятии с помощью инструментов, '
            'которые мы разобрали выше, всем будет комфортно учиться.',
            '   ',
            'Мне помогают чувствовать себя уверенно '
            'упражнения по ораторскому мастерству. Могу поделиться интересной подборкой из семи коротких видеоуроков '
            'от моего друга и преподавательницы Седы Каспаровой.',
        ])
    else:
        text = '\n'.join([
            'Хорошо!',
            '    ',
            'Я считаю, что студенты, которые задают вопросы, дают обратную связь и вступают в диалог '
            'помогают мне развиваться не только как преподавателю, но и как профессионалу. Например, я могу узнать '
            'совершенно неожиданный взгляд на проблему или явление, найти новые аргументы, почему что-то хорошо, '
            'а что-то — не очень удачное решение.',
            '   ',
            'В любой ситуации мне помогают чувствовать себя уверенно '
            'упражнения по ораторскому мастерству. Могу поделиться интересной подборкой из семи коротких видеоуроков '
            'от моего друга и преподавательницы Седы Каспаровой.',
        ])

    buttons = [
        [InlineKeyboardButton(text='Посмотреть подборку упражнений', callback_data=ANSWER_1)],
        [InlineKeyboardButton(text='Нет, спасибо, идём дальше', callback_data=ANSWER_2)],
    ]
    keyboard = InlineKeyboardMarkup(buttons)
    await update.callback_query.message.reply_text(text, reply_markup=keyboard)

    return BLOCK3_EXERCISES_1


async def block3_exercises_1(update: Update, context: ContextTypes.DEFAULT_TYPE) -> str:
    query = update.callback_query
    await query.answer()

    for message_id in ([
        MEDIA_SELECTION_1,
        MEDIA_SELECTION_2,
        MEDIA_SELECTION_3,
        MEDIA_SELECTION_4,
        MEDIA_SELECTION_6,
        MEDIA_SELECTION_7,
        MEDIA_SELECTION_8,
    ]):
        await context.bot.copy_message(chat_id=update.effective_chat.id, from_chat_id=MEDIA_CHANNEL_ID,
                                       message_id=message_id)
        await asleep(10)

    buttons = [[
        InlineKeyboardButton(text='Вперед!', callback_data=DUMMY),
    ]]
    keyboard = InlineKeyboardMarkup(buttons)
    await update.callback_query.message.reply_text(text='Можем двигаться дальше', reply_markup=keyboard,
                                                   disable_web_page_preview=True,
                                                   parse_mode=ParseMode.HTML)

    return BLOCK3_EXERCISES_2


async def block3_exercises_2(update: Update, context: ContextTypes.DEFAULT_TYPE) -> str:
    query = update.callback_query
    await query.answer()

    text = '\n'.join([
        'Преподавателю важно не только быть хорошим спикером, уметь вовлечь студентов в занятие и управлять его '
        'динамикой, но и уверенно себя чувствовать при работе с техническими сервисами. У меня есть информация по '
        'различным сервисам, которые могут пригодится в преподавании.',
        '   ',
        'Оставлю ее ниже.',
    ])
    await context.bot.send_message(chat_id=update.effective_chat.id, text=text)

    await asleep(5)

    text = '\n'.join([
        '<b>Платформы для синхронных (в режиме реального времени) онлайн-занятий</b>',
        'Обычно я использую '
        '<a href="https://telemost.yandex.ru/">Яндекс Телемост</a>, '
        '<a href="https://zoom.us/">Zoom</a>, '
        '<a href="https://meet.google.com">GoogleMeet</a>'
        ' или <a href="https://webinar.ru/">Webinar.ru</a>. У каждой из этих платформ есть бесплатный функционал и '
        'есть расширенный, '
        'по платной подписке. Прежде чем проводить занятие, проверьте, достаточно ли вам указанного функционала '
        'платформы. Например: ',
        '– времени трансляции; ',
        '– времени записи занятия; ',
        '– возможности делиться экраном, '
        'писать в чат, создавать комнаты внутри одной встречи, когда участники работают в мини-группах и т. д.',
        '   ',
        '<b>Онлайн-доски для совместной работы</b>',
        ' Инструмент, который помогает всем участникам онлайн-занятия находиться в '
        'одном пространстве — на виртуальной доске, видеть действия друг друга в режиме реального времени. ',
        'Мне '
        'нравятся <a href="https://miro.com/">Miro</a>, '
        '<a href="https://tr.padlet.com/">Padlet</a> и '
        '<a href="https://chrome.google.com/webstore/detail/jamboard/ihacalceahhliihnhclmjjghadnhhnoc?hl=ru">'
        'JamBord</a>. '
        'У них есть достаточный бесплатный функционал, с ними просто работать.',
        '   ',
        '<b>Сервисы для опросов</b>',
        ' <a href="https://kahoot.com">Kahoot</a>, '
        '<a href="https://www.typeform.com/">Typeform</a>, '
        '<a href="https://www.google.com/forms/about/">Google Forms</a>, '
        '<a href="https://cloud.yandex.ru/services/forms">Яндекс Формы</a>. Все эти сервисы я использую для создания '
        'тестов и коротких викторин. Их можно использовать как на занятии, так и после него.',
        '   ',
        'Многие платформы для '
        'проведения вебинаров имеют встроенный функционал — опросы или совместные доски. Протестируйте платформу, '
        'прежде чем проводить на ней занятие: возможно, вам не пригодятся сторонние сервисы.',
    ])

    await context.bot.send_message(chat_id=update.effective_chat.id, text=text, disable_web_page_preview=True,
                                   parse_mode=ParseMode.HTML)

    await asleep(10)

    text = 'Переходим к следующему этапу – проверке домашних работ? ' \
           'Или хотите посмотреть все разделы и выбрать подходящий?'

    buttons = [[
        InlineKeyboardButton(text='К следующему этапу!', callback_data=ANSWER_1),
    ], [
        InlineKeyboardButton(text='Хочу посмотреть все блоки и выбрать', callback_data=ANSWER_2),
    ], [
        InlineKeyboardButton(text='Буду заканчивать курс', callback_data=ANSWER_3)
    ]]
    keyboard = InlineKeyboardMarkup(buttons)
    await update.callback_query.message.reply_text(text, reply_markup=keyboard, disable_web_page_preview=True,
                                                   parse_mode=ParseMode.HTML)

    return BLOCK3_FINISH_1


async def block3_finish_2(update: Update, context: ContextTypes.DEFAULT_TYPE) -> str:
    query = update.callback_query
    await query.answer()

    text = '\n'.join([
        'Что выберем?',
    ])

    buttons = [[
        InlineKeyboardButton(text='Готовимся к занятию', callback_data=ANSWER_1),
    ], [
        InlineKeyboardButton(text='А что по домашкам?', callback_data=ANSWER_2),
        InlineKeyboardButton(text='Преподаватель тоже человек!', callback_data=ANSWER_3),
    ]]
    keyboard = InlineKeyboardMarkup(buttons)

    await update.callback_query.message.reply_text(text, reply_markup=keyboard)

    return BLOCK3_FINISH_3


block3_states = {
    BLOCK3_INTRO: [CallbackQueryHandler(block3_intro)],
    BLOCK3_INTRO_1: [CallbackQueryHandler(block3_intro_1)],
    BLOCK3_INTRO_2: [CallbackQueryHandler(block3_intro_2)],
    BLOCK3_INTRO_3: [CallbackQueryHandler(block3_intro_3)],
    BLOCK3_INTRO_4: [CallbackQueryHandler(block3_intro_4)],
    BLOCK3_INTRO_5: [CallbackQueryHandler(block3_intro_5)],
    BLOCK3_INTRO_6: [CallbackQueryHandler(block3_intro_6)],
    BLOCK3_INTRO_7: [CallbackQueryHandler(block3_intro_7)],
    BLOCK3_INTRO_8: [CallbackQueryHandler(block3_intro_8)],
    BLOCK3_INTRO_9: [CallbackQueryHandler(block3_intro_9)],
    BLOCK3_INTRO_10: [CallbackQueryHandler(block3_intro_10)],
    BLOCK3_INTRO_11: [CallbackQueryHandler(block3_intro_11)],
    BLOCK3_INTRO_12: [CallbackQueryHandler(block3_intro_12)],
    BLOCK3_INTRO_13: [CallbackQueryHandler(block3_intro_13)],
    BLOCK3_INTRO_14: [CallbackQueryHandler(block3_intro_14)],
    BLOCK3_INTRO_15: [CallbackQueryHandler(block3_intro_15_1)],
    BLOCK3_INTRO_16: [CallbackQueryHandler(block3_intro_15_2)],
    BLOCK3_INTRO_17: [CallbackQueryHandler(block3_intro_16)],
    BLOCK3_INTRO_18: [MessageHandler(filters.TEXT & ~filters.COMMAND, block3_intro_17)],
    BLOCK3_INTRO_19: [CallbackQueryHandler(block3_intro_18)],
    BLOCK3_INTRO_20: [CallbackQueryHandler(block3_intro_19)],
    BLOCK3_INTRO_21: [CallbackQueryHandler(block3_intro_20)],

    BLOCK3_CONFLICT_1: [
        CallbackQueryHandler(block3_conflict_1, pattern=ANSWER_1),
        CallbackQueryHandler(block3_conflict_7, pattern=ANSWER_5),
    ],
    BLOCK3_CONFLICT_2: [CallbackQueryHandler(block3_conflict_2)],
    BLOCK3_CONFLICT_3: [CallbackQueryHandler(block3_conflict_3)],
    BLOCK3_CONFLICT_4: [CallbackQueryHandler(block3_conflict_4)],
    BLOCK3_CONFLICT_5: [CallbackQueryHandler(block3_conflict_5)],
    BLOCK3_CONFLICT_6: [CallbackQueryHandler(block3_conflict_6)],
    BLOCK3_CONFLICT_7: [CallbackQueryHandler(block3_conflict_7)],

    BLOCK3_EXERCISES_1: [CallbackQueryHandler(block3_exercises_1)],
    BLOCK3_EXERCISES_2: [CallbackQueryHandler(block3_exercises_2)],

    BLOCK3_FINISH_1: [
        CallbackQueryHandler(block4_intro, pattern=ANSWER_1),
        CallbackQueryHandler(block3_finish_2, pattern=ANSWER_2),
        CallbackQueryHandler(block1_final, pattern=ANSWER_3),
    ],
    BLOCK3_FINISH_2: {
        CallbackQueryHandler(block1_final, pattern=ANSWER_1),
        CallbackQueryHandler(block3_finish_2, pattern=ANSWER_2),
    },
    BLOCK3_FINISH_3: [
        CallbackQueryHandler(block2_intro, pattern=ANSWER_1),
        CallbackQueryHandler(block4_intro, pattern=ANSWER_2),
        CallbackQueryHandler(block5_intro, pattern=ANSWER_3),
    ],
}
