from discord import Embed

from embed.err_embed import general_err_embed
from utils.load_config import load_config_from_json, update_config_to_json


async def fav_collection_button_callback(
        interaction,
        author_id,
        favorite_collections,
        collection_name,
        collection
    ):
    if author_id != interaction.user.id:
        return

    embed = Embed(color=0xFFA46E)
    if interaction.data['custom_id'] == '❤️':
        if len(favorite_collections) >= 20:
            embed = general_err_embed(
                'You can only have 20 favorite collection slots.')
        else:
            favorite_collections[collection_name] = {
                'slug': collection
            }
            update_config_to_json(
                uid=str(interaction.user.id),
                favorite_collections=favorite_collections
            )
            embed.title = 'Collection added'
            embed.description = f'The collection `{collection_name}` has added to your favorite collections.'
    else:
        del favorite_collections[collection_name]
        update_config_to_json(
            uid=str(interaction.user.id),
            favorite_collections=favorite_collections
        )
        embed.title = 'Collection removed'
        embed.description = f'The collection `{collection_name}` has removed from your favorite collections.'
    await interaction.response.send_message(embed=embed)