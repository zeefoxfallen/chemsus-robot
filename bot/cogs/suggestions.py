from discord import channel
from discord.ext import commands

class sugg(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def botsuggest(self, ctx, *args):
        if args == ():
            await ctx.channel.send("you need to actually suggest something")
        else:
            output = ""
            for arg in args:
                output += str(arg)
                output += " "
            await self.bot.get_channel(891745640344871004).send(output)