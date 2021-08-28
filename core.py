
# import packages
from discord.ext import commands as discordcmds
import time

# import loacl files
import commands
import events
import values

# main bot class
class botCore:
    def __init__(self):

        # initialize bot
        self.bot = discordcmds.Bot(command_prefix='$')

        # initialize events and commands
        events.eventsInit(self.bot)
        commands.commandsInit(self.bot)

    # on call, set starttime and start bot
    def START(self,token):
        values.data["starttime"] = time.time()
        self.bot.run(token)


