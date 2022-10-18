import os
import time
from dotenv import load_dotenv

import discord
from discord.ext import tasks, commands
# from discord.ext import tasks as discordTasks

# from royaltiz import *
from new_version_royaltiz import *
from igraal import *

load_dotenv()

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)
global time
time = 0

@bot.event
async def on_ready():
  task_loop.start()
  print("Conection Ok!")

@tasks.loop(minutes=15)
async def task_loop():
  print('Check all price')
  channel = bot.get_channel(1017727497963585536)
  result = start_royaltiz_player()
  filteredResult = filter_the_result(result)
  await channel.send(filteredResult)
  print('End !')

@bot.command(name='r')
async def lunch_royaltiz(ctx):
  result = start_royaltiz_player()
  await ctx.channel.send(result)
  print('End !')

@bot.command(name='igraal')
async def lunch_igraal(ctx):
  result = index()
  await ctx.channel.send(result)
  print('End !')



bot.run(os.getenv("TOKEN"))
