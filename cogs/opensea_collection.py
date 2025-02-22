import json
import re

from discord import (ApplicationContext, Embed, IntegrationType,
                     InteractionContextType, Option)
from discord.ext import commands
from discord.ui import Button, View
from discord.utils import basic_autocomplete

from api.get_os_collection import get_os_collection
from callback.fav_collection_button_callback import \
    fav_collection_button_callback
from embed.err_embed import general_err_embed
from embed.opensea_collection_embed import opensea_collection_embed
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
            _,
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

        (success, collection_data) = get_os_collection(collection)

        embed = Embed()
        view = View()

        if success:
            embed = opensea_collection_embed(collection_data, collection, view)

            collection_name = collection_data['name']
            description = collection_data['description']
            if description != '':
                description = f'>>> {description}'

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
