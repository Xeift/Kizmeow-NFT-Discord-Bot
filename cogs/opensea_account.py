
from discord import (ApplicationContext, ButtonStyle, Embed, IntegrationType,
                     InteractionContextType, Option, PartialEmoji)
from discord.ext import commands
from discord.ui import Button, View

from api.get_os_account import get_os_account


class opensea_account(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(
        name='opensea_account',
        description='View account details of a specific OpenSea account',
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
    async def opensea_account(
        self,
        ctx: ApplicationContext,
        address_or_username: Option(
            str, 'EVM address(ENS supported) or username on OpenSea'),
        enable_link_button: Option(bool, 'Enable link button. Disabled by default. Sharing personal X link may break rules in some servers.', default=False),
    ):
        await ctx.defer()
        disable_link_button = not enable_link_button
        (success, account_data) = get_os_account(address_or_username)
        embed = Embed(color=0xFFA46E)
        view = View()

        if success:
            address = account_data['address']
            username = account_data['username']
            bio = account_data['bio']
            joined_date = account_data['joined_date']
            short_address = account_data['address'][:7]
            pfp_img = account_data['profile_image_url']
            banner_img = account_data['banner_image_url']
            opensea_url = f'https://opensea.io/{address}'
            etherscan_url = f'https://etherscan.io/address/{address}'
            website_url = account_data['website']
            social_media_accounts = account_data['social_media_accounts']

            embed.title = f'OpenSea Account Info of {short_address}'
            embed.set_thumbnail(url=pfp_img)
            if banner_img != '':
                embed.set_image(url=banner_img)
            embed.set_footer(
                text='Source: OpenSea API',
                icon_url='https://raw.githubusercontent.com/Xeift/Kizmeow-NFT-Discord-Bot/refs/heads/main/img/opensea_logo.png'
            )

            embed.add_field(
                name='Address', value=f'[{address}]({etherscan_url})', inline=False)
            embed.add_field(name='Username', value=username, inline=True)
            embed.add_field(name='Bio', value=bio, inline=True)
            embed.add_field(name='Joined Date', value=joined_date, inline=True)
            embed.add_field(
                name='', value='Note: buttons are disabled by default. If you wish to enable the buttons, set `enable_link_button` parameter to `False`.', inline=False)

            opensea_button = Button(
                label='OpenSea',
                style=ButtonStyle.link,
                url=opensea_url,
                emoji=PartialEmoji(name='opensea_icon_transparent',
                                   id=1300799256730538047),
                disabled=disable_link_button
            )
            view.add_item(opensea_button)

            etherscan_button = Button(
                label='Etherscan',
                style=ButtonStyle.link,
                url=etherscan_url,
                emoji=PartialEmoji(name='etherscan_icon_transparent',
                                   id=1300797214720917596),
                disabled=disable_link_button
            )
            view.add_item(etherscan_button)

            website_button = Button(
                label='Website',
                style=ButtonStyle.link,
                url=website_url,
                emoji='🔗',
                disabled=disable_link_button
            )
            if website_url != '':
                view.add_item(website_button)

            for social_media_account in social_media_accounts:
                platform = social_media_account['platform']
                username = social_media_account['username']

                if platform == 'twitter':
                    x_button = Button(
                        label='X',
                        style=ButtonStyle.link,
                        url=f'https://x.com/{username}',
                        emoji=PartialEmoji(name='x_icon_transparent',
                                           id=1300788826905772063),
                        disabled=disable_link_button
                    )
                    view.add_item(x_button)
                elif platform == 'instagram':
                    instagram_button = Button(
                        label='Instagram',
                        style=ButtonStyle.link,
                        url=f'https://www.instagram.com/{username}',
                        emoji=PartialEmoji(
                            name='instagram_icon_transparent', id=1300788845842927708),
                        disabled=disable_link_button
                    )
                    view.add_item(instagram_button)

        else:
            embed.title = '[Failed]'
            embed.description = f'Command execution failed. Reason:\n```{
                account_data}```'

        await ctx.respond(embed=embed, view=view)


def setup(bot):
    bot.add_cog(opensea_account(bot))
