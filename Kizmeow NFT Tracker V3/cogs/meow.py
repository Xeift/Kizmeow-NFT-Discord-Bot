import discord
from discord.commands import slash_command
from discord.ext import commands
from core.cog_core import cogcore

class meow(cogcore):
    @slash_command(name='meow',description='return bot latency')
    async def meow(
        self,
        ctx: discord.ApplicationContext
    ):
        embed=discord.Embed(title='Nyaa!', description=f'{self.bot.latency*1000:.2f} ms', color=0xFFA46E)
        await ctx.respond(embed=embed)

def setup(bot):# add cog
    bot.add_cog(meow(bot))
