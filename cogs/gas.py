
from discord import (ApplicationContext, Embed, IntegrationType,
                     InteractionContextType, Option, OptionChoice)
from discord.ext import commands


class gas(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(
        name='gas',
        description='Check current gas price',
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
    async def gas(
        self,
        ctx: ApplicationContext,
        source: Option(
            input_type='str',
            description='Select source',
            choices=[
                'Ethereum - Etherscan API',
                'Ethereum - Blocknative API'
            ]
        )
        
    ):
        latency = self.bot.latency
        embed = Embed(
            title='source',
            description=f'source is: {source}',
            color=0xFFA46E
        )
        await ctx.respond(embed=embed)


def setup(bot):
    bot.add_cog(gas(bot))
