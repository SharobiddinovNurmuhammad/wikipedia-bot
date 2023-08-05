import wikipedia

wikipedia.set_lang('uz')

async def wikisearch(msg: str) -> list:
    arr = wikipedia.search(msg)
    return arr

async def wikiloops(arr: list, text='', count=0)-> str:
    text = f"<b>Topilgan maqolalar:\n</b>"
    for i in arr:
        count += 1
        text += f"<b>{count}</b>. {i}\n"
    return text

async def wikiresult(msg: str) -> str:
    text = f"<b>{msg}</b>\n\n"
    text += wikipedia.summary(msg)
    return text

