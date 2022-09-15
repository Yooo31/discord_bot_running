import os

from dotenv import load_dotenv
import discord
from discord.ext import commands

from royaltiz import *

load_dotenv()

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
  print("Conection Ok!")

@bot.command(name='r')
async def lunch_royaltiz(ctx):
  result = run_all_player()
  await ctx.channel.send(result)

bot.run(os.getenv("TOKEN"))