from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def wikiSearchBtn(arr):
    recent_wiki = InlineKeyboardMarkup(row_width=5)
    inline_buttons = [InlineKeyboardButton(text=f"{i+1}", callback_data=f"{arr[i]}") for i in range(len(arr))]
    recent_wiki.add(*inline_buttons)
    return recent_wiki

