import discord
from discord.ext import commands


class password(commands.Cog):
    def __init__(self,bot):
        self.bot = bot



    @commands.command()
    async def password(self,ctx):
        embed = discord.Embed(
            description = "**Password resets**\n If you have forgotten your PikaNetwork in-game password you can request it to be reset on our forums.\n 🔹 **Create a password reset:**\n https://pika-network.net/forums/password-reset-requests.169/",
            colour = discord.Colour.blue()
        )
        await ctx.send(embed=embed)




def setup(bot):
    bot.add_cog(password(bot))