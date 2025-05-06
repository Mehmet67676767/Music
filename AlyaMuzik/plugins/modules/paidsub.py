# Copyright (C) 2025 by Alya_Help @ Github, < https://github.com/TheTeamAlya >
# Subscribe On YT < Jankari Ki Duniya >. All rights reserved. © Alya © Yukki.

"""
TheTeamAlya is a project of Telegram bots with variety of purposes.
Copyright (c) 2021 ~ Present Team Alya <https://github.com/TheTeamAlya>

This program is free software: you can redistribute it and can modify
as you want or you can collabe if you have new ideas.
"""


import asyncio
from AlyaMuzik import app
from pyrogram import Client, filters
from datetime import datetime, timedelta
from pyrogram.errors import FloodWait
from AlyaMuzik.core.mongo import db as alexa
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from AlyaMuzik.utils.database import get_served_users, get_served_chats


OWNER_ID = 6174058850
