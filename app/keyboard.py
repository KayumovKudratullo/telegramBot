from aiogram.types import ReplyKeyboardMarkup,KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup

from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder

main = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Catalog')],
    [KeyboardButton(text='Cart'), (KeyboardButton(text='Contact'))]
],
resize_keyboard= True,
input_field_placeholder="Feel free to write")


settings = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='telegram', url='https://t.me/qayumovvvvvv')],
    [InlineKeyboardButton(text='Github', url='https://github.com/qayumovvvvvv'), InlineKeyboardButton(text="What's up", url='https://wa.me/qr/5JZCOCHHSKGJK1')]
])


cars = ['Tesla', 'Mercedes', 'BMW', 'Matiz', 'Gentra']

async def inline_car():
    keyboard = InlineKeyboardBuilder()
    for car in cars:
        keyboard.add(InlineKeyboardButton(text=car, url='https://github.com/qayumovvvvvv'))
    return keyboard.adjust(2).as_markup()