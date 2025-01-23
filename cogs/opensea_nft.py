import json
from discord import (ApplicationContext, AutocompleteContext, ButtonStyle, Embed, IntegrationType,
                     InteractionContextType, Option, PartialEmoji)
from discord.ext import commands
from discord.ui import Button, View
from discord.utils import basic_autocomplete

from api.get_os_nft import get_os_nft
from utils.load_config import load_config_from_json
from utils.str_datetime_to_timestamp import str_datetime_to_timestamp
from utils.chain import get_info_by_code

class opensea_nft(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    def get_chain_code_from_name(chain_name):
        with open('chain_detail.json', 'r') as file:
            data = json.load(file)
        for k, v in data.items():
            if v['chain_name'] == chain_name: return k

    def collection_name_autocomplete(self: AutocompleteContext):
        with open('collection_name_autocomplete.json', 'r', encoding='utf-8') as of:
            collection_name_data = json.load(of)
        return ['[Manually enter contract address]'] + list(collection_name_data.keys())

    def chain_autocomplete(ctx):
        quick_select = ctx.options.get('quick_select')
        if quick_select == '[Manually enter contract address]':
            with open('chain_detail.json', 'r') as file:
                data = json.load(file)
            return [v['chain_name'] for v in data.values()]
        else:
            return ["(empty) This field is not required since you've selected the collection name"]

    def address_autocomplete(ctx):
        quick_select = ctx.options.get('quick_select')
        if quick_select == '[Manually enter contract address]':
            return []
        else:
            return ["(empty) This field is not required since you've selected the collection name"]

    def token_id_autocomplete(ctx):
        return []
        
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
        chain: Option(
            str,
            'The chain of the NFT',
            required=False,
            autocomplete=basic_autocomplete(chain_autocomplete)
        ),
        address: Option(
            str,
            'The address of the NFT',
            required=False,
            autocomplete=basic_autocomplete(address_autocomplete)
        ),
        token_id: Option(
            str,
            'The token id of the NFT',
            required=False,
            autocomplete=basic_autocomplete(token_id_autocomplete)
        )        
    ):


        await ctx.defer()

        with open('collection_name_autocomplete.json', 'r') as of:
            collection_name_data = json.load(of)

        if quick_select in collection_name_data:
            chain = collection_name_data[quick_select]['chain']
            address = collection_name_data[quick_select]['address']

        #     embed.title = 'Select '
        #     await ctx.respond('edit and add select menu + input modal')
        # elif quick_select.startswith('[❤️]'):
        #     await ctx.respond('read slug in setting')
        # elif quick_select in collection_name_data:
        #     quick_select = collection_name_data[quick_select]['slug']
        #     print('call func to get embed')
        # else:
        #     print('collection not found')
        #     embed.title = '[Failed]'
        #     embed.description = f'Command execution failed. Reason:\n```{
        #         account_data}```'

            


        # await ctx.respond(embed=embed, view=view)


        (success, nft_data) = get_os_nft(chain, address, token_id)
        embed = Embed(color=0xFFA46E)
        view = View()

        if success:
            with open('collection_name_autocomplete.json', 'r', encoding='utf-8') as of:
                collection_name_data = json.load(of)
            nft_data = nft_data['nft']
            contract = nft_data['contract']
            token_standard = nft_data['token_standard']
            collection = nft_data['collection']
            for c in collection_name_data:
                if collection_name_data[c]['slug'] == collection:
                    collection = c
                    break
            identifier = nft_data['identifier']
            nft_name = f'{collection}#{identifier}'
            display_img_url = nft_data['display_image_url']
            original_img_url = nft_data['image_url']
            metadata_url = nft_data['metadata_url']
            opensea_url = nft_data['opensea_url']
            last_update_time = str_datetime_to_timestamp(nft_data['updated_at'])

            is_disabled = nft_data['is_disabled']
            is_nsfw = nft_data['is_nsfw']
            is_suspicious = nft_data['is_suspicious']

            (chain_name, _, exp_url, _, _) = get_info_by_code(chain)

            creator_address = nft_data['creator']
            creator_os_url = f'https://www.opensea.io/{creator_address}'
            owners = nft_data['owners']
            owner_text = ''
            if len(owners) == 1:
                owner = owners[0]
                owner_address = owner['address']
                owner_exp_url = f'{exp_url}{owner_address}'
                owner_os_url = f'https://www.opensea.io/{owner_address}'
                owner_text = f'[exp]({owner_exp_url})｜[os]({owner_os_url})'
                print(owner_text)

            rarity_rk = nft_data['rarity']['rank']
            

            embed.title = f'OpenSea NFT Info of {nft_name}'
            # embed.set_thumbnail(url=pfp_img)
            # if banner_img != '':
            #     embed.set_image(url=display_img_url)
            embed.set_footer(
                text='Source: OpenSea API',
                icon_url='https://raw.githubusercontent.com/Xeift/Kizmeow-NFT-Discord-Bot/refs/heads/main/img/opensea_logo.png'
            )

            await ctx.respond(embed=embed)
