import discord
from discord.ext import commands
import json
import os
from dotenv import load_dotenv

load_dotenv()
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")

try:
    adminsFile = open("{}/admins.json".format(os.path.dirname(__file__),"rt"))
    adminsFilsStr = adminsFile.read()
    adminsFile.close()
    ADMINS = json.loads(adminsFilsStr)
    del adminsFilsStr
except FileNotFoundError:
    print("!!! \"admins.json\" not found, admin commands disabled !!!")
    ADMINS = {}

bot = commands.Bot(command_prefix='$')

@bot.event
async def on_ready():
    print('\"{0.user}\" is online in the following server(s):'.format(bot))
    for guild in bot.guilds:
        print(' - \"{}\" (id: {})'.format(guild.name,guild.id))

@bot.event
async def on_message(message):
    await bot.process_commands(message)

    if message.author == bot.user:
        return

    if message.content == "bot?":
        await message.channel.send("Beep Boop")

    if message.content.startswith('+hello'):
        await message.channel.send('Hello!')

# # Temporaily Disabled Until Functional:
# @bot.command()
# async def reactrole(ctx,  emoji, role: discord.role,*,message):

#     emb = discord.Embed(description=message)
#     msg = await ctx.channel.send(embed=emb)
#     await msg.add_reaction(emoji)

#     with open('reactrole.json') as json_file:
#         data = json.load(json_file)

#         new_react_role = {
#             'role_name' :role.__name,
#             'role_id' :role.id,
#             'emoji' :emoji,
#             'message_id' :msg.id
#         }

#         data.append(new_react_role)

#         with open('reactrole.json','w') as j:
#             json.dump(data,j,indent=4)

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
    if str(ctx.author.id) in ADMINS.keys():
        await ctx.channel.send("*I will rise again* :skull:")
        raise SystemExit
    else:
        await ctx.channel.send("I'm sorry my child, you're not close enough with chemsus to use this command")

@bot.command()
async def whoami(ctx):
    username = ctx.author.name
    userid = ctx.author.id
    print("[whoami] Name: \"{}\" ID: \"{}\"".format(username,userid))
    await ctx.channel.send("You, my child are \"{}\"".format(username))

@bot.command()
async def admins(ctx):
    if ADMINS == {}:
        await ctx.channel.send("There are currently no Robot Chemsus admins, check that admins.json loaded correctly.")
    output = "The current Robot Chemsus admins are: "
    i = 1
    for adminID in ADMINS.keys():
        if i != 1:
            output += ", "
            if i == len(ADMINS.keys()):
                output += "& "
        output += "\""
        output += str(await bot.fetch_user(adminID))
        output += "\""
        i += 1
    await ctx.channel.send(output)

bot.run(DISCORD_TOKEN)