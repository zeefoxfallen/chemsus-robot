
if __name__ == '__main__':

    # import packages
    from dotenv import load_dotenv
    import os

    # import loacl files
    import core

    # loads .env contaning the auth token
    load_dotenv()
    DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")

    # initialize bot
    BOT = core.botCore()

    # start bot
    BOT.START(DISCORD_TOKEN)
