
from discord import (ApplicationContext, Embed, IntegrationType,
                     InteractionContextType, Option)
from discord.ext import commands
from discord.ui import View
from discord.utils import basic_autocomplete

from api.get_gas_etherscan import get_gas_etherscan
from api.get_gas_blocknative import get_gas_blocknative
from utils.err_embed import general_err_embed
from utils.gas_tracker_embed import gas_etherscan_embed, gas_blocknative_embed
from view.gas_tracker_view import gas_etherscan_view
from utils.chain import get_available_chains, get_gas_source_by_name, get_gas_source_detail

class gas(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    def source_autocomplete(ctx):
        chain_name = ctx.options.get('chain')
        gas_source = get_gas_source_by_name(chain_name)
        return gas_source.keys()
        
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
        chain: Option(
            input_type='str',
            description='The chain for checking the gas price.',
            choices=get_available_chains()
        ),
        source: Option(
            input_type='str',
            description='Select a source.',
            autocomplete=basic_autocomplete(source_autocomplete)
        )
        
    ):
        embed = Embed()
        file = None
        view = View()

        gas_source_detail = get_gas_source_detail(chain, source)

        print(source)
        print(gas_source_detail)

        if source == 'Etherscan API':
            (success, gas_data) = get_gas_etherscan()
            if success:
                (embed, file) = gas_etherscan_embed(gas_data)
                view = gas_etherscan_view(view)
            else:
                embed=general_err_embed('Etherscan API is currently down. Please try again later.')

        elif source == 'Blocknative API':
            (success, gas_data) = get_gas_blocknative(gas_source_detail)
            if success:
                (embed, file) = gas_blocknative_embed(gas_data)
                view = gas_blocknative_view(view)
            else:
                embed=general_err_embed('Blocknative API is currently down. Please try again later.')
            

            
        await ctx.respond(embed=embed, view=view, file=file)


def setup(bot):
    bot.add_cog(gas(bot))
