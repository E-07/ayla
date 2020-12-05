# Atualmente a Ayla é em JavaScript, Estou passando ela para Python...
import discord
from discord.ext import commands
import os
from server import run

bot = commands.Bot(command_prefix=".")

for filename in os.listdir("./cogs"):
	if filename.endswith(".py") and filename != "__init__.py":
		bot.load_extension(f'cogs.{filename[:-3]}')


@bot.command()
async def load(ctx, extension):
	bot.load_extension(f"cogs.{extension}")


@bot.command()
async def unload(ctx, extension):
	bot.unload_extension(f"cogs.{extension}")


@bot.command()
async def reload(ctx, extension):
	bot.unload_extension(f"cogs.{extension}")
	bot.load_extension(f"cogs.{extension}")


run()
bot.run(os.getenv("TOKEN"))
