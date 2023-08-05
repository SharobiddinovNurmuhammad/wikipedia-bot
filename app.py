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

# /start commandasi uchun handlar
@dp.message_handler(commands='start')
async def start(message: types.Message):
    text = f"Assalomu alaykum <b>{message.from_user.full_name}</b>, Wikisearch botga xush kelibsiz!\nBotdan qanday foydalanishni bilish uchun /help buyrug'ini kiriting!"
    await message.reply(text=text, parse_mode='HTML')

# /help commadasi uchun handlar
@dp.message_handler(commands='help')
async def help(message: types.Message):
    text = "Wikisearch dan foydalanish uchun botga maqolangizga oid biror kalit so'z yuboring:\n<b>Misol uchun:</b>\nPython\nSalom\nKitob va h.k.lar.. "
    await message.reply(text=text, parse_mode='HTML')

@dp.message_handler()
async def wikibot(message: types.Message):
    msg = message.text
    arr = await wikisearch(msg)
    text = await wikiloops(arr)
    if len(wikisearchbtn(arr)['inline_keyboard']) == 0:
        await message.answer("Bunday kalit so'zga oid maqola topilmadi!")
    else:
        await message.answer(text=text, reply_markup=wikisearchbtn(arr), parse_mode='HTML')
        

@dp.callback_query_handler()
async def wikipages(call: types.CallbackQuery):
    text = call.data
    await call.answer(text="⏳Biroz kutib turing maqola qidirilmoqda...")
    text = await wikiresult(text)
    await call.message.answer(text, parse_mode='HTML')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)