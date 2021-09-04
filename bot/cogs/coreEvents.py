from discord.ext import commands

class coreEvents(commands.Cog):
    
    def __init__(self,bot):
        self.bot = bot

    @commands.Cog.listener("on_message")
    async def on_message(self,message):

        await self.bot.process_commands(message)

        if message.author == bot.user:
            return

        if message.content == "bot?":
            await message.channel.send("Beep Boop")

    @commands.Cog.listener("on_ready")
    async def on_ready(self):

        print('\"{0.user}\" is online in the following guild(s):'.format(bot))
        for guild in bot.guilds:
            print(' - \"{}\" (id: {})'.format(guild.name,guild.id))