import discord
from discord.ext import commands


class tic(commands.Cog):
    def __init__(self,bot):
        self.bot = bot


    @commands.command()
    async def ticket(self,ctx):
        embed = discord.Embed(
            description = "**Creating a help and support ticket.**\n If you would like to request assistance from staff privately, you can submit a Help & Support ticket on our forums.\n 🔹 **Help and support ticket:**\n https://pika-network.net/forums/help-support.173/",
            colour = discord.Colour.blue()
        )
        await ctx.send(embed=embed)



def setup(bot):
    bot.add_cog(tic(bot))