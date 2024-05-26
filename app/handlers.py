from aiogram import F, Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message

import app.keyboard as kb

router = Router()


@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.reply(f'salom.\n your ID: {message.from_user.id}.\nUsername: @{message.from_user.username}', 
        reply_markup= await kb.inline_car())


@router.message(Command('help'))
async def get_help(message: Message):
    await message.answer('How can I help you /help')


@router.message(F.text == "How are you?")
async def how_are_you(message: Message):
    await message.answer('OK!')


@router.message(F.photo)
async def get_photo(message: Message):
    await message.answer(f" ID photo: {message.photo[-1].file_id}")


@router.message(Command('get_photo'))
async def get_photo(message: Message):
    await message.answer_photo(photo='https://cdn.pixabay.com/photo/2015/04/23/22/00/tree-736885_1280.jpg', caption='This is creator')