
if __name__ == '__main__':

    # import packages
    import discord
    from discord.ext import commands
    from dotenv import load_dotenv
    from datetime import datetime
    import os

    
    from cogs import coreUtils, coreEvents, coreCmds, logs, suggestions, welcome, economy

    # change working directory to the directory where this file is located
    os.chdir(os.path.dirname(__file__))   

    # loads .env contaning the auth token
    load_dotenv()
    DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")

    # setup discord bot intents
    intents = discord.Intents.default()
    intents.members = True

    # initialize bot
    bot = commands.Bot(command_prefix='$',intents=intents)

    # initialize cogs
    bot.add_cog(coreUtils.coreUtils(bot))
    bot.add_cog(coreEvents.coreEvents(bot))
    bot.add_cog(coreCmds.coreCmds(bot))
    bot.add_cog(logs.logs(bot))
    bot.add_cog(suggestions.sugg(bot))
    bot.add_cog(welcome.Welcome(bot))
    bot.add_cog(economy.economy(bot))

    # start bot
    bot.get_cog('coreUtils').values["startTime"] = datetime.now()
    bot.run(DISCORD_TOKEN)

