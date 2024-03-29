from discord.ext import commands
import discord
from datetime import datetime
import random 

class coreCmds(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def echo(self,ctx, *args):
        if args == ():
            await ctx.channel.send(":zipper_mouth:")
        else:
            output = ""
            for arg in args:
                output += str(arg)
                output += " "
            await ctx.channel.send(output)

    @commands.command()
    async def kill(self,ctx):
        if await self.bot.get_cog('coreUtils').adminCheck(ctx):
            await ctx.channel.send("**I will rise again** :skull:")
            await ctx.bot.close()
            raise SystemExit
 
    @commands.command()
    async def dm(self,ctx, member: discord.Member, *, content):
        if await self.bot.get_cog('coreUtils').adminCheck(ctx):
            channel = await member.create_dm()
            await channel.send(content)
            await ctx.channel.send(f"Sent \"{content}\" to {member.name}#{member.discriminator} :incoming_envelope:")

    @commands.command()
    async def whoami(self,ctx):
        username = ctx.author.name
        userid = ctx.author.id
        print(f"[whoami] Name: \"{username}\" ID: \"{userid}\"")
        await ctx.channel.send(f"You, my child are \"{username}\"")

    @commands.command()
    async def uptime(self,ctx):
        uptime = datetime.now() - self.bot.get_cog("coreUtils").values.get("startTime")
        await ctx.channel.send(f"the bot has been online for: `{uptime}` ")

    @commands.command()
    async def coinflip(self,ctx):
        if await self.bot.get_cog('coreUtils').adminCheck(ctx,sendError=False):
            coinfval = random.randint(0,21)
        else:
            coinfval = random.randint(0,20)

        await ctx.channel.send("flipping the coin...")

        if coinfval < 10:
            await ctx.channel.send("the coin is heads")
        elif coinfval < 20:
            await ctx.channel.send("the coin is tails")
        else:
            await ctx.channel.send("the coin landed on it's side")


    @commands.command()
    async def diceroll(self,ctx):
        if await self.bot.get_cog('coreUtils').adminCheck(ctx,sendError=False):
            diceval = random.randint(0,61)
        else:
            diceval = random.randint(0,60)

        await ctx.channel.send("rolling the dice...")

        if diceval < 10:
            await ctx.channel.send("the dice is a 1")
        elif diceval <20:
            await ctx.channel.send("the dice is a 2")
        elif diceval <30:
            await ctx.channel.send("the dice is a 3")
        elif diceval <40:
            await ctx.channel.send("the dice is a 4")
        elif diceval <50:
            await ctx.channel.send("the dice is a 5")
        elif diceval <60:
            await ctx.channel.send("the dice is a 6")
        else:
            await ctx.channel.send("the dice shattered when it hit the table")