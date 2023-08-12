import json
import discord
from discord.ext import commands, tasks
import random
import asyncio
from asyncio import sleep
import discord
from discord.ext import commands
from discord import app_commands
import os
import requests
import datetime
from discord.ui import Select
from discord import Embed, app_commands
from discord.ext import commands
import string
from discord.ext.commands import CommandNotFound
from discord.ui import Button, View
from typing import ValuesView
from typing import Union
from datetime import datetime, timedelta
import urllib.parse
import subprocess
bot = commands.Bot(command_prefix="!", description="Bot en devellepement by Sitylist94", intents=discord.Intents.all())

status = [
    "Python is the best programming language"
]

@bot.command()
async def Bonjour(ctx):
    await ctx.send("Salut ça va")



@bot.event
async def on_ready():
    print("Ready !")
    changeStatus.start()

@bot.command()
async def start(ctx, secondes=5):
    changeStatus.change_interval(seconds=secondes)
    await ctx.send("Bot Prêt ✅")

@tasks.loop(seconds=5)
async def changeStatus():
    game = discord.Game(random.choice(status))
    await bot.change_presence(status=discord.Status.dnd, activity=game)

bot.run(TOKEN)
