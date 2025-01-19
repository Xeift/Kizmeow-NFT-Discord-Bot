import json
from discord import (ApplicationContext, AutocompleteContext, ButtonStyle, Embed, IntegrationType,
                     InteractionContextType, Option, PartialEmoji)
from discord.ext import commands
from discord.ui import Button, View
from discord.utils import basic_autocomplete

from api.get_os_nft import get_os_nft
from utils.load_config import load_config_from_json


class opensea_nft(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    def collection_name_autocomplete(self: AutocompleteContext):
        with open('collection_name_autocomplete.json', 'r', encoding='utf-8') as of:
            collection_name_data = json.load(of)
        return ['[Manually enter contract address]'] + list(collection_name_data.keys())
        
    @commands.slash_command(
        name='opensea_nft',
        description='View details of a specific NFT on OpenSea',
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
    async def opensea_nft(
        self,
        ctx: ApplicationContext,
        quick_select: Option(
            str,
            'Select the collection. [Quick Select]',
            autocomplete=basic_autocomplete(collection_name_autocomplete)
        ),
        # chain: Option(
        #     str,
        #     'The chain of the NFT',
        #     required=False
        # ),
        # address: Option(
        #     str,
        #     'The address of the NFT',
        #     required=False
        # ),
    ):
        await ctx.defer()

        with open('collection_name_autocomplete.json', 'r') as of:
            collection_name_data = json.load(of)
            
        if quick_select == '[Manually enter contract address]':
            embed = Embed(color=0xFFA46E)
            embed.title = 'Select '
            await ctx.respond('edit and add select menu + input modal')
        elif quick_select.startwith('[❤️]'):
            await ctx.respond('read slug in setting')
        elif quick_select in collection_name_data:
            quick_select = collection_name_data[quick_select]['slug']
            print('call func to get embed')
        else:
            print('collection not found')
            embed.title = '[Failed]'
            embed.description = f'Command execution failed. Reason:\n```{
                account_data}```'

            
        def makeNftEmbed(chain, address, token_id):
            (success, nft_data) = get_os_nft(chain, address, token_id)
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
                embed.set_footer(
                    text='Source: OpenSea API',
                    icon_url='https://raw.githubusercontent.com/Xeift/Kizmeow-NFT-Discord-Bot/refs/heads/main/img/opensea_logo.png'
                )
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

                returm (embed. view)

        await ctx.respond(embed=embed, view=view)


def setup(bot):
    bot.add_cog(opensea_nft(bot))
