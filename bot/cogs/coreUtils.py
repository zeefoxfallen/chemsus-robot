from discord.ext import commands

class coreUtils(commands.Cog):

    def __init__(self,bot):
        self.bot = bot
        self.values = {}

    # fucntion to check if command author is a guild admin
    async def adminCheck(self,ctx,sendError=True):
        if ctx.message.author.guild_permissions.administrator:
            if sendError:
                self.bot.get_cog("logs").log(ctx.guild.id,"admin-commands",f"{ctx.author.name}#{ctx.author.discriminator} successfully used command \"{ctx.invoked_with}\".")
            return True
        if sendError:
            await ctx.channel.send("I'm sorry my child, you're not close enough with Chemsus to use this command")
            self.bot.get_cog("logs").log(ctx.guild.id,"admin-commands",f"{ctx.author.name}#{ctx.author.discriminator} tried to use command \"{ctx.invoked_with}\" and was blocked.")
        return False
    