from discord import (ApplicationContext, Embed, IntegrationType,
                     InteractionContextType, Option)
from discord.ext import commands
from discord.ui import View

from api.get_os_account import get_os_account
from embed.err_embed import general_err_embed
from embed.opensea_account_embed import opensea_account_embed
from utils.load_config import load_config_from_json
from view.button import (etherscan_button, instagram_button, opensea_button,
                         website_button, x_button)
from web3 import Web3

class address_converter(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(
        name='address_converter',
        description='Convert the address to checksum, lower case or uppercase address',
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
    async def address_converter(
        self,
        ctx: ApplicationContext,
        address: Option(
            str,
            'EVM address'
        )
    ):
        await ctx.defer()
        
        mid = str(ctx.author.id)
        (
            enable_link_button,
            _,
            visibility,
            _,
            _
        ) = load_config_from_json(mid)
        embed = Embed(title='Address converter')
        embed.add_field(name='Checksum address', value=Web3.to_checksum_address(address))
        await ctx.respond(embed=embed)

        # if success:
            
        # await ctx.respond(
            # embed=embed,
            # view=view,
            # ephemeral=not visibility
        # )


def setup(bot):
    bot.add_cog(address_converter(bot))
