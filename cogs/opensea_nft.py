import json
import re

from discord import (ApplicationContext, AutocompleteContext, ButtonStyle,
                     Embed, IntegrationType, InteractionContextType, Option,
                     PartialEmoji)
from discord.ext import commands
from discord.ui import Button, View
from discord.utils import basic_autocomplete

from api.get_os_nft import get_os_nft
from utils.chain import get_code_by_name, get_info_by_code
from utils.datetime_to_timestamp import datetime_to_timestamp
from utils.err_embed import general_err_embed, missing_param_embed
from utils.load_config import load_config_from_json, update_config_to_json


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
            'Select the collection. [Quick Select]',
            autocomplete=basic_autocomplete(collection_name_data)
        ),
        token_id: Option(
            str,
            'The token id of the NFT',
            required=False,
            autocomplete=basic_autocomplete(token_id_autocomplete)
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
        embed = Embed(color=0xFFA46E)
        view = View()

        if success:
            (chain_name, exp_name, exp_address_url,
             exp_token_url, exp_emoji, _, token_standards) = get_info_by_code(chain)

            with open('collection_name_data.json', 'r', encoding='utf-8') as of:
                collection_name_data = json.load(of)
            nft_data = nft_data['nft']
            contract = nft_data['contract']
            contract_address_short = contract[:7]
            contract_exp_url = f'{exp_token_url}{contract}'

            token_standard = nft_data['token_standard']
            for ts in token_standards:
                if token_standard == ts:
                    token_standard = token_standards[ts]
                    break

            collection = nft_data['collection']
            for c in collection_name_data:
                if collection_name_data[c]['slug'] == collection:
                    collection = c
                    break
            identifier = nft_data['identifier']
            if len(identifier) > 7:
                identifier = identifier[:7]

            nft_name = nft_data['name']
            if nft_name == None:
                nft_name = f'{collection}#{identifier}'

            display_img_url = nft_data['display_image_url']

            opensea_url = nft_data['opensea_url']
            opensea_button = Button(
                label='OpenSea',
                style=ButtonStyle.link,
                url=opensea_url,
                emoji=PartialEmoji(name='opensea_icon',
                                   id=1326452492644515963),
                disabled=disable_link_button
            )
            view.add_item(opensea_button)

            exp_button = Button(
                label=exp_name,
                style=ButtonStyle.link,
                url=f'{exp_token_url}{address}',
                emoji=PartialEmoji(name=f'{exp_token_url.lower()}_logo',
                                   id=exp_emoji),
                disabled=disable_link_button
            )
            view.add_item(exp_button)

            original_img_url = nft_data['image_url']
            download_img_button = Button(
                label='Download Full Resolution Image',
                style=ButtonStyle.link,
                url=original_img_url,
                emoji='🖼️',
                disabled=disable_link_button
            )
            view.add_item(download_img_button)

            metadata_url = nft_data['metadata_url']
            metadata_button = Button(
                label='View NFT Metadata',
                style=ButtonStyle.link,
                url=metadata_url,
                emoji='💾',
                disabled=disable_link_button
            )
            view.add_item(metadata_button)

            last_update_time = datetime_to_timestamp(
                nft_data['updated_at'])

            # is_disabled = nft_data['is_disabled']
            # is_nsfw = nft_data['is_nsfw']
            # is_suspicious = nft_data['is_suspicious']

            creator_address = nft_data['creator']
            if creator_address != None:
                creator_address_short = creator_address[:7]
                creator_os_url = f'https://www.opensea.io/{creator_address}'

            owners = nft_data['owners']
            owner_text = ''
            if owners == None:
                owner_text = '(Too much owners!)'
            elif len(owners) == 1:
                owner = owners[0]
                owner_address = owner['address']
                owner_address_short = owner['address'][:7]
                owner_exp_url = f'{exp_address_url}{owner_address}'
                owner_os_url = f'https://www.opensea.io/{owner_address}'
                owner_text = f'{owner_address_short}\n[Exp]({owner_exp_url})｜[OpenSea]({
                    owner_os_url})'
            elif len(owners) <= 5:
                for owner in owners:
                    owner_address = owner['address']
                    owner_address_short = owner['address'][:7]
                    owner_exp_url = f'{exp_address_url}{owner_address}'
                    owner_os_url = f'https://www.opensea.io/{owner_address}'
                    owner_text += f'{owner_address_short} [Exp]({owner_exp_url})｜[OpenSea]({
                        owner_os_url})\n'
            else:
                owner_text = f'({len(owners)} owners)'

            rarity_rk = 0
            if nft_data['rarity'] != None:
                rarity_rk = nft_data['rarity']['rank']

            embed.title = nft_name
            embed.set_image(url=display_img_url)
            embed.set_footer(
                text='Source: OpenSea API',
                icon_url='https://raw.githubusercontent.com/Xeift/Kizmeow-NFT-Discord-Bot/refs/heads/main/img/opensea_logo.png'
            )
            embed.add_field(
                name='Contract Address',
                value=f'[{contract_address_short}]({contract_exp_url})',
            )
            embed.add_field(
                name='Owner',
                value=owner_text
            )
            if creator_address != None:
                embed.add_field(
                    name='Creator',
                    value=f'{creator_address_short}\n[Exp]({exp_address_url}{
                        creator_address})｜[OpenSea]({creator_os_url})'
                )
            embed.add_field(
                name='Chain',
                value=chain_name
            )
            embed.add_field(
                name='Token Standard',
                value=token_standard
            )
            if rarity_rk != 0:
                embed.add_field(
                    name='Rarity Rank',
                    value=rarity_rk
                )

            embed.add_field(
                name='Last Update Time',
                value=f'<t:{last_update_time}:D>'
            )

            embed.add_field(
                name='════════════    Traits    ════════════',
                value='',
                inline=False
            )
            traits = nft_data['traits']
            if traits != None:
                for trait in traits:
                    type = trait['trait_type']
                    value = trait['value']

                    embed.add_field(
                        name=type,
                        value=value if value != None else ''
                    )

            fav_nft_button = Button(
                style=ButtonStyle.primary,
            )
            if nft_name in favorite_nfts:
                fav_nft_button.label = 'Remove from favorite'
                fav_nft_button.emoji = '🖤'
                add_to_favorite = False
            else:
                fav_nft_button.label = 'Add to favorite'
                fav_nft_button.emoji = '❤️'
                add_to_favorite = True

            async def fav_nft_button_callback(interaction):
                if ctx.author != interaction.user:
                    return

                embed = Embed(color=0xFFA46E)
                if add_to_favorite:
                    if len(favorite_nfts) >= 20:
                        embed = general_err_embed(
                            'You can only have 20 favorite NFT slots.')
                    else:
                        favorite_nfts[nft_name] = {
                            'chain': chain,
                            'address': address,
                            'token_id': token_id
                        }
                        update_config_to_json(
                            uid=str(interaction.user.id),
                            favorite_nfts=favorite_nfts
                        )
                        embed.title = 'NFT added'
                        embed.description = f'The NFT `{
                            nft_name}` has added to your favorite NFTs.'
                else:
                    del favorite_nfts[nft_name]
                    update_config_to_json(
                        uid=str(interaction.user.id),
                        favorite_nfts=favorite_nfts
                    )
                    embed.title = 'NFT removed'
                    embed.description = f'The NFT `{
                        nft_name}` has removed from your favorite NFTs.'
                await interaction.response.send_message(embed=embed, ephemeral=not visibility)

            fav_nft_button.callback = fav_nft_button_callback
            view.add_item(fav_nft_button)            
        else:
            embed.title = '[Failed]'
            embed.description = f'Command execution failed. Reason:\n```{
                nft_data}```'

        await ctx.respond(embed=embed, view=view, ephemeral=not visibility)


def setup(bot):
    bot.add_cog(opensea_nft(bot))
