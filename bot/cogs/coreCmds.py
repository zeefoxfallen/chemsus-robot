from discord.ext import commands
import discord
from datetime import datetime
import random 

class coreCmds(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    # fucntion to check if command author is a guild admin
    async def adminCheck(self,ctx,sendError=True):
        if ctx.message.author.guild_permissions.administrator:
            if sendError:
                self.bot.get_cog("logs").log(ctx.guild.id,"admin-commands",f"{ctx.author.name}#{ctx.author.discriminator} successfully used command \"{ctx.invoked_with}\".")
            return True
        if sendError:
            await ctx.channel.send("I'm sorry my child, you're not close enough with Chemsus to use this command")
            self.bot.get_cog("logs").log(ctx.guild.id,"admin-commands",f"{ctx.author.name}#{ctx.author.discriminator} tried to use command \"{ctx.invoked_with}\" and was blocked.")
        return False

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
        if await self.adminCheck(ctx):
            await ctx.channel.send("**I will rise again** :skull:")
            await ctx.bot.close()
            raise SystemExit
 
    @commands.command()
    async def dm(self,ctx, member: discord.Member, *, content):
        if await self.adminCheck(ctx):
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
        if await self.adminCheck(ctx,sendError=False):
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