import discord

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('+hello'):
        await message.channel.send('Hello!')

client.run("ODcxMTU3MTA0NjM4MDY2NzUx.YQXORw.u7owINfM7P7mlm9O29rWOW9GvCc")