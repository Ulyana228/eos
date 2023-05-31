from aiogram import Bot, Dispatcher, executor, types
from aiogram.types.web_app_info import WebAppInfo
bot = Bot('6077384165:AAHKlZuSJAAoFxOPWCglGsZECW4EbRLXLxw')
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    markup = types.ReplyKeyboardMarkup()
    markup.add(types.KeyboardButton('открыть веб-страницу', web_app=WebAppInfo(url='https://index.html/')))
    await message.answer('Добрый день! Вас приветсвует компания ЭОСТех. Для начала работы пройдите регистрацию пользователя', reply_markup=markup)
executor.start_polling(dp)


#bot = telebot.TeleBot('6077384165:AAHKlZuSJAAoFxOPWCglGsZECW4EbRLXLxw')

# # name = None
#
# @bot.message_handler(commands=['site', 'website'])
# def site(message):
#     webbrowser.open('https://eos.ru/')
#
# @bot.message_handler(commands=['start', 'main', 'hello'])
# def start(message):
#     conn = sqlite3.connect('eostex.sql')
#     cur = conn.cursor()
#
#     cur.execute('CREATE TABLE IF NOT EXISTS users (id int auto_increment primery key, name varchar(255), pass varchar(255)) ')
#     conn.commit()
#     cur.close()
#     conn.close()
#
#     bot.send_message(message.chat.id, 'Добрый день! Вас приветсвует компания ЭОСТех. Для начала работы пройдите регистрацию пользователя. Введите ваше имя:')
#     bot.register_next_step_handler(message, user_name)
#
#     def user_name(message):
#     global name
#     name = message.text.strip()
#     bot.send_message(message.chat.id,'Введите пароль:')
#     bot.register_next_step_handler(message, user_pass)
#
#     def user_pass(message):
#         password = message.text.strip()
#         conn = sqlite3.connect('eostex.sql')
#         cur = conn.cursor()
#         cur.execute(f'INSERT INTO users (name, pass) VALUES ({name}, {password})')
#         conn.commit()
#         cur.close()
#         conn.close()
#
#         # markup = telebot.types.InlineKeyboardMarkup()
#         # markup.add(telebot.types.InlineKeyboardMarkup)
#         bot.send_message(message.chat.id, 'Пользователь зарегистрирован')
#
#
#
#     #bot.send_message(message.chat.id, f'Добрый день, {message.from_user.first_name} {message.from_user.last_name}! Вас приветствует компания "ЭОСТех"')
#
# @bot.message_handler(commands=['help'])
# def main(message):
#     bot.send_message(message.chat.id, 'По всем интересующим вас вопросам обратитесь в поддержку по номеру +7(495) 221-24-31')
#
# @bot.message_handler()
# def info(message):
#     if message.text.lower() == 'привет':
#         bot.send_message(message.chat.id, f'Добрый день, {message.from_user.first_name} {message.from_user.last_name}! Вас приветствует компания "ЭОСТех"')
#     elif message.text.lower() == 'id':
#         bot.reply_to(message, f'ID: {message.from_user.id}')


# bot.infinity_polling()
