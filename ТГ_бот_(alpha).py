import telebot
from telebot import types

bot = telebot.TeleBot('6568755149:AAELZ9yLNm56n3jsGDFoZhJlkxnq1LJTsGc')


@bot.message_handler(commands=['старт'])
def start(massage):
    bot.send_message(massage.chat.id, "Добро пожаловать в студенческий бот NewSunrise", parse_mode='html')


@bot.message_handler(content_types=['text'])
def get_user_text(massage):
    if massage.text == "Привет":
        bot.send_message(massage.chat.id, 'и тебе привет!', parse_mode='html')
    elif massage.text == 'id':
        bot.send_message(massage.chat.id, f'Твой ID: {massage.from_user.id}', parse_mode='html')
    elif massage.text == "photo":
        photo = open("int.png", 'rb')
        bot.send_photo(massage.chat.id, photo)
    else:
        bot.send_message(massage.chat.id, 'Я тебя не понимаю', parse_mode='html')

@bot.message_handler(content_types=['photo'])
def get_user_photo(massage):
    bot.send_message(massage.chat.id,"Вау, крутое фото!")

@bot.message_handler(commands=['website'])
def website (massage):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('Посетить веб сайт', url ='https://itproger.com'))
    bot.send_message(massage.chat.id, "Передите на сайт!",reply_markup= markup)

bot.polling(none_stop=True)

## @NewSunrise4_bot - токен этого бота
