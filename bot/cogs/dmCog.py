import discord
from discord.ext import commands
from datetime import datetime

from .. import values

class dmCog(commands.Cog):

    def __init__(self,bot):
        self.bot = bot

    