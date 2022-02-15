#imports
from discord.ext import commands
import json

#imports data needed for economy


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

            with open(f'{self.gamePath}/saves/{self.saveName}.json', 'w', encoding='utf-8') as file:
                json.dump(saveDict, file, ensure_ascii=False, indent=4)