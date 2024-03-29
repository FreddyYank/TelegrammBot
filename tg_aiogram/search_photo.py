import asyncio
import logging
from aiogram.enums.parse_mode import ParseMode
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters.command import Command, CommandStart
from config import settings
from icrawler.builtin import GoogleImageCrawler


bot = Bot(token=settings['TOKEN'], parse_mode=ParseMode.HTML)
dp = Dispatcher()

@dp.message(Command('search'))
async def serach_photo(message: types.Message):
    crawler = GoogleImageCrawler(storage={'tg_aiogram':'./img'})
    crawler.crawl(keyword=f'{message.text}',max_num=2)

#------------Запуск__________________-
async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())

