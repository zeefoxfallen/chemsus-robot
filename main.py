import discord
import json
from discord.ext import commands
client = discord.Client()
client = commands.bot(command_prefix="+")


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('+hello'):
        await message.channel.send('Hello!')

@client.command()
async def reactrole(ctx,  emoji, role: discord.role,*,message):

    emb = discord.embed(description=message)
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


client.run("ODcxMTU3MTA0NjM4MDY2NzUx.YQXORw.u7owINfM7P7mlm9O29rWOW9GvCc")