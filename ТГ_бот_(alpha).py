import telebot
import sqlite3

bot = telebot.TeleBot('6987424211:AAFORNgk3wEzZDPW7OI2SvXne7uiU5gdPrM')
name = None
surname = None


@bot.message_handler(commands=['regstudent'])
def start(message):
    conn = sqlite3.connect('itproger.sql')
    cur = conn.cursor()

    cur.execute('CREATE TABLE IF NOT EXISTS users (id int auto_increment primary key, name varchar(50), surname varchar(50), pass varchar(50))')
    conn.commit()
    cur.close()
    conn.close()

    bot.send_message(message.chat.id, 'Привет, сейчас тебя зарегистрируем! Введите Ваше имя')
    bot.register_next_step_handler(message, user_name)
def user_name(message):
    global name
    name = message.text.strip()
    bot.send_message(message.chat.id, 'Введите фамилию')
    bot.register_next_step_handler(message, user_surname)
def user_surname(message):
    global surname
    surname = message.text.strip()
    bot.send_message(message.chat.id, 'Введите пароль')
    bot.register_next_step_handler(message, user_pass)
def user_pass(message):
    password = message.text.strip()

    conn = sqlite3.connect('itproger.sql')
    cur = conn.cursor()

    cur.execute(f"INSERT INTO users (name, surname, pass) VALUES ('%s', '%s', '%s')" % (name, surname, password))
    conn.commit()
    cur.close()
    conn.close()

    markup = telebot.types.InlineKeyboardMarkup()
    markup.add(telebot.types.InlineKeyboardButton('Список пользователей', callback_data='users'))
    bot.send_message(message.chat.id, 'Пользователь зарегистрирован!', reply_markup=markup)

@bot.callback_query_handler(func=lambda call: True)
def callback(call):
    conn = sqlite3.connect('itproger.sql')
    cur = conn.cursor()

    cur.execute('SELECT * FROM users')
    users = cur.fetchall()

    info = ''
    for el in users:
        info += f'Имя: {el[1]}\nФамилия: {el[2]}\nПароль: {el[3]}\n'

    cur.close()
    conn.close()

    bot.send_message(call.message.chat.id, info)

bot.polling(none_stop=True)
