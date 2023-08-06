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
    title = f"<b>{msg}</b>\n\n"
    text = f"<i>{wikipedia.summary(msg)}</i>"
    url = wikipedia.page(msg).url
    arr = [title, text, url]
    return arr

