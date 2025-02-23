import json
import re

from discord import (ApplicationContext, Embed, IntegrationType,
                     InteractionContextType, Option)
from discord.ext import commands
from discord.ui import Button, View
from discord.utils import basic_autocomplete

from api.get_os_nft import get_os_nft
from callback.fav_nft_button_callback import fav_nft_button_callback
from embed.err_embed import general_err_embed, missing_param_embed
from embed.opensea_nft_embed import opensea_nft_embed
from utils.chain import get_code_by_name, get_info_by_code
from utils.load_config import load_config_from_json
from view.button import (download_img_button, exp_button, favorite_nft_button,
                         metadata_button, opensea_button)


class opensea_nft(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    def collection_name_data(ctx):
        (
            _,
            _,
            _,
            _,
            favorite_nfts
        ) = load_config_from_json(str(ctx.interaction.user.id))
        favorite_nfts_prefix = []
        for favorite_nft in favorite_nfts:
            favorite_nfts_prefix.append(f'[💗] {favorite_nft}')

        with open('collection_name_data.json', 'r', encoding='utf-8') as of:
            collection_name_data = json.load(of)
        return favorite_nfts_prefix + ['[Manually enter contract address]'] + list(collection_name_data.keys())

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
            "Select a collection from the list below or select [Manually enter contract address]",
            autocomplete=basic_autocomplete(collection_name_data)
        ),
        token_id: Option(
            str,
            'The token id of the NFT.',
            required=False,
            autocomplete=basic_autocomplete(token_id_autocomplete)
        ),
        chain: Option(
            str,
            'The blockchain of the NFT.',
            required=False,
            autocomplete=basic_autocomplete(chain_autocomplete)
        ),
        address: Option(
            str,
            'The contract address of the NFT.',
            required=False,
            autocomplete=basic_autocomplete(address_autocomplete)
        ),

    ):
        mid = str(ctx.author.id)
        (
            enable_link_button,
            _,
            visibility,
            _,
            favorite_nfts
        ) = load_config_from_json(mid)
        disable_link_button = not enable_link_button

        with open('collection_name_data.json', 'r') as of:
            collection_name_data = json.load(of)

        if quick_select in collection_name_data:  # token_id
            if token_id == None:
                await ctx.respond(embed=missing_param_embed('token_id'), ephemeral=not visibility)
                return

            chain = collection_name_data[quick_select]['chain']
            address = collection_name_data[quick_select]['address']

        elif quick_select.startswith('[💗] '):  # (None)
            quick_select = re.sub(
                r'^\[💗\] ',
                '',
                quick_select
            )
            chain = favorite_nfts[quick_select]['chain']
            address = favorite_nfts[quick_select]['address']
            token_id = favorite_nfts[quick_select]['token_id']

        # token_id, chain, address
        elif quick_select == '[Manually enter contract address]':
            if token_id == None:
                await ctx.respond(embed=missing_param_embed('token_id'), ephemeral=not visibility)
                return
            elif chain == None:
                await ctx.respond(embed=missing_param_embed('chain'), ephemeral=not visibility)
                return
            if address == None:
                await ctx.respond(embed=missing_param_embed('address'), ephemeral=not visibility)
                return

            chain = get_code_by_name(chain)

        else:  # ignore
            reason = 'Wrong input. Please check the input of <quick_select>. If you wish to enter the collection info manually, select [Manually enter contract address]'
            await ctx.respond(embed=general_err_embed(reason), ephemeral=not visibility)
            return

        (success, nft_data) = get_os_nft(chain, address, token_id)
        embed = Embed()
        view = View()

        if success:
            nft_data = nft_data['nft']
            embed = opensea_nft_embed(chain, nft_data)
            (
                _,
                exp_name,
                _,
                exp_token_url,
                exp_emoji,
                _,
                _
            ) = get_info_by_code(chain)
            opensea_url = nft_data['opensea_url']
            original_img_url = nft_data['image_url']
            metadata_url = nft_data['metadata_url']
            view.add_item(opensea_button(opensea_url))
            view.add_item(exp_button(
                exp_name,
                exp_token_url,
                exp_emoji
            ))
            view.add_item(download_img_button(original_img_url))
            if len(metadata_url) < 128: view.add_item(metadata_button(metadata_url))
            fav_nft_button = Button()
            nft_name = nft_data['name']
            if nft_name in favorite_nfts:
                fav_nft_button = favorite_nft_button(
                    'Remove from favorite',
                    '🖤'
                )
            else:
                fav_nft_button = favorite_nft_button(
                    'Add to favorite',
                    '❤️'
                )

            fav_nft_button.callback = lambda interaction: fav_nft_button_callback(
                interaction,
                ctx.author.id,
                favorite_nfts,
                nft_name,
                chain,
                address,
                token_id
            )
            view.add_item(fav_nft_button)            
        else:
            embed=general_err_embed(nft_data)

        await ctx.respond(
            embed=embed,
            view=view
        )


def setup(bot):
    bot.add_cog(opensea_nft(bot))
