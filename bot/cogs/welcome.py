from discord.ext.commands import Cog
from discord.ext import commands

class Welcome(commands.Cog):
    def __init__ (self, bot):
        self.bot = bot

#    @Cog.listener()
#    async def on_ready(self):
#        if not self.bot.ready:
#            self.bot.cogs_ready.ready_up("Welcome")

    @commands.Cog.listener()
    async def on_member_join(self, member):
        await self.bot.get_channel(862199629142818846).send(f"welcome {member.mention}. i see you are new here. we here accept all but those who do unspeakable things")

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        await self.bot.get_channel(862199629142818846).send(f"goodbye {member.display_name}. we are sorry to see you leave")

def setup(bot):
    bot.add_cog(Welcome(bot))