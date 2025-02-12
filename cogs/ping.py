
from discord import (ApplicationContext, Embed, IntegrationType,
                     InteractionContextType)
from discord.ext import commands

from utils.load_config import load_config_from_json


class ping(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(
        name='ping',
        description='Check latency of the bot.',
        integration_types=[
            IntegrationType.user_install,
            IntegrationType.guild_install,
        ],
        contexts=[
            InteractionContextType.guild,
            InteractionContextType.bot_dm,
            InteractionContextType.private_channel,
        ],
    )
    async def ping(
        self,
        ctx: ApplicationContext
    ):
        mid = str(ctx.author.id)
        (
            _,
            _,
            visibility,
            _,
            _
        ) = load_config_from_json(mid)
        latency = self.bot.latency
        embed = Embed(
            title='Bot Latency',
            description=f'{latency * 1000:.2f} ms ({latency:.2f} s)',
            color=0xFFA46E
        )
        await ctx.respond(embed=embed, ephemeral=not visibility)


def setup(bot):
    bot.add_cog(ping(bot))
