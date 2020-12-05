from discord.ext import commands
import discord


class Event(commands.Cog):
	def __init__(self, bot):
		self.bot = bot

	@commands.Cog.listener()
	async def on_ready(self):
		print("Iniciado com sucesso!")

def setup(bot):
    bot.add_cog(Event(bot))