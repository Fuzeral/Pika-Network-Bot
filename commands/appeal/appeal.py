import discord
from discord.ext import commands


class App(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

    @commands.command()
    async def appeal(self,ctx):
        embed = discord.Embed(
            description = "**Appealing for your punishment.**\n If you feel like you got falsely punished you can appeal on the forums.\n **🔹 Appeal:**\nhttps://pika-network.net/forums/punishment-appeals.149/",
            colour = discord.Colour.blue()
        )
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(App(bot))