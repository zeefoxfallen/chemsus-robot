import discord
import json
from discord.ext import commands

bot = commands.Bot(command_prefix='$')

@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))

@bot.event
async def on_message(message):
    await bot.process_commands(message)

    if message.author == bot.user:
        return

    if message.content == "bot?":
        await message.channel.send("Beep Boop")

    if message.content.startswith('+hello'):
        await message.channel.send('Hello!')

@bot.command()
async def reactrole(ctx,  emoji, role: discord.role,*,message):

    emb = discord.Embed(description=message)
    msg = await ctx.channel.send(embed=emb)
    await msg.add_reaction(emoji)

    with open('reactrole.json') as json_file:
        data = json.load(json_file)

        new_react_role = {
            'role_name' :role.__name,
            'role_id' :role.id,
            'emoji' :emoji,
            'message_id' :msg.id
        }


        data.append(new_react_role)

        with open('reactrole.json','w') as j:
            json.dump(data,j,indent=4)

bot.run("ODcxMTU3MTA0NjM4MDY2NzUx.YQXORw.u7owINfM7P7mlm9O29rWOW9GvCc")