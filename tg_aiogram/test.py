import asyncio
import logging
from aiogram.enums.parse_mode import ParseMode
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters.command import Command, CommandStart
from config import settings
import requests as req
from bs4 import BeautifulSoup

bot = Bot(token=settings['TOKEN'], parse_mode=ParseMode.HTML)
dp = Dispatcher()


@dp.message(CommandStart())
async def start(message: types.Message):
    await message.answer('/winner')


@dp.message(Command('git'))
async def git_name(message: types.Message):
    a = message.text.split(' ')
    response = req.get(f"https://api.github.com/users/{a[1]}").json()
    list = []
    for i in response:
        await message.answer(i + ":", response[f'{i}'])




@dp.message(Command('winner'))
async def winner(message: types.Message):

    a = message.text.split(' ')
    await message.answer(a[1])

    response = req.get("https://api.github.com/users/")
    # soup = BeautifulSoup(response.text,"html")
    print(response.json())



@dp.message(Command('id'))
async def id(message: types.Message, bot: Bot):
    id = message.chat.id
    await bot.send_message(message.chat.id, f"{id}")




#------------Запуск__________________-
async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())

