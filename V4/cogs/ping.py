import discord
from discord.ext import commands
from discord.commands import slash_command


class ping(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @slash_command(name='ping', description='Return bot latency')
    async def ping(
        self,
        ctx: discord.ApplicationContext
    ):
        latency = self.bot.latency
        embed = discord.Embed(
            title='Bot latency',
            description=f'{latency * 1000:.2f} ms ({latency:.3f} s)',
            color=0xFFA46E
        )
        await ctx.respond(embed=embed, ephemeral=True)


def setup(bot):
    bot.add_cog(ping(bot))
