# Copyright (C) 2025 by Alya_Help @ Github, < https://github.com/TheTeamAlya >
# Subscribe On YT < Jankari Ki Duniya >. All rights reserved. © Alya © Yukki.

"""
TheTeamAlya is a project of Telegram bots with variety of purposes.
Copyright (c) 2021 ~ Present Team Alya <https://github.com/TheTeamAlya>

This program is free software: you can redistribute it and can modify
as you want or you can collabe if you have new ideas.
"""

from typing import Union, List
from pyrogram import filters

other_filters = filters.group & ~filters.via_bot & ~filters.forwarded
other_filters2 = filters.private & ~filters.via_bot & ~filters.forwarded


def commandpro(commands: Union[str, List[str]]):
    return filters.command(commands, "")
