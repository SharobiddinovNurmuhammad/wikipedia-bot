import wikipedia

wikipedia.set_lang('uz')

async def wikisearch(msg: str)-> str:
    arr = wikipedia.search(msg)
    return arr

async def wikiloops(arr: list, text='', count=0)-> str:
    text = f"Topilgan maqolalar:\n"
    for i in arr:
        count += 1
        text += f"{count}. {i}\n"
    return text

async def wikiresult(msg: str) -> str:
    text = f"-<b>{msg}</b>\n\n"
    text += wikipedia.summary(msg)
    return text

