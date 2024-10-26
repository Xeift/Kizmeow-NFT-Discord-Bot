import requests
import datetime
import discord
from discord.ui import View
from buttons.buttons import etherscan_button, twitter_button, discord_button, site_button, facebook_button, telegram_button, instagram_button, medium_button, return_button

async def looksrare_embed(collection):
    url = f'https://api.opensea.io/api/v1/collection/{collection}'
    collection = requests.get(url).json()['collection']['primary_asset_contracts'][0]['address']
    
    url = f'https://api.looksrare.org/api/v1/collections?address={collection}'
    r = requests.get(url).json()['data']
    
    address = f"`{r['address']}`"
    name = r['name']
    type = f"`{r['type']}`"
    symbol = f"`{r['symbol']}`"
    isVerified = f"`{r['isVerified']}`"
    logoURI = r['logoURI']
    bannerURI = r['bannerURI']

    etherscan_button.url = 'https://www.youtube.com/watch?v=dQw4w9WgXcQ' if f'https://etherscan.io/address/{collection}' == None else f'https://etherscan.io/address/{collection}'
    site_button.url = 'https://www.youtube.com/watch?v=dQw4w9WgXcQ' if r['websiteLink'] == None else r['websiteLink']
    facebook_button.url = 'https://www.youtube.com/watch?v=dQw4w9WgXcQ' if r['facebookLink'] == None else r['facebookLink']
    twitter_button.url = 'https://www.youtube.com/watch?v=dQw4w9WgXcQ' if r['twitterLink'] == None else r['twitterLink']
    instagram_button.url = 'https://www.youtube.com/watch?v=dQw4w9WgXcQ' if r['instagramLink'] == None else r['instagramLink']
    telegram_button.url = 'https://www.youtube.com/watch?v=dQw4w9WgXcQ' if r['telegramLink'] == None else r['telegramLink']
    medium_button.url = 'https://www.youtube.com/watch?v=dQw4w9WgXcQ' if r['mediumLink'] == None else r['mediumLink']
    discord_button.url = 'https://www.youtube.com/watch?v=dQw4w9WgXcQ' if r['discordLink'] == None else r['discordLink']

    
    url = f'https://api.looksrare.org/api/v1/collections/stats?address={collection}'
    r = requests.get(url).json()['data']

    countOwners = f"`{r['countOwners']}`"
    totalSupply = f"`{r['totalSupply']} NFT`"
    floorPrice = '`no data`' if r['floorPrice'] == None else f"`{int(r['floorPrice']) * 10 ** -18 :.2f} ETH`"
    
    volume24h = '`no data`' if r['volume24h'] == None else f"`{int(r['volume24h']) * 10 ** -18 :.2f} ETH`"
    average24h = '`no data`' if r['average24h'] == None else f"`{float(r['average24h']) * 10 ** -18 :.2f} ETH`"
    count24h = '`no data`' if r['count24h'] == None else f"`{r['count24h']} NFT`"
    
    volume7d = '`no data`' if r['volume7d'] == None else f"`{int(r['volume7d']) * 10 ** -18 :.2f} ETH`"
    average7d = '`no data`' if r['average7d'] == None else f"`{float(r['average7d']) * 10 ** -18 :.2f} ETH`"
    count7d = '`no data`' if r['count7d'] == None else f"`{r['count7d']} NFT`"
    
    volume1m = '`no data`' if r['volume1m'] == None else f"`{int(r['volume1m']) * 10 ** -18 :.2f} ETH`"
    average1m = '`no data`' if r['average1m'] == None else f"`{float(r['average1m']) * 10 ** -18 :.2f} ETH`"
    count1m = '`no data`' if r['count1m'] == None else f"`{r['count1m']} NFT`"
    
    volumeAll = '`no data`' if r['volumeAll'] == None else f"`{int(r['volumeAll']) * 10 ** -18 :.2f} ETH`"
    averageAll = '`no data`' if r['averageAll'] == None else f"`{float(r['averageAll']) * 10 ** -18 :.2f} ETH`"
    countAll = '`no data`' if r['countAll'] == None else f"`{r['countAll']} NFT`"
    

    embed = discord.Embed(title='', color=0xFFA46E)
    embed.set_image(url=bannerURI)
    embed.add_field(name='Contract', value=address, inline=False)
    embed.add_field(name='Type', value=type, inline=True)
    embed.add_field(name='Verified', value=isVerified, inline=True)
    embed.add_field(name='Symbol', value=symbol, inline=True)
    embed.add_field(name='Owners', value=countOwners, inline=True)
    embed.add_field(name='Total Supply', value=totalSupply, inline=True)
    embed.add_field(name='Floor Price', value=floorPrice, inline=True)
    
    embed.add_field(name='1D Volume', value=volume24h, inline=True)
    embed.add_field(name='1D Avg', value=average24h, inline=True)
    embed.add_field(name='1D Sales', value=count24h, inline=True)
    
    embed.add_field(name='1W Volume', value=volume7d, inline=True)
    embed.add_field(name='1W Avg', value=average7d, inline=True)
    embed.add_field(name='1W Sales', value=count7d, inline=True)
    
    embed.add_field(name='1M Volume', value=volume1m, inline=True)
    embed.add_field(name='1M Avg', value=average1m, inline=True)
    embed.add_field(name='1M Sales', value=count1m, inline=True)

    embed.add_field(name='Total Volume', value=volumeAll, inline=True)
    embed.add_field(name='Total Avg', value=averageAll, inline=True)
    embed.add_field(name='Total Sales', value=countAll, inline=True)

    embed.set_author(name=f'{name}', url=f'https://looksrare.io/collection/{collection}', icon_url=logoURI)
    embed.set_footer(text='Data provided by Kizmeow NFT Bot', icon_url='https://user-images.githubusercontent.com/80938768/204983971-d7cf0e40-f4ce-4737-ba07-85ed62112dab.png')
    embed.timestamp = datetime.datetime.now()

    
    view = View(timeout=None)
    view.add_item(etherscan_button)
    view.add_item(site_button)
    view.add_item(facebook_button)
    view.add_item(twitter_button)
    view.add_item(instagram_button) 
    view.add_item(telegram_button) 
    view.add_item(medium_button) 
    view.add_item(discord_button) 

    return(embed, view)