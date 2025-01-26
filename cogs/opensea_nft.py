import json

from discord import (ApplicationContext, AutocompleteContext, ButtonStyle,
                     Embed, IntegrationType, InteractionContextType, Option,
                     PartialEmoji)
from discord.ext import commands
from discord.ui import Button, View
from discord.utils import basic_autocomplete

from api.get_os_nft import get_os_nft
from utils.chain import get_info_by_code
from utils.datetime_to_timestamp import datetime_to_timestamp
from utils.load_config import load_config_from_json


class opensea_nft(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    def get_chain_code_from_name(chain_name):
        with open('chain_detail.json', 'r') as file:
            data = json.load(file)
        for k, v in data.items():
            if v['chain_name'] == chain_name:
                return k

    def collection_name_data(self: AutocompleteContext):
        with open('collection_name_data.json', 'r', encoding='utf-8') as of:
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
            autocomplete=basic_autocomplete(collection_name_data)
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

        with open('collection_name_data.json', 'r') as of:
            collection_name_data = json.load(of)

        if quick_select in collection_name_data:
            chain = collection_name_data[quick_select]['chain']
            address = collection_name_data[quick_select]['address']

        elif quick_select.startswith('[❤️]'):
            # TODO: add favorite NFT, favorite token
            print('read chain, address, token_id in setting')

        (success, nft_data) = get_os_nft(chain, address, token_id)
        embed = Embed(color=0xFFA46E)
        view = View()

        if success:
            (chain_name, _, exp_url, _, _) = get_info_by_code(chain)

            with open('collection_name_data.json', 'r', encoding='utf-8') as of:
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
            last_update_time = datetime_to_timestamp(
                nft_data['updated_at'])

            is_disabled = nft_data['is_disabled']
            is_nsfw = nft_data['is_nsfw']
            is_suspicious = nft_data['is_suspicious']

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

            rarity_rk = nft_data['rarity']['rank']  # TODO: deal with null

            embed.title = f'OpenSea NFT Info of {nft_name}'
            embed.set_image(url=display_img_url)
            embed.set_footer(
                text='Source: OpenSea API',
                icon_url='https://raw.githubusercontent.com/Xeift/Kizmeow-NFT-Discord-Bot/refs/heads/main/img/opensea_logo.png'
            )
            embed.add_field(
                name='Contract Address',
                value=f''
            )

            await ctx.respond(embed=embed)


def setup(bot):
    bot.add_cog(opensea_nft(bot))
