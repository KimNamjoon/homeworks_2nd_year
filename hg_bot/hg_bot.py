import telebot
import conf
import markovify
from flask
import os


bot = telebot.TeleBot("859243603:AAFGCSutKzT5Ksy4KOAEpPKMZM6zxGJ5PqA")


def chain(): #хоба, вот функция для цепи
    with open('hg.txt', encoding='utf-8') as f: #открываем войну и мир
        t = f.read() #читаем войну и мир в переменную
    m = markovify.Text(t) #хоп, тренируем цепь на тексе
    return m.make_short_sentence(max_chars=200) #генерим предложение в макс 200 символов длиной и отдаем его


@bot.message_handler(commands=['start', 'help']) #команды бота пошли - эта говорит ему вот так отвечать на /start или /help
def send_welcome(message):
    bot.send_message(message.chat.id, 'Приветствую, трибут. Это бот, генерирующий то, как пройдут твои "Голодные Игры"!\nОт вас требуется ввести любое сообщение')

@bot.message_handler(func=lambda m: True)
def ans(message):
    bot.send_message(message.chat.id, 'И пусть удача всегда будет на вашей стороне!\n{} '.format(chain()))


if __name__ == '__main__':
    import os
    app.debug = True
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
