
if __name__ == '__main__':

    # import packages
    from discord.ext import commands
    from dotenv import load_dotenv
    from datetime import datetime
    import os

    
    from cogs import coreUtils, logs

    # change working directory to the directory where this file is located
    os.chdir(os.path.dirname(__file__))   

    # loads .env contaning the auth token
    load_dotenv()
    DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")

    # initialize bots
    bot = commands.Bot(command_prefix='$')

    # initialize cogs
    bot.add_cog(coreUtils.coreUtils(bot))
    bot.add_cog(logs.logs(bot))

    # start bot
    bot.get_cog('coreUtils').values["startTime"] = datetime.now()
    bot.start(DISCORD_TOKEN)