#                 embed.add_field(
#                     name='Address', value=f'[{address}]({etherscan_url})', inline=False)
#                 embed.add_field(name='Username', value=username, inline=True)
#                 embed.add_field(name='Bio', value=bio, inline=True)
#                 embed.add_field(name='Joined Date', value=joined_date, inline=True)
#                 embed.add_field(
#                     name='', value='Note: buttons are disabled by default. If you wish to enable the buttons, set `enable_link_button` parameter to `False`.', inline=False)
#                 embed.set_footer(
#                     text='Source: OpenSea API',
#                     icon_url='https://raw.githubusercontent.com/Xeift/Kizmeow-NFT-Discord-Bot/refs/heads/main/img/opensea_logo.png'
#                 )
#                 opensea_button = Button(
#                     label='OpenSea',
#                     style=ButtonStyle.link,
#                     url=opensea_url,
#                     emoji=PartialEmoji(name='opensea_icon_transparent',
#                                        id=1300799256730538047),
#                     disabled=disable_link_button
#                 )
#                 view.add_item(opensea_button)
# 
#                 etherscan_button = Button(
#                     label='Etherscan',
#                     style=ButtonStyle.link,
#                     url=etherscan_url,
#                     emoji=PartialEmoji(name='etherscan_icon_transparent',
#                                        id=1300797214720917596),
#                     disabled=disable_link_button
#                 )
#                 view.add_item(etherscan_button)
# 
#                 website_button = Button(
#                     label='Website',
#                     style=ButtonStyle.link,
#                     url=website_url,
#                     emoji='🔗',
#                     disabled=disable_link_button
#                 )
#                 if website_url != '':
#                     view.add_item(website_button)
# 
#                 for social_media_account in social_media_accounts:
#                     platform = social_media_account['platform']
#                     username = social_media_account['username']
# 
#                     if platform == 'twitter':
#                         x_button = Button(
#                             label='X',
#                             style=ButtonStyle.link,
#                             url=f'https://x.com/{username}',
#                             emoji=PartialEmoji(name='x_icon_transparent',
#                                                id=1300788826905772063),
#                             disabled=disable_link_button
#                         )
#                         view.add_item(x_button)
#                     elif platform == 'instagram':
#                         instagram_button = Button(
#                             label='Instagram',
#                             style=ButtonStyle.link,
#                             url=f'https://www.instagram.com/{username}',
#                             emoji=PartialEmoji(
#                                 name='instagram_icon_transparent', id=1300788845842927708),
#                             disabled=disable_link_button
#                         )
#                         view.add_item(instagram_button)
# 
#                 returm (embed. view)

def setup(bot):
    bot.add_cog(opensea_nft(bot))
