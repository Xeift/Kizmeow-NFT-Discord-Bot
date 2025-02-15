
from discord import (ApplicationContext, Embed, IntegrationType,
                     InteractionContextType, Option)
from discord.ext import commands
from discord.ui import View

from api.get_gas_etherscan import get_gas_etherscan
from api.get_gas_blocknative import get_gas_blocknative
from utils.err_embed import general_err_embed
from utils.gas_tracker_embed import gas_etherscan_embed
from view.gas_tracker_view import gas_etherscan_view


class gas(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(
        name='gas',
        description='Check realtime gas price of multiple chain.',
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
            description='The chain and source for checking the gas price.',
            choices=[
                'Ethereum - Etherscan API',
                'Ethereum - Blocknative API'
            ]
        )
        
    ):
        embed = Embed()
        file = None
        view = View()
        
        if source == 'Ethereum - Etherscan API':
            (success, gas_data) = get_gas_etherscan()
            if success:
                (embed, file) = gas_etherscan_embed(gas_data)
                view = gas_etherscan_view(view)
                # TODO: add favorite btn
            else:
                embed=general_err_embed('Etherscan API is currently down. Please try again later.')

        elif source == 'Ethereum - Blocknative API':
            (success, gas_data) = get_gas_blocknative()
            if success:
                print(gas_data)
                (embed, file) = gas_blocknative_embed(gas_data)
                view = gas_blocknative_view(view)
            else:
                embed=general_err_embed('Blocknative API is currently down. Please try again later.')
            

            
        await ctx.respond(embed=embed, view=view, file=file)


def setup(bot):
    bot.add_cog(gas(bot))
