
# import packages
import pathlib
import datetime
import logging

# import local modules
import values

def logsInit(bot):

    pathlib.Path("../logs").mkdir(parents=True, exist_ok=True)
    logger = logging.getLogger("discord")
    logger.setLevel(logging.INFO) # Do not allow DEBUG messages through
    handler = logging.FileHandler(filename="../logs/discord.py.log", encoding="utf-8", mode="w")
    handler.setFormatter(logging.Formatter("[{asctime}] {levelname}: {name}: {message}", style="{"))
    logger.addHandler(handler)
    
    # create log directories (if they don't already exist)
    pathlib.Path("../logs/dms").mkdir(parents=True, exist_ok=True)
    pathlib.Path("../logs/main").mkdir(parents=True, exist_ok=True)
    for guild in bot.guilds:
        pathlib.Path(f"../logs/{guild.id}").mkdir(parents=True, exist_ok=True)

def log(dir,filename,content):
    with open(f"../logs/{dir}/{filename}-{values.data.get('starttime-human')}.log","ta") as logfile:
        logfile.write(f"[{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S,%f')[:-3]}] {content}\n")


def dmLog(message):
    author = message.author
    recipient = message.channel.recipient
    content = message.content
    log("dms",f"{recipient.name}#{recipient.discriminator}",f"{author.name}#{author.discriminator}: {content}")
    if author == recipient:
        print(f"[DM] {author.name}#{author.discriminator}: {content}")
    else:
        print(f"[DM] {author.name}#{author.discriminator} => {recipient.name}#{recipient.discriminator}: {content}")
