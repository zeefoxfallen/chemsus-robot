import discord
from discord.ext import commands
import os
from dotenv import load_dotenv
import time

import commandsf

class botCore():
    def __init__(self):
        global bot

        

        load_dotenv()
        self.DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
        self.ADMINS = os.getenv("ADMINS").split(":")

        bot = commands.Bot(command_prefix='$')

        cmds = commandsf.botcommands(bot)

        @bot.event
        async def on_message(message):

            if isinstance(message.channel, discord.channel.DMChannel):
                if message.author == message.channel.recipient:
                    print(f"{message.author.name}#{message.author.discriminator}: {message.content}")
                else:
                    print(f"{message.author.name}#{message.author.discriminator} => {message.channel.recipient.name}#{message.channel.recipient.discriminator}: {message.content}")

            await bot.process_commands(message)

            if message.author == bot.user:
                return

            if message.content == "bot?":
                await message.channel.send("Beep Boop")

        bot.run(self.DISCORD_TOKEN)


if __name__ == '__main__':
    core = botCore()

