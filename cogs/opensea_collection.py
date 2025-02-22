import json
import re

from discord import (ApplicationContext, Embed, IntegrationType,
                     InteractionContextType, Option)
from discord.ext import commands
from discord.ui import Button, View
from discord.utils import basic_autocomplete

from api.get_os_collection import get_os_collection
from api.get_os_collection_statistics import get_os_collection_statistics
from callback.fav_collection_button_callback import \
    fav_collection_button_callback
from embed.err_embed import general_err_embed
from utils.chain import get_info_by_code
from utils.load_config import load_config_from_json
from view.button import (discord_button, exp_button,
                         favorite_collection_button, instagram_button,
                         opensea_button, telegram_button, website_button,
                         wiki_button, x_button)


class opensea_collection(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    def collection_name_data(ctx):
        (
            _,
            _,
            _,
            favorite_collections,
            _
        ) = load_config_from_json(str(ctx.interaction.user.id))
        favorite_collections_prefix = []
        for favorite_collection in favorite_collections:
            favorite_collections_prefix.append(f'[💗] {favorite_collection}')
        with open('collection_name_data.json', 'r', encoding='utf-8') as of:
            collection_name_data = json.load(of)

        final_collection_name_data = favorite_collections_prefix + \
            list(collection_name_data.keys())
        return final_collection_name_data

    @commands.slash_command(
        name='opensea_collection',
        description='View details of a specific OpenSea NFT collection',
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
    async def opensea_collection(
        self,
        ctx: ApplicationContext,
        collection: Option(
            str,
            'Select a collection from the list below or enter the collection slug manually.',
            autocomplete=basic_autocomplete(collection_name_data)
        )
    ):
        mid = str(ctx.author.id)
        (
            enable_link_button,
            _,
            visibility,
            favorite_collections,
            _
        ) = load_config_from_json(mid)
        with open('collection_name_data.json', 'r') as of:
            collection_name_data = json.load(of)
        if collection in collection_name_data:
            collection = collection_name_data[collection]['slug']
        elif collection.startswith('[💗] '):
            collection = re.sub(
                r'^\[💗\] ',
                '',
                collection
            )
            collection = favorite_collections[collection]['slug']

        disable_link_button = not enable_link_button
        (success, collection_data) = get_os_collection(collection)

        embed = Embed(color=0xFFA46E)
        view = View()

        if success:
            collection_name = collection_data['name']
            cas = collection_data['contracts']
            cas_text = ''
            description = collection_data['description']
            if description != '':
                description = f'>>> {description}'
            supply = collection_data['total_supply']
            category = collection_data['category']
            created_date = collection_data['created_date']
            owner_address = collection_data['owner']
            owner_address_short = collection_data['owner'][:7]
            default_chain = collection_data['payment_tokens'][0]['chain'] if cas == [
            ] else cas[0]['chain']
            (chain_name, exp_name, exp_address_url, exp_token_url, _,
             ticker, _) = get_info_by_code(default_chain)
            owner_exp_url = f'{exp_address_url}{owner_address}'
            owner_os_url = f'https://opensea.io/{owner_address}'
            fees = collection_data['fees']
            fees_text = ''
            verify_state = collection_data['safelist_status']
            pfp_img = collection_data['image_url']
            banner_img = collection_data['banner_image_url']

            opensea_url = collection_data['opensea_url']
            website_url = collection_data['project_url']
            wiki_url = collection_data['wiki_url']
            discord_url = collection_data['discord_url']
            telegram_url = collection_data['telegram_url']
            x_username = collection_data['twitter_username']
            x_url = f'https://x.com/{x_username}'
            instagram_username = collection_data['instagram_username']
            instagram_url = f'https://www.instagram.com/{instagram_username}'

            if opensea_url: view.add_item(opensea_button(opensea_url))
            if website_url: view.add_item(website_button(website_url))
            if wiki_url: view.add_item(wiki_button(wiki_url))
            if discord_url: view.add_item(discord_button(discord_url))
            if telegram_url: view.add_item(telegram_button(telegram_url))
            if x_username: view.add_item(x_button(x_url))
            if instagram_username: view.add_item(instagram_button(instagram_url))

            embed.title = f'{collection_name}'
            embed.set_thumbnail(url=pfp_img)
            if banner_img != '':
                embed.set_image(url=banner_img)

                for ca in cas:
                    chain = ca['chain']
                    address = ca['address']
                    (
                        chain_name,
                        exp_name,
                        exp_address_url,
                        exp_token_url,
                        exp_emoji,
                        ticker,
                        _
                    ) = get_info_by_code(chain)


                    view.add_item(exp_button(
                        exp_name,
                        f'{exp_token_url}{address}',
                        exp_emoji
                    ))
                    cas_text += f"[{ca['address'][:7]}]({exp_token_url}{ca['address']}) ({chain_name})\n"

            if cas_text != '':
                embed.add_field(name='Contract Address',
                                value=cas_text, inline=False)
            embed.add_field(name='Description',
                            value=description, inline=False)
            embed.add_field(name='Total Supply', value=supply, inline=True)
            embed.add_field(name='Category', value=category, inline=True)
            embed.add_field(name='Created Date',
                            value=created_date, inline=True)
            if cas != []:
                embed.add_field(
                    name='Owner',
                    value=f'{owner_address_short} ({chain_name})\n[Exp]({owner_exp_url})｜[OpenSea]({owner_os_url})',
                    inline=True
                )
            for fee in fees:
                if fee['required'] == True:
                    fee['required'] = 'Required'
                else:
                    fee['required'] = 'Optional'

                fees_text += f"{fee['required']} [{fee['fee']}%]({exp_address_url}{fee['recipient']})\n"
            embed.add_field(name='Fees', value=fees_text, inline=True)
            embed.add_field(name='Verification',
                            value=verify_state, inline=True)
            embed.set_footer(
                text='Source: OpenSea API',
                icon_url='https://raw.githubusercontent.com/Xeift/Kizmeow-NFT-Discord-Bot/refs/heads/main/img/opensea_logo.png'
            )
            (success, collection_statistic_data) = get_os_collection_statistics(collection)
            if success:
                num_holders = collection_statistic_data['total']['num_owners']
                market_cap = round(
                    collection_statistic_data['total']['market_cap'], 2)
                floor_price = round(
                    collection_statistic_data['total']['floor_price'], 2)

                volume_all = round(
                    collection_statistic_data['total']['volume'], 2)
                volume_1d = round(
                    collection_statistic_data['intervals'][0]['volume'], 2)
                volume_1d_del = round(
                    collection_statistic_data['intervals'][0]['volume_change'], 2)
                volume_7d = round(
                    collection_statistic_data['intervals'][1]['volume'], 2)
                volume_7d_del = round(
                    collection_statistic_data['intervals'][1]['volume_change'], 2)
                volume_30d = round(
                    collection_statistic_data['intervals'][2]['volume'], 2)
                volume_30d_del = round(
                    collection_statistic_data['intervals'][2]['volume_change'], 2)

                sales_all = round(
                    collection_statistic_data['total']['sales'], 2)
                sales_1d = round(
                    collection_statistic_data['intervals'][0]['sales'], 2)
                sales_7d = round(
                    collection_statistic_data['intervals'][1]['sales'], 2)
                sales_30d = round(
                    collection_statistic_data['intervals'][2]['sales'], 2)

                average_price_all = round(
                    collection_statistic_data['total']['average_price'], 2)
                average_price_1d = round(
                    collection_statistic_data['intervals'][0]['average_price'], 2)
                average_price_7d = round(
                    collection_statistic_data['intervals'][1]['average_price'], 2)
                average_price_30d = round(
                    collection_statistic_data['intervals'][2]['average_price'], 2)

                embed.add_field(
                    name='Unique Holders',
                    value=num_holders,
                    inline=True
                )
                embed.add_field(
                    name='Market Cap',
                    value=f'{market_cap} {ticker}',
                    inline=True
                )
                embed.add_field(
                    name='Floor Price',
                    value=f'{floor_price} {ticker}',
                    inline=True
                )
                embed.add_field(
                    name='Volume',
                    value=(
                        f'```1D  {str(volume_1d).ljust(12)}{ticker}({volume_1d_del}%)\n'
                        f'7D  {str(volume_7d).ljust(12)}{ticker}({volume_7d_del}%)\n'
                        f'30D {str(volume_30d).ljust(12)}{ticker}({volume_30d_del}%)\n'
                        f'All {str(volume_all).ljust(12)}{ticker}```'
                    ),
                    inline=False
                )
                embed.add_field(
                    name='Average Price',
                    value=(
                        f'`1D  {str(average_price_1d).ljust(8)} {ticker}`\n'
                        f'`7D  {str(average_price_7d).ljust(8)} {ticker}`\n'
                        f'`30D {str(average_price_30d).ljust(8)} {ticker}`\n'
                        f'`All {str(average_price_all).ljust(8)} {ticker}`'
                    ),
                    inline=True
                )
                embed.add_field(
                    name='Sales',
                    value=(
                        f'`1D  {str(sales_1d).ljust(8)} NFT`\n'
                        f'`7D  {str(sales_7d).ljust(8)} NFT`\n'
                        f'`30D {str(sales_30d).ljust(8)} NFT`\n'
                        f'`All {str(sales_all).ljust(8)} NFT`'
                    ),
                    inline=True
                )

                fav_collection_button = Button()
                if collection_name in favorite_collections:
                    fav_collection_button = favorite_collection_button(
                        'Remove from favorite',
                        '🖤'
                    )
                else:
                    fav_collection_button = favorite_collection_button(
                        'Add to favorite',
                        '❤️'
                    )

                fav_collection_button.callback = lambda interaction: fav_collection_button_callback(
                    interaction,
                    ctx.author.id,
                    favorite_collections,
                    collection_name,
                    collection
                )
                view.add_item(fav_collection_button)

        else:
            embed = general_err_embed(collection_data)

        await ctx.respond(embed=embed, view=view, ephemeral=not visibility)


def setup(bot):
    bot.add_cog(opensea_collection(bot))
