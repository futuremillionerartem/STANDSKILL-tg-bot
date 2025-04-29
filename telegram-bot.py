import telebot
from telebot import types



bot_token = "YOR_TOKEN"
bot = telebot.TeleBot(bot_token)
url = 'https://t.me/+-btZ8kkHuBVjZjJi'

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
    btn1 = types.KeyboardButton('💰 ГОЛДА')
    btn2 = types.KeyboardButton('✍️ ОТЗЫВЫ')
    btn3 = types.KeyboardButton('👨‍💻 САЙТ')
    btn4 = types.KeyboardButton('📖 ПОДДЕРЖКА')
    markup.add(btn1, btn2, btn3, btn4)
    bot.send_message(message.chat.id, 'Спасибо что выбрали нас! \nВыберите в меню, что хотите сделать', reply_markup=markup)

def summa(message):

    if message.text == '⬅ ГЛАВНОЕ МЕНЮ':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('💰 ГОЛДА')
        btn2 = types.KeyboardButton('✍️ ОТЗЫВЫ')
        btn3 = types.KeyboardButton('👨‍💻 САЙТ')
        btn4 = types.KeyboardButton('📖 ПОДДЕРЖКА')
        markup.add(btn1, btn2, btn3, btn4)
        bot.send_message(message.chat.id, 'Спасибо что выбрали нас! \nВыберите в меню, что хотите сделать', reply_markup=markup)

    if message.text != '⬅ ГЛАВНОЕ МЕНЮ':
        if message.text.isnumeric():
            itog = int(message.text)
            number = itog // 0.7
            markup = types.InlineKeyboardMarkup()
            btn_inline2 = types.InlineKeyboardButton(text='СВЯЗАТЬСЯ', url='https://t.me/americadreamX')
            markup.add(btn_inline2)
            text_by = bot.send_message(message.chat.id, f'💵 Сумма: {itog} ₽\n💰 Вы получаете: {number} золота\n\n\nНажмите кнопку "СВЯЗАТЬСЯ" для покупки голды', reply_markup=markup)
            bot.register_next_step_handler(text_by, summa)

        else:
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            back = types.KeyboardButton('⬅ ГЛАВНОЕ МЕНЮ')
            markup.add(back)
            text_wrong = bot.send_message(message.chat.id, 'Введите целое число', reply_markup=markup)
            bot.register_next_step_handler(text_wrong, summa)


def summa2(message):

    if message.text == '⬅ ГЛАВНОЕ МЕНЮ':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('💰 ГОЛДА')
        btn2 = types.KeyboardButton('✍️ ОТЗЫВЫ')
        btn3 = types.KeyboardButton('👨‍💻 САЙТ')
        btn4 = types.KeyboardButton('📖 ПОДДЕРЖКА')
        markup.add(btn1, btn2, btn3, btn4)
        bot.send_message(message.chat.id, 'Спасибо что выбрали нас! \nВыберите в меню, что хотите сделать', reply_markup=markup)

    if message.text != '⬅ ГЛАВНОЕ МЕНЮ':
        if message.text.isnumeric():
            itog2 = int(message.text)
            number2 = itog2 * 0.45
            markup = types.InlineKeyboardMarkup()
            btn_inline2 = types.InlineKeyboardButton(text='СВЯЗАТЬСЯ', url='https://t.me/americadreamX')
            markup.add(btn_inline2)
            text_sell = bot.send_message(message.chat.id, f'💰 Сумма: {itog2} Золота\n💵 Вы получаете: {number2} ₽\n\n\nНажмите кнопку "СВЯЗАТЬСЯ" для продажи голды', reply_markup=markup)
            bot.register_next_step_handler(text_sell, summa2)

        else:
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            back = types.KeyboardButton('⬅ ГЛАВНОЕ МЕНЮ')
            markup.add(back)
            text_wrong2 = bot.send_message(message.chat.id, 'Введите целое число', reply_markup=markup)
            bot.register_next_step_handler(text_wrong2, summa2)


@bot.message_handler(content_types=['text'])
def bot_message(message):
    if message.chat.type == 'private':
        if message.text == '💰 ГОЛДА':
            markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
            btn4 = types.KeyboardButton('💳 КУПИТЬ')
            btn5 = types.KeyboardButton('💳 ПРОДАТЬ')
            back = types.KeyboardButton('⬅ ГЛАВНОЕ МЕНЮ')
            markup.add(btn4, btn5)
            markup.add(back)
            bot.send_message(message.chat.id, 'Выберите действие в меню', reply_markup=markup)

        if message.text == '✍️ ОТЗЫВЫ':
            markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
            back = types.KeyboardButton('⬅ ГЛАВНОЕ МЕНЮ')
            markup.add(back)
            bot.send_message(message.chat.id, f'Наши отзывы: {url}', reply_markup=markup)

        if message.text == '👨‍💻 САЙТ':
            markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
            back = types.KeyboardButton('⬅ ГЛАВНОЕ МЕНЮ')
            markup.add(back)
            bot.send_message(message.chat.id, f'🛠 Извините но в данный момент сайт находиться в разработке', reply_markup=markup)

        if message.text == '📖 ПОДДЕРЖКА':
            markup = types.InlineKeyboardMarkup()
            btn_inline = types.InlineKeyboardButton(text='НАПИСАТЬ', url='https://t.me/americadreamX')
            markup.add(btn_inline)
            bot.send_message(message.chat.id, f'Задайте свой конкретный вопрос \nадминистратору в чат по кнопке "НАПИСАТЬ" \nи через некоторое время Вам поступит ответ!', reply_markup=markup)

        if message.text == '⬅ ГЛАВНОЕ МЕНЮ':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn1 = types.KeyboardButton('💰 ГОЛДА')
            btn2 = types.KeyboardButton('✍️ ОТЗЫВЫ')
            btn3 = types.KeyboardButton('👨‍💻 САЙТ')
            btn4 = types.KeyboardButton('📖 ПОДДЕРЖКА')
            markup.add(btn1, btn2, btn3, btn4)
            bot.send_message(message.chat.id, 'Спасибо что выбрали нас! \nВыберите в меню, что хотите сделать', reply_markup=markup)


        if message.text == '💳 КУПИТЬ':
            file_rub = open('img/rub.jpg', 'rb')
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            back = types.KeyboardButton('⬅ ГЛАВНОЕ МЕНЮ')
            markup.add(back)
            sent = bot.send_photo(message.chat.id, file_rub, f'Введите сумму в рублях: ', reply_markup=markup)
            bot.register_next_step_handler(sent, summa)



        if message.text == '💳 ПРОДАТЬ':
            file_gold = open('img/gold.jpg', 'rb')
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            back = types.KeyboardButton('⬅ ГЛАВНОЕ МЕНЮ')
            markup.add(back)
            sent2 = bot.send_photo(message.chat.id, file_gold, f'Введите количество голды: ', reply_markup=markup)
            bot.register_next_step_handler(sent2, summa2)





bot.polling(none_stop=True, interval=0)

