from discord import Embed

from embed.err_embed import general_err_embed
from utils.load_config import update_config_to_json


async def fav_nft_button_callback(
    interaction,
    author_id,
    favorite_nfts,
    nft_name,
    chain,
    address,
    token_id
):
    if author_id != interaction.user.id:
        return

    embed = Embed(color=0xFFA46E)
    if interaction.data['custom_id'] == '❤️':
        if len(favorite_nfts) >= 20:
            embed = general_err_embed('You can only have 20 favorite NFT slots.')
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
            embed.description = f'The NFT `{nft_name}` has added to your favorite NFTs.'
    else:
        del favorite_nfts[nft_name]
        update_config_to_json(
            uid=str(interaction.user.id),
            favorite_nfts=favorite_nfts
        )
        embed.title = 'NFT removed'
        embed.description = f'The NFT `{nft_name}` has removed from your favorite NFTs.'
    await interaction.response.send_message(embed=embed)
