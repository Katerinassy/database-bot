from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


def get_keyboard_1():
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    button_1 = KeyboardButton('Предсказание')
    button_2 = KeyboardButton('Отправь фото машины - BMW M5')
    button_3 = KeyboardButton('Перейти на следующую клавиатуру')
    keyboard.add(button_1, button_2, button_3)
    return keyboard

def get_keyboard_2():
    keyboard_2 = ReplyKeyboardMarkup(resize_keyboard=True)
    button_4 = KeyboardButton('Отправь фото машины - RAM')
    button_5 = KeyboardButton('Вернуться на 1 клавиатуру')
    keyboard_2.add(button_4,button_5)
    return keyboard_2
