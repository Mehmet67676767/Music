# Copyright (C) 2025 by Alya_Help @ Github, < https://github.com/TheTeamAlya >
# Subscribe On YT < Jankari Ki Duniya >. All rights reserved. © Alya © Yukki.

"""
TheTeamAlya is a project of Telegram bots with variety of purposes.
Copyright (c) 2021 ~ Present Team Alya <https://github.com/TheTeamAlya>

This program is free software: you can redistribute it and can modify
as you want or you can collabe if you have new ideas.
"""


from os import listdir, mkdir
from os.path import isdir
from shutil import rmtree

from ..logging import LOGGER


def dirr():
    current_items = listdir()

    if "assets" not in current_items:
        LOGGER(__name__).warning(
            "Assets Folder not Found. Please clone repository again."
        )
        exit()

    for folder in ("downloads", "cache"):
        if folder in current_items and isdir(folder):
            rmtree(folder)
        mkdir(folder)

    LOGGER(__name__).info("Directories Updated.")
