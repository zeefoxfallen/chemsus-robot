#imports
from discord.ext import commands

#imports data needed for economy
from economydata import accounts

class economy(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

        #setup profile
        @commands.command()
        async def estart(ctx, member):
            if accounts == member.id:
                await ctx.channel.send("you already have a account")
            else:
                accounts.append(member.id)