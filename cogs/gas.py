
from discord import (ApplicationContext, Embed, IntegrationType,
                     InteractionContextType, Option, OptionChoice)
from discord.ext import commands
from api.get_gas_etherscan import get_gas_etherscan

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
            description='Select chain and source',
            choices=[
                'Ethereum - Etherscan API',
                'Ethereum - Blocknative API'
            ]
        )
        
    ):
        (success, gas_data) = get_gas_etherscan()

        embed = Embed(color=0xFFA46E)
        if success:
            embed.title = f'Source is {source}'
            embed.description = f'{gas_data}'
        else:
            embed.title = 'err'
            embed.description = 'test2'
            
        await ctx.respond(embed=embed)


def setup(bot):
    bot.add_cog(gas(bot))
