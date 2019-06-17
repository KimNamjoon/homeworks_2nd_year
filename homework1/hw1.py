import re
import random

def choice():
    topic = input('Выберите тему: \n 1. Специи \n 2. Греческие боги \n 3. Цветы \n')
    while topic != '1' and topic != '2' and topic != '3': #проверяем выбрал ли игрок тему
        print('Тема не найдена.')
        topic = input('Выберите тему: \n 1. Специи \n 2. Греческие боги \n 3. Цветы \n')
    return topic

def r_choice(topic): #читаем файл со словами и сразу выбираем случайное (до меня дошло, что можно было называть списки слов цифрами после написания кучи if-ов...)
    if topic == '1':
        with open('специи.txt', encoding = 'utf-8') as f:
            text = f.readlines()
    if topic == '2':
        with open('греческие_боги.txt', encoding = 'utf-8') as f:
            text = f.readlines()
    if topic == '3':
        with open('цветы.txt', encoding = 'utf-8') as f:
            text = f.readlines()
    rc = random.choice(text)
    return rc

##def check_it(g): #проверка символа на пригодность (буква, кириллица)
##    if g not in 'ёйцукенгшщзхъфывапролджэячсмитьбю'
##        print('Введите букву!')

def gallows(rc):
    i = 0 #индекс для хождения по слову
    miss = [] #попытки (буквы)
    spaces = '_ '*len(rc) #прочерки
    print('Вы должны угадать слово из ',len(rc),' букв. У Вас есть 6 попыток. Удачи!' )
    print(spaces)
    с = 6 #c - counter для попыток
    while c > 0:
        trying = input('Введите букву: ').lower()
        if trying not in 'йцукенгшщзхъфывапролджэячсмитьбюё':
            print('Введите букву русского алфавита!')
        if trying in already_tried:
            print('Вы уже вводили эту букву!')
        if trying not in rc:
            print('Этой буквы нет в слове!')
            c -= 1
            i += 1
        else:
            co = 0 #очередной счетчик
            for letter in rc:
                if trying == letter:
                    spaces[co] == spaces
                    spaces = spaces[:1]+ trying + spaces[i+1]
                else:
                    co += 1
        print(letter)
    miss.append(trying)
    if c == 0:
        print('У Вас кончились попытки!')


def main():
    topic = choice()
    rc = r_choice(topic)
    gallows(rc)

main()
