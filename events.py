
# import packages
import discord

# initialize event functions
def eventsInit(bot):

    @bot.event
    async def on_message(message):

        if isinstance(message.channel, discord.channel.DMChannel):
            if message.author == message.channel.recipient:
                print(f"{message.author.name}#{message.author.discriminator}: {message.content}")
            else:
                print(f"{message.author.name}#{message.author.discriminator} => {message.channel.recipient.name}#{message.channel.recipient.discriminator}: {message.content}")

        await bot.process_commands(message)

        if message.author == bot.user:
            return

        if message.content == "bot?":
            await message.channel.send("Beep Boop")

    @bot.event
    async def on_ready():
        print('\"{0.user}\" is online in the following guild(s):'.format(bot))
        for guild in bot.guilds:
            print(' - \"{}\" (id: {})'.format(guild.name,guild.id))