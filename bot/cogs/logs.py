import discord
from discord.ext import commands 
import pathlib
import logging
from datetime import datetime

class logs(commands.Cog):

    def __init__(self,bot):
        self.bot = bot

        # initalize discord.py's logger
        pathlib.Path("../logs").mkdir(parents=True, exist_ok=True)
        logger = logging.getLogger("discord")
        logger.setLevel(logging.INFO) # Do not allow DEBUG messages through
        handler = logging.FileHandler(filename="../logs/discord.py.log", encoding="utf-8", mode="w")
        handler.setFormatter(logging.Formatter("[{asctime}] {levelname}: {name}: {message}", style="{"))
        logger.addHandler(handler)

        # create log directories (if they don't already exist)
        pathlib.Path("../logs/dms").mkdir(parents=True, exist_ok=True)
        # pathlib.Path("../logs/main").mkdir(parents=True, exist_ok=True) # not currently in use
        for guild in bot.guilds:
            pathlib.Path(f"../logs/{guild.id}").mkdir(parents=True, exist_ok=True)

    def log(self,dir,filename,content):
        with open(f"../logs/{dir}/{filename}-{self.bot.get_cog('coreUtils').values.get('startTime').strftime('%Y%m%d-%H%M%S')}.log","ta") as logfile:
            logfile.write(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S,%f')[:-3]}] {content}\n")

    @commands.Cog.listener("on_message")
    async def dmLogger(self,message): 
        if isinstance(message.channel, discord.channel.DMChannel):
            author = message.author
            recipient = message.channel.recipient
            content = message.content
            self.log("dms",f"{recipient.name}#{recipient.discriminator}",f"{author.name}#{author.discriminator}: {content}")
            if author == recipient:
                print(f"[DM] {author.name}#{author.discriminator}: {content}")
            else:
                print(f"[DM] {author.name}#{author.discriminator} => {recipient.name}#{recipient.discriminator}: {content}")
