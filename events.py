
# import packages
import discord

# import local modules
import logs

# initialize event functions
def eventsInit(bot):

    @bot.event
    async def on_message(message):

        if isinstance(message.channel, discord.channel.DMChannel):
            logs.dmLog(bot,message)

        await bot.process_commands(message)

        if message.author == bot.user:
            return

        if message.content == "bot?":
            await message.channel.send("Beep Boop")

    @bot.event
    async def on_ready():

        logs.logsInit(bot)

        print('\"{0.user}\" is online in the following guild(s):'.format(bot))
        for guild in bot.guilds:
            print(' - \"{}\" (id: {})'.format(guild.name,guild.id))