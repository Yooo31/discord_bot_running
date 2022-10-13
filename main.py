import os
from dotenv import load_dotenv

import discord
from discord.ext import commands
from discord.ext import tasks as discordTasks

# from royaltiz import *
from new_version_royaltiz import *
from igraal import *

load_dotenv()

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
  print("Conection Ok!")

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

@discordTasks.loop(minutes=1.0)
async def get_evolution():
  await channel.send('test')
  print('test')

get_evolution.start()
bot.run(os.getenv("TOKEN"))