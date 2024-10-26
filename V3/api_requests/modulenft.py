import datetime
import os

import discord
import requests
from buttons.buttons import looksrare_button, opensea_button, x2y2_button
from discord.ui import View


async def modulenft_embed(collection):

    
    url = f'https://api.modulenft.xyz/api/v2/eth/nft/collection?slug={collection}'
    headers = {
        'accept': 'application/json',
        'X-API-KEY': os.getenv('MODULENFT_API_KEY')
    }
    r = requests.get(url, headers=headers).json()['data']

    
    name = r['name']
    slug = r['slug']
    description = r['description']
    external_url = r['socials']['external_url']
    discord_url = r['socials']['discord_url']
    twitter_url = f"https://twitter.com/{r['socials']['twitter_username']}"
    image_url = r['images']['image_url']
    banner_image_url = r['images']['banner_image_url']
    createdDate = int(datetime.datetime.fromisoformat(r['createdDate']).timestamp())


    embed = discord.Embed(title='', color=0xFFA46E)
    embed.set_image(url=banner_image_url)
    embed.add_field(name='Description', value=f'{description}', inline=False)
    embed.add_field(name='Created', value=f'<t:{createdDate}:R>', inline=False)
    embed.add_field(name='_ _', value=f'[Website]({external_url})║[Discord]({discord_url})║[Twitter]({twitter_url})', inline=False)
    embed.set_author(name=f'{name}', url=f'https://opensea.io/collection/{slug}', icon_url=image_url)
    embed.set_footer(text='Data provided by Kizmeow NFT Bot', icon_url='https://user-images.githubusercontent.com/80938768/204983971-d7cf0e40-f4ce-4737-ba07-85ed62112dab.png')
    embed.timestamp = datetime.datetime.now()

    
    view = View(timeout=None)
    view.add_item(opensea_button)
    view.add_item(looksrare_button)
    # view.add_item(x2y2_button)

    
    return (embed, view)