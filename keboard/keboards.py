from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

def get_keyboard_1():
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    button_1 = KeyboardButton('Ссылка на Эйфелеву башню')
    button_2 = KeyboardButton('Перейти на следующую клавиатуру')
    button_3 = KeyboardButton('Ссылка на Великую Китайскую стену')
    button_4 = KeyboardButton('Ссылка на Статую Свободы')
    button_5 = KeyboardButton('Ссылка на Пирамиды')
    keyboard.add(button_1, button_2, button_3, button_4, button_5)
    return keyboard

def get_keyboard_2():
    keyboard_2 = ReplyKeyboardMarkup(resize_keyboard=True)
    button_3 = KeyboardButton('Ссылка на Колизей')
    button_4 = KeyboardButton('Перейти назад')
    button_5 = KeyboardButton('Ссылка на Тадж-Махал')
    button_6 = KeyboardButton('Ссылка на Сиднейский оперный театр')
    button_7 = KeyboardButton('Ссылка на Кремль')
    keyboard_2.add(button_3, button_4, button_5, button_6, button_7)
    return keyboard_2