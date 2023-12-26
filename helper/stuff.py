#    This file is part of the CompressorBot distribution.
#    Copyright (c) 2021 Danish_00
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, version 3.
#
#    This program is distributed in the hope that it will be useful, but
#    WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
#    General Public License for more details.
#
#    License can be found in < https://github.com/1Danish-00/CompressorBot/blob/main/License> .

from .worker import *


async def up(event):
    if not event.is_private:
        return
    stt = dt.now()
    ed = dt.now()
    v = ts(int((ed - uptime).seconds) * 1000)
    ms = (ed - stt).microseconds / 1000
    p = f"🌋Pɪɴɢ = {ms}ms"
    await event.reply(v + "\n" + p)


async def start(event):
    ok = await event.client(GetFullUserRequest(event.sender_id))
    await event.reply(
        f"Hi `{event.sender.first_name}`\nThis is A CompressorBot Which Can Encode Videos.\nReduce Size of Videos With Negligible Quality Change\nU can Generate Samples/screenshots too/n/n ♥ Bot By:- @Matiz_Techz",
        buttons=[
            [Button.inline("🦋 Hᴇʟᴘ", data="ihelp")],
            [
                Button.url("👩‍💻 Dᴇᴠᴇʟᴏᴘᴇʀ", url="t.me/Md_Matin_Ashraf"),
                Button.url("📡 Leech Group", url="t.me/Matiz_Techz/156"),
            ],
        ],
    )


async def help(event):
    await event.reply(
        "**🐠 A Quality CompressorBot**\n\n+This Bot Compress Videos With Negligible Quality Change.\n+Generate Sample Compressed Video\n+Easy to Use\n-Due to Quality Settings Bot Takes Time To Compress.\nSo Be patience Nd Send videos One By One After Completing.\nDont Spam Bot.\n\nJust Forward Video To Get Options"
    )


async def ihelp(event):
    await event.edit(
        "**🐠 A Quality CompressorBot**\n\n+This Bot Compress Videos With Negligible Quality Change.\n+Generate Sample Compressed Video\n+Screenshots Too\n+Easy to Use\n-Due to Quality Settings Bot Takes Time To Compress.\nSo Be patience Nd Send videos One By One After Completing.\nDont Spam Bot.\n\nJust Forward Video To Get Options",
        buttons=[Button.inline("»»Bᴀᴄᴋ««", data="beck")],
    )


async def beck(event):
    ok = await event.client(GetFullUserRequest(event.sender_id))
    await event.edit(
        f"Hi `{event.sender.first_name}`\nThis is A CompressorBot Which Can Encode Videos.\nReduce Size of Videos With Negligible Quality Change\nU can Generate Samples/screenshots too/n/n ♥ Bot By:- @Matiz_Techz",
        buttons=[
            [Button.inline("🦋 Hᴇʟᴘ", data="ihelp")],
            [
                Button.url("👩‍💻 Dᴇᴠᴇʟᴏᴘᴇʀ", url="t.me/Md_Matin_Ashraf"),
                Button.url("📡 Leech Group", url="t.me/Matiz_Techz/156"),
            ],
        ],
    )


async def sencc(e):
    key = e.pattern_match.group(1).decode("UTF-8")
    await e.edit(
        "• Choose Mode Baby 😅\n➔ Default For Compress Direct\n➔ Custom Compress Means, You Set Add Custom File Name And Custom Thumbnail",
        buttons=[
            [
                Button.inline("Default Compress", data=f"encc{key}"),
                Button.inline("Custom Compress", data=f"ccom{key}"),
            ],
            [Button.inline("»»Bᴀᴄᴋ««", data=f"back{key}")],
        ],
    )


async def back(e):
    key = e.pattern_match.group(1).decode("UTF-8")
    await e.edit(
        "🐠  **What To Do** 🐠",
        buttons=[
            [
                Button.inline("📽 Gᴇɴᴇʀᴀᴛᴇ Sᴀᴍᴘʟᴇ", data=f"gsmpl{key}"),
                Button.inline("🖼 Screenshots", data=f"sshot{key}"),
            ],
            [Button.inline("🗜 Cᴏᴍᴘʀᴇss", data=f"sencc{key}")],
        ],
    )


async def ccom(e):
    await e.edit("Send Ur Custom Name For That File")
    wah = e.pattern_match.group(1).decode("UTF-8")
    wh = decode(wah)
    out, dl, thum, dtime = wh.split(";")
    chat = e.sender_id
    async with e.client.conversation(chat) as cv:
        reply = cv.wait_event(events.NewMessage(from_users=chat))
        repl = await reply
        if "." in repl.text:
            q = repl.text.split(".")[-1]
            g = repl.text.replace(q, "mkv")
        else:
            g = repl.text + ".mkv"
        outt = f"encode/{chat}/{g}"
        x = await repl.reply(
            f"Custom File Name : {g}\n\nNow Send Thumbnail Picture For it."
        )
        replyy = cv.wait_event(events.NewMessage(from_users=chat))
        rep = await replyy
        if rep.media:
            tb = await e.client.download_media(rep.media, f"thumb/{chat}.jpg")
        elif rep.text and not (rep.text).startswith("/"):
            url = rep.text
            os.system(f"wget {url}")
            tb = url.replace("https://telegra.ph/file/", "")
        else:
            tb = thum
        omk = await rep.reply(f"Thumbnail {tb} Setted Successfully ✅")
        hehe = f"{outt};{dl};{tb};{dtime}"
        key = code(hehe)
        await customenc(omk, key)
