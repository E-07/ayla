from discord.ext import commands
import discord


class Info(commands.Cog):
	def __init__(self, bot):
		self.bot = bot

	@commands.command(aliases=["p"])
	async def ping(self, ctx):
		await ctx.send("Pong")


def setup(bot):
	bot.add_cog(Info(bot))
