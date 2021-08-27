
def init(bot):

    @bot.command()
    async def echo(ctx, *args):
        print(args)
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
        if str(ctx.author.id) in ADMINS:
            await ctx.channel.send("**I will rise again** :skull:")
            raise SystemExit
        else:
            await ctx.channel.send("I'm sorry my child, you're not close enough with Chemsus to use this command")
            

    @bot.command()
    async def dm(ctx, member: discord.Member, *, content):
        if str(ctx.author.id) in ADMINS:
            channel = await member.create_dm()
            await channel.send(content)
        else:
            await ctx.channel.send("I'm sorry my child, you're not close enough with Chemsus to use this command")

    @bot.command()
    async def whoami(ctx):
        username = ctx.author.name
        userid = ctx.author.id
        print("[whoami] Name: \"{}\" ID: \"{}\"".format(username,userid))
        await ctx.channel.send("You, my child are \"{}\"".format(username))

    @bot.command()
    async def admins(ctx):
        if ADMINS == []:
            await ctx.channel.send("There are currently no loaded Robot Chemsus admins.")
        else:
            output = "The current Robot Chemsus admins are: "
            i = 1
            for adminID in ADMINS:
                if i != 1:
                    output += ", "
                    if i == len(ADMINS):
                        output += "& "
                output += "\""
                output += str(await bot.fetch_user(adminID))
                output += "\""
                i += 1
            await ctx.channel.send(output)

    @bot.command()
    async def uptime(ctx):
        global starttime
        await ctx.channel.send(f"the bot has been online for {round(((time.time() - starttime) / 60),3)} minutes")
