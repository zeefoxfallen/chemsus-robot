
# import packages
from discord.ext import commands as discordcmds
import time
import datetime

# import local modules
import commands
import events
import values

# main bot class
class botCore:
    def __init__(self):

        # initialize bot
        self.bot = discordcmds.Bot(command_prefix='$')

        # initialize event and command modules
        events.eventsInit(self.bot)
        commands.commandsInit(self.bot)

    # on call, set starttime and start bot
    def START(self,token):
        values.data["starttime-human"] = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
        values.data["starttime-unix"] = time.time()
        self.bot.run(token)


