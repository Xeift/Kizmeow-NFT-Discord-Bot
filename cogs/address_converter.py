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
        address_or_username: Option(
            str,
            'EVM address (ENS supported) or OpenSea username.'
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
        disable_link_button = not enable_link_button
        (success, account_data) = get_os_account(address_or_username)
        embed = Embed()
        view = View()

        if success:
            embed = opensea_account_embed(account_data)
            address = account_data['address']
            username = account_data['username']
            opensea_url = f'https://opensea.io/{address}'
            etherscan_url = f'https://etherscan.io/address/{address}'
            website_url = account_data['website']
            social_media_accounts = account_data['social_media_accounts']

            view.add_item(opensea_button(opensea_url))
            view.add_item(etherscan_button(etherscan_url))
            if website_url: view.add_item(website_button(website_url))

            for social_media_account in social_media_accounts:
                platform = social_media_account['platform']
                username = social_media_account['username']

                if platform == 'twitter':
                    x_url = f'https://x.com/{username}'
                    view.add_item(x_button(x_url))
                elif platform == 'instagram':
                    instagram_url=f'https://www.instagram.com/{username}'
                    view.add_item(instagram_button(instagram_url))
                else:
                    embed = general_err_embed(account_data)

        await ctx.respond(
            embed=embed,
            view=view,
            ephemeral=not visibility
        )


def setup(bot):
    bot.add_cog(address_converter(bot))
