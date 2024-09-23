from pypresence import Presence
import time
import discord
from discord.ext import commands
import os
from discord import app_commands
import random
import subprocess
from discord import Intents, Client, Interaction, Game
from discord.app_commands import CommandTree
from datetime import timedelta, datetime, timezone
import aiohttp
from keep_alive import keep_alive
import asyncio

client_id = '1163118566401376397'
RPC = Presence(client_id)

RPC.connect()
RPC.update(start=time.time(),
           large_image="hanabi",
           large_text="花火♡",
           small_image="channels4_profile",
           small_text=
           "Honkai: Star Rail")
while True:
    time.sleep(15)

    keep_alive()