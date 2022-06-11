import discord
from discord.ext import commands


class Bug(commands.Cog):
    def __init__(self,bot):
        self.bot = bot


    @commands.command()
    async def bug(self,ctx):
        embed = discord.Embed(
            title = "Found a bug?\n We are sorry about that. Make sure to report it so we can make sure it will not happen again.\n 🔹 Bug Report: \n https://pika-network.net/forums/bug_reports/",
            colour = discord.Colour.blue()
        )
        await ctx.send(embed=embed)



def setup(bot):
    bot.add_cog(Bug(bot))