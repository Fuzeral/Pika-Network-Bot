import discord
from discord.ext import commands


class Report(commands.Cog):
    def __init__(self,bot):
        self.bot = bot



    @commands.command()
    async def report(self,ctx):
        embed = discord.Embed(
            title = "**Links to report**\n 🔹Player Report:\nhttps://pika-network.net/forums/player-reports.150/\n 🔹 Bug Reports:\nhttps://pika-network.net/forums/bug_reports/",
            colour = discord.Colour.blue()
        )
        await ctx.send(embed=embed)




def setup(bot):
    bot.add_cog(Report(bot))