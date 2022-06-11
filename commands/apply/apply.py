import discord
from discord.ext import commands


class Apply(commands.Cog):
    def __init__(self,bot):
        self.bot = bot


    @commands.command()
    async def apply(self,ctx):
        embed = discord.Embed(
            description = "**Looking for apply**?\n Here are the links you need in order to reply.\n 🔹 **Staff Application:**\n https://pika-network.net/forums/staff-applications.147/ \n 🔹 **Youtube/Twitch application:** \n https://pika-network.net/forums/youtube-twitch-applications.193/",
            colour = discord.Colour.blue()
        )
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(Apply(bot))