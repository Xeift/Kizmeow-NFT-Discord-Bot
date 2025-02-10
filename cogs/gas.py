
from discord import (ApplicationContext, Embed, IntegrationType,
                     InteractionContextType, Option)
from discord.ext import commands

from api.get_gas_etherscan import get_gas_etherscan
from utils.err_embed import general_err_embed


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
        (success, gas_data) = get_gas_etherscan()

        embed = Embed(color=0xFFA46E)
        if success:
            gas_data = gas_data['result']
            low = float(gas_data['SafeGasPrice'])
            medium = float(gas_data['ProposeGasPrice'])
            high = float(gas_data['FastGasPrice'])
            gasUsedRatio = gas_data['gasUsedRatio'].split(',')
            gasUsedRatioText = ''
            for gas in gasUsedRatio:
                gasUsedRatioText += f'{float(gas) * 100:.2f}% '
  

            embed.title = f'Gas Tracker'
            embed.add_field(name='🐢', value=f'{low:.2f} gwei')
            embed.add_field(name='🚗', value=f'{medium:.2f} gwei')
            embed.add_field(name='🚀', value=f'{high:.2f} gwei')
            embed.add_field(name='Last 5 block gas use ratio', value=gasUsedRatioText)
            
        # TODO: add gas source footer
        else:
            embed=general_err_embed('Etherscan API is currently down. Please try again later.')
            
        await ctx.respond(embed=embed)


def setup(bot):
    bot.add_cog(gas(bot))
