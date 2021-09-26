#imports
from discord.ext import commands

class sugg(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    #the bot suggest command code
    @commands.command()
    async def botsuggest(self, ctx, *args):
        if args == ():
            await ctx.channel.send("you need to actually suggest something")
        else:
            output = ""
            for arg in args:
                output += str(arg)
                output += " "
            message = await self.bot.get_channel(891745640344871004).send(output)
            emoji = '\N{THUMBS UP SIGN}'
            await message.add_reaction(emoji)
            emoji = '\N{THUMBS DOWN SIGN}'
            await message.add_reaction(emoji)

    #the server suggest command code
    @commands.command()
    async def serversuggest(self, ctx, *args):
        if args == ():
            await ctx.channel.send("you need to actually suggest something")
        else:
            output = ""
            for arg in args:
                output += str(arg)
                output += " "
            message = await self.bot.get_channel(891773352845385758).send(output)
            emoji = '\N{THUMBS UP SIGN}'
            await message.add_reaction(emoji)
            emoji = '\N{THUMBS DOWN SIGN}'
            await message.add_reaction(emoji)