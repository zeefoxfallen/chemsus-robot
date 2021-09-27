#imports
from discord.ext import commands

#imports data needed for economy
from economydata.accounts import accountsl

class economy(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

        #setup profile
    @commands.command()
    async def estart(self,ctx):
        if ctx.author.id in accountsl:
            await ctx.channel.send("you already have a account")
        else:
            accountsl.append(ctx.author.id)
            await ctx.channel.send("your account has been made")