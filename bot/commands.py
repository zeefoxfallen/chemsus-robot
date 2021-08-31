
# import packages
import discord
from datetime import datetime

# import local modules
import values
import logs
import random

# fucntion to check if command author is a guild admin
async def adminCheck(ctx,sendError=True):
    if ctx.message.author.guild_permissions.administrator:
        logs.log(ctx.guild.id,"admin-commands",f"{ctx.author.name}#{ctx.author.discriminator} successfully used command \"{ctx.invoked_with}\".")
        return True
    if sendError:
        await ctx.channel.send("I'm sorry my child, you're not close enough with Chemsus to use this command")
        logs.log(ctx.guild.id,"admin-commands",f"{ctx.author.name}#{ctx.author.discriminator} tried to use command \"{ctx.invoked_with}\" and was blocked.")
    return False

# initialize command functions
def commandsInit(bot):

    @bot.command()
    async def echo(ctx, *args):
        if args == ():
            await ctx.channel.send(":zipper_mouth:")
        else:
            output = ""
            for arg in args:
                output += str(arg)
                output += " "
            await ctx.channel.send(output)

    @bot.command()
    async def kill(ctx):
        if await adminCheck(ctx):
            await ctx.channel.send("**I will rise again** :skull:")
            await ctx.bot.close()
            raise SystemExit
 
    @bot.command()
    async def dm(ctx, member: discord.Member, *, content):
        if await adminCheck(ctx):
            channel = await member.create_dm()
            await channel.send(content)
            await ctx.channel.send(f"Sent \"{content}\" to {member.name}#{member.discriminator} :incoming_envelope:")

    @bot.command()
    async def whoami(ctx):
        username = ctx.author.name
        userid = ctx.author.id
        print(f"[whoami] Name: \"{username}\" ID: \"{userid}\"")
        await ctx.channel.send(f"You, my child are \"{username}\"")

    @bot.command()
    async def uptime(ctx):
        uptime = datetime.now() - values.data.get("startTime")
        await ctx.channel.send(f"the bot has been online for: `{uptime}` ")

    @bot.command()
    async def coinflip(ctx):
        if await adminCheck(ctx,sendError=False):
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