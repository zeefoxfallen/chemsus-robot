
# import packages
import discord.ext
from datetime import datetime

# import local modules
import commands
import events
import values

# main bot class
class botCore:

    def __init__(self):

        # initialize bot
        self.bot = discord.ext.commands.Bot(command_prefix='$')

        # initialize event and command modules
        events.eventsInit(self.bot)
        commands.commandsInit(self.bot)

    # on call, set the start time and start the bot
    def START(self,token):
        values.data["startTime"] = datetime.now()
        self.bot.run(token)


