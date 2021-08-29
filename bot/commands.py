
# import packages
import discord
import time

# import local modules
import values
import logs

# fucntion to check if command author is a guild admin
async def adminCheck(ctx,sendError=True):
    if ctx.message.author.guild_permissions.administrator:
        logs.log(ctx.guild.id,"admin-commands",f"{ctx.author.name}#{ctx.author.discriminator} successfully used command \"{ctx.invoked_with}\".")
        return True
    if sendError:
        await ctx.channel.send("I'm sorry my child, you're not close enough with Chemsus to use this command")
    logs.log(ctx.guild.id,"admin-commands",f"{ctx.author.name}#{ctx.author.discriminator} tried to use command \"{ctx.invoked_with}\" in  and was blocked.")
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
        print("[whoami] Name: \"{}\" ID: \"{}\"".format(username,userid))
        await ctx.channel.send("You, my child are \"{}\"".format(username))

    @bot.command()
    async def uptime(ctx):
        uptime = round(((time.time() - values.data.get("starttime-unix")) / 60),3)
        await ctx.channel.send(f"the bot has been online for {uptime} minutes")
