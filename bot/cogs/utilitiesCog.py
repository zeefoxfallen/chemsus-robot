from discord.ext import commands

class utilitiesCog(commands.Cog):

    def __init__(self,bot):
        self.bot = bot
        self.logCog = self.bot.get_cog("logCog")