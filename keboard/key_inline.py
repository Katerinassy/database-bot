from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def get_keyboard_1_inline():
    keyboard_inline = InlineKeyboardMarkup(row_width=2)
    but_inline = InlineKeyboardButton('Приобрести', url='https://auto.ru/moskva/cars/bmw/m5/all/')
    but_inline2 = InlineKeyboardButton('Посмотреть информацию', url='https://www.bmw.ru/ru/all-models/m-series/m5-sedan/2021/bmw-5-series-sedan-m-automobiles-overview.html')
    keyboard_inline.add(but_inline, but_inline2)

    return keyboard_inline

def get_keyboard_2_inline():
    keyboard_inline2 = InlineKeyboardMarkup(row_width= 2)
    but_inline3 = InlineKeyboardButton('Приобрести', url='https://auto.ru/moskva/cars/dodge/ram/used/')
    but_inline4 = InlineKeyboardButton('Посмотреть информацию', url='https://ru.wikipedia.org/wiki/Ram_Trucks')
    keyboard_inline2.add(but_inline3, but_inline4)

    return keyboard_inline2