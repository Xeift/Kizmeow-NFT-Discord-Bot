import discord
from discord.commands import slash_command
from discord.ext import commands


class ping(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @slash_command(name='ping', description='Return bot latency')
    async def ping(
            self,
            ctx: discord.ApplicationContext
    ):
        embed = discord.Embed(title='Nyaa! ' f'{self.bot.latency * 1000:.2f} ms', color=0xFFA46E)
        await ctx.respond(embed=embed, ephemeral=True)


def setup(bot):  # add cog
    bot.add_cog(ping(bot))
