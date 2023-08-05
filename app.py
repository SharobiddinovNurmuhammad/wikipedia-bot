import logging
from config import API_TOKEN
from aiogram import Bot, Dispatcher, executor, types
from keyboards import wikisearchbtn
from functions import wikisearch, wikiloops, wikiresult


# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.reply("Hi!\nI'm EchoBot!\nPowered by aiogram.", parse_mode='HTML')


@dp.message_handler()
async def wikibot(message: types.Message):
    msg = message.text
    arr = await wikisearch(msg)
    text = await wikiloops(arr)
    await message.answer(text=text, reply_markup=wikisearchbtn(arr), parse_mode='HTML')


@dp.callback_query_handler()
async def wikipages(call: types.CallbackQuery):
    text = call.data
    print(text)
    text = await wikiresult(text)
    await call.message.answer(text, parse_mode='HTML')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)