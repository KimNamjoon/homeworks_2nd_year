import telebot
import conf
import markovify
from flask
import os


telebot.apihelper.proxy = {'https': 'socks5h://geek:socks@t.geekclass.ru:7777'}
bot = telebot.TeleBot("859243603:AAFGCSutKzT5Ksy4KOAEpPKMZM6zxGJ5PqA")
bot.remove_webhook()
bot.set_webhook(url="https://git.heroku.com/evening-woodland-05043.git")

app = flask.Flask(__name__)


def chain():
    with open('hg.txt', encoding='utf-8') as f:
        t = f.read()
    m = markovify.Text(t)
    return m.make_short_sentence(max_chars=200)


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.send_message(message.chat.id, 'Приветствую, трибут. Это бот, генерирующий то, как пройдут твои "Голодные Игры"!\nОт вас требуется ввести любое сообщение')

@bot.message_handler(func=lambda m: True)
def ans(message):
    bot.send_message(message.chat.id, 'И пусть удача всегда будет на вашей стороне!\n{} '.format(chain()))

@app.route("/", methods=['GET', 'HEAD'])
def index():
    return 'ok'

@app.route("/bot", methods=['POST'])
def webhook():
    if flask.request.headers.get('content-type') == 'application/json':
        json_string = flask.request.get_data().decode('utf-8')
        update = telebot.types.Update.de_json(json_string)
        bot.process_new_updates([update])
        return ''
    else:
        flask.abort(403)

if __name__ == '__main__':
    import os
    app.debug = True
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
