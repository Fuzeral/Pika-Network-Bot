
import discord
from discord.ext import commands

class Pay(commands.Cog):
    def __init__(self,bot):
        self.bot = bot


    @commands.command()
    async def payment(self,ctx):
        embed = discord.Embed(
            title = "Payment issues",
            description = "If you have not received the items from your PikaNetwork store purchase or have any issues with them, please create a payment releated thread\n 🔹 Payment Support: \n https://pika-network.net/payment-support/",
            colour = discord.Colour.blue()
        )
        await ctx.send(embed=embed)



def setup(bot):
    bot.add_cog(Pay(bot))