# -*- coding: utf-8 -*-

import telebot
import conf
import markovify
import flask
import os

bot = telebot.TeleBot("859243603:AAFGCSutKzT5Ksy4KOAEpPKMZM6zxGJ5PqA")

app = flask.Flask(__name__)

def chain():
    with open('hg.txt', encoding='utf-8') as f:
        t = f.read()
    m = markovify.Text(t)
    return m.make_short_sentence(max_chars=200)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.send_message(message.chat.id, '�����������. ��� ���, ������� ���������� ����� �� ������ ����� ���� � �������� �����.\n �������� � ����� �����-������ �����.')

@bot.message_handler(func=lambda m: True)
def ans(message):
    bot.send_message(message.chat.id, '� ����� ����� ������ ����� �� ����� �������!\n{} '.format(chain()))

bot.polling(none_stop = True)

if __name__ == '__main__':
    import os
    app.debug = True
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
