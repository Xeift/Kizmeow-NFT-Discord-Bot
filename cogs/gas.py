
from discord import (ApplicationContext, Embed, IntegrationType,
                     InteractionContextType, Option)
from discord.ext import commands

from api.get_gas_etherscan import get_gas_etherscan
from utils.err_embed import general_err_embed
from utils.gas_tracker_embed import gas_etherscan_embed


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
                # 'Ethereum - Blocknative API'
            ]
        )
        
    ):
        if source == 'Ethereum - Etherscan API':
            (success, gas_data) = get_gas_etherscan()
            embed = Embed() # A
            if success:
                embed = gas_etherscan_embed(gas_data) # B
            else:
                embed=general_err_embed('Etherscan API is currently down. Please try again later.') # C
            
        await ctx.respond(embed=embed)


def setup(bot):
    bot.add_cog(gas(bot))
