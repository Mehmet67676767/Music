# Copyright (C) 2025 by Alya_Help @ Github, < https://github.com/TheTeamAlya >
# Subscribe On YT < Jankari Ki Duniya >. All rights reserved. © Alya © Yukki.

"""
TheTeamAlya is a project of Telegram bots with variety of purposes.
Copyright (c) 2021 ~ Present Team Alya <https://github.com/TheTeamAlya>

This program is free software: you can redistribute it and can modify
as you want or you can collabe if you have new ideas.
"""


import asyncio
import importlib
from typing import Any

from pyrogram import idle
from pytgcalls.exceptions import NoActiveGroupCall

import config
from config import BANNED_USERS
from AlyaMuzik import LOGGER, app, userbot
from AlyaMuzik.core.call import Alya
from AlyaMuzik.misc import sudo
from AlyaMuzik.plugins import ALL_MODULES
from AlyaMuzik.utils.database import get_banned_users, get_gbanned
from AlyaMuzik.core.cookies import save_cookies


async def init() -> None:
    # Check for at least one valid Pyrogram string session
    if all(not getattr(config, f"STRING{i}") for i in range(1, 6)):
        LOGGER("AlyaMuzik").error("Add Pyrogram string session and then try...")
        exit()
    await sudo()
    try:
        for user_id in await get_gbanned():
            BANNED_USERS.add(user_id)
        for user_id in await get_banned_users():
            BANNED_USERS.add(user_id)
    except:
        pass
    await app.start()
    await save_cookies()
    for module in ALL_MODULES:
        importlib.import_module("AlyaMuzik.plugins" + module)
    LOGGER("AlyaMuzik.plugins").info("Necessary Modules Imported Successfully.")
    await userbot.start()
    await Alya.start()
    try:
        await Alya.stream_call("https://telegra.ph/file/b60b80ccb06f7a48f68b5.mp4")
    except NoActiveGroupCall:
        LOGGER("AlyaMuzik").error(
            "[ERROR] - \n\nTurn on group voice chat and don't put it off otherwise I'll stop working thanks."
        )
        exit()
    except:
        pass
    await Alya.decorators()
    LOGGER("AlyaMuzik").info("Alya Music Bot Started Successfully")
    await idle()
    await app.stop()
    await userbot.stop()
    LOGGER("AlyaMuzik").info("Stopping Alya Music Bot...")


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(init())
    LOGGER("AlyaMuzik").info("Stopping Music Bot")
