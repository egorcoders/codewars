# my solution
# best solution

def rot13(s):
    # Строка из ожидаемых букв
    chars = "abcdefghijklmnopqrstuvwxyz"
    # Строка из смещённых букв на 13 шагов вперёд
    trans = chars[13:] + chars[:13]
    # Ищем индекс буквы из первой строки, а потом букву по
    # индексу из второй. Если нет такой буквы, возвращаем её
    rot_char = lambda c: trans[chars.find(c)] if chars.find(c) > -1 else c
    # Проходимся по строке и объединяем значения полученного списка
    return ''.join(
        rot_char(c.lower()).upper() if c.isupper()
        else rot_char(c)
        for c in s
    )

import codecs
from curses.ascii import isupper


def rot13_0(message):  # cheating way
    return codecs.encode(message, 'rot13')


import string
from codecs import encode as _dont_use_this_
from string import maketrans, lowercase, uppercase


def rot13_1(message):
    lower = maketrans(lowercase, lowercase[13:] + lowercase[:13])
    upper = maketrans(uppercase, uppercase[13:] + uppercase[:13])
    return message.translate(lower).translate(upper)


def rot13_2(message):
    rot13 = str.maketrans(
        'ABCDEFGHIJKLMabcdefghijklmNOPQRSTUVWXYZnopqrstuvwxyz',
        'NOPQRSTUVWXYZnopqrstuvwxyzABCDEFGHIJKLMabcdefghijklm')
    message.translate(rot13)
