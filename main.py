import os

from dotenv import load_dotenv
import discord
from discord.ext import commands

load_dotenv()

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
  print("Conection Ok!")

@bot.command(name='command_name')
async def lunch_royaltiz(ctx):
  result = exec(open("./file_toexec.py").read())
  await ctx.channel.send(result)

bot.run(os.getenv("TOKEN"))