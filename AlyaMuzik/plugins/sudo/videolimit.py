# Copyright (C) 2025 by Alya_Help @ Github, < https://github.com/TheTeamAlya >
# Subscribe On YT < Jankari Ki Duniya >. All rights reserved. © Alya © Yukki.

"""
TheTeamAlya is a project of Telegram bots with variety of purposes.
Copyright (c) 2021 ~ Present Team Alya <https://github.com/TheTeamAlya>

This program is free software: you can redistribute it and can modify
as you want or you can collabe if you have new ideas.
"""


from pyrogram import filters
from pyrogram.types import Message

from strings import get_command
from AlyaMuzik import app
from AlyaMuzik.misc import SUDOERS
from AlyaMuzik.utils.database import set_video_limit
from AlyaMuzik.utils.decorators.language import language

VIDEOLIMIT_COMMAND = get_command("VIDEOLIMIT_COMMAND")


@app.on_message(filters.command(VIDEOLIMIT_COMMAND) & SUDOERS)
@language
async def set_video_limit_kid(client, message: Message, _):
    if len(message.command) != 2:
        usage = _["vid_1"]
        return await message.reply_text(usage)
    message.chat.id
    state = message.text.split(None, 1)[1].strip()
    if state.lower() == "disable":
        limit = 0
        await set_video_limit(limit)
        return await message.reply_text(_["vid_4"])
    if state.isnumeric():
        limit = int(state)
        await set_video_limit(limit)
        if limit == 0:
            return await message.reply_text(_["vid_4"])
        await message.reply_text(_["vid_3"].format(limit))
    else:
        return await message.reply_text(_["vid_2"])
