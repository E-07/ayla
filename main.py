# Atualmente a Ayla é em JavaScript, Estou passando ela para Python...

# Discord
import discord
from discord.ext import commands

# Files
import os
import json


def load_file():
	with open("config.json", "r") as file:
		return json.load(file)


config = load_file()

bot = commands.Bot(
    command_prefix=config["prefix"])  # Prefixo secundário para testes :0


@bot.event
async def on_ready():
	print("Estou Rodando!")


@bot.event
async def on_message(message):
	if message.author.bot:  # Se a mensagem for de bot retorna nada.
		return
	else:
		await bot.process_commands(message)


@bot.command()
async def ping(ctx):
	await ctx.send("Pong")


bot.run(os.getenv("TOKEN"))
