import asyncio
import logging

from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from config import TOKEN


bot = Bot(token=TOKEN)
dp  = Dispatcher()


@dp.message(CommandStart())
async def cmd_start(message: Message):
    await message.reply(f'salom.\n your ID: {message.from_user.id}.\nUsername: @{message.from_user.username}')


@dp.message(Command('help'))
async def get_help(message: Message):
    await message.answer('How can I help you /help')


@dp.message(F.text == "How are you?")
async def how_are_you(message: Message):
    await message.answer('OK!')


@dp.message(F.photo)
async def get_photo(message: Message):
    await message.answer(f" ID photo: {message.photo[-1].file_id}")


@dp.message(Command('get_photo'))
async def get_photo(message: Message):
    await message.answer_photo(photo='https://cdn.pixabay.com/photo/2015/04/23/22/00/tree-736885_1280.jpg', caption='This is creator')


async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Exit')