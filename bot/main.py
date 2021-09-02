
if __name__ == '__main__':

    # import packages
    from discord.ext import commands
    from dotenv import load_dotenv
    from datetime import datetime
    import os

    import values
    from cogs import logCog

    # change working directory to the directory where this file is located
    os.chdir(os.path.dirname(__file__))   

    # loads .env contaning the auth token
    load_dotenv()
    DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")

    # initialize bot
    bot = commands.Bot(command_prefix='$')

    # initialize cogs
    bot.add_cog(logCog.logCog(bot))

    # start bot
    values.add("startTime",datetime.now())
    bot.start(DISCORD_TOKEN)
