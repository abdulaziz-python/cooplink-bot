# -*- coding: utf-8 -*-
from dataclasses import dataclass, field
from typing import List
import os

@dataclass
class BotConfig:
    TOKEN: str = "BOT_TOKEN"
    ADMIN_IDS: List[int] = field(default_factory=lambda: [6236467772])
    DB_NAME: str = "code_selling_bot.db"
    ANNOUNCEMENT_CHANNEL: str = "@cooplink"

@dataclass
class Channels:
    REQUIRED: List[str] = field(default_factory=lambda: ["@cooplink", "@pythonnews_uzbekistan"])
    ANNOUNCEMENT: str = "@cooplink"

config = BotConfig()
channels = Channels()

BOT_TOKEN = config.TOKEN
ADMIN_IDS = config.ADMIN_IDS
DB_NAME = config.DB_NAME
ANNOUNCEMENT_CHANNEL = config.ANNOUNCEMENT_CHANNEL
REQUIRED_CHANNELS = channels.REQUIRED
DATABASE_URL = os.getenv("DATABASE_URL", "DATABASE_URL")
