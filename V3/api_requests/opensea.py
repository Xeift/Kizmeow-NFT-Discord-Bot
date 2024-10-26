import requests
import datetime
import discord
from discord.ui import View
from buttons.buttons import etherscan_button, twitter_button, discord_button, site_button, return_button

async def opensea_embed(collection):

    url = f'https://api.opensea.io/api/v1/collection/{collection}'
    r = requests.get(url).json()['collection']

    primary_asset_contracts = f"`{r['primary_asset_contracts'][0]['address']}`"
    image_url = r['image_url']
    created_date = f"<t:{int(datetime.datetime.fromisoformat(r['created_date']).timestamp())}:R>"
    dev_seller_fee_basis_points = f"`{str(int(r['dev_seller_fee_basis_points']) / 100)}%`"
    
    discord_button.url = 'https://www.youtube.com/watch?v=dQw4w9WgXcQ' if r['discord_url'] == None else r['discord_url']
    twitter_button.url = 'https://www.youtube.com/watch?v=dQw4w9WgXcQ' if f"https://twitter.com/{r['twitter_username']}" == None else f"https://twitter.com/{r['twitter_username']}"
    site_button.url = 'https://www.youtube.com/watch?v=dQw4w9WgXcQ' if r['external_url'] == None else r['external_url']
    etherscan_button.url = 'https://www.youtube.com/watch?v=dQw4w9WgXcQ' if f'https://etherscan.io/address/{primary_asset_contracts}' == None else f'https://etherscan.io/address/{primary_asset_contracts}'
    
    safelist_request_status = f"`{r['safelist_request_status']}`"
    name = r['name']
    banner_image_url = f'https://open-graph.opensea.io/v1/collections/{collection}'

    one_hour_volume = f"`{r['stats']['one_hour_volume']:.2f} ETH`"
    one_hour_sales = f"`{r['stats']['one_hour_sales']} NFT`"
    one_hour_average_price = f"`{r['stats']['one_hour_average_price']:.2f} ETH`"

    one_day_volume = f"`{r['stats']['one_day_volume']:.2f} ETH`"
    one_day_sales = f"`{r['stats']['one_day_sales']} NFT`"
    one_day_average_price = f"`{r['stats']['one_day_average_price']:.2f} ETH`"

    seven_day_volume = f"`{r['stats']['seven_day_volume']:.2f} ETH`"
    seven_day_sales = f"`{r['stats']['seven_day_sales']} NFT`"
    seven_day_average_price = f"`{r['stats']['seven_day_average_price']:.2f} ETH`"

    thirty_day_volume = f"`{r['stats']['thirty_day_volume']:.2f} ETH`"
    thirty_day_sales = f"`{r['stats']['thirty_day_sales']} NFT`"
    thirty_day_average_price = f"`{r['stats']['thirty_day_average_price']:.2f} ETH`"

    total_volume = f"`{r['stats']['total_volume']:.2f} ETH`"
    total_sales = f"`{r['stats']['total_sales']} NFT`"
    total_average_price = f"`{r['stats']['average_price']:.2f} ETH`"

    total_supply = f"`{r['stats']['total_supply']} NFT`"
    num_owners = f"`{r['stats']['num_owners']}`"
    floor_price = '`no data`' if r['stats']['floor_price'] == None else f"`{r['stats']['floor_price']:.2f}`"
    

    embed = discord.Embed(title='', color=0xFFA46E)
    embed.set_image(url=banner_image_url)
    embed.add_field(name='Contract', value=primary_asset_contracts, inline=False)
    embed.add_field(name='Created', value=created_date, inline=True)
    embed.add_field(name='Verified', value=safelist_request_status, inline=True)
    embed.add_field(name='Creator Earnings', value=dev_seller_fee_basis_points, inline=True)
    embed.add_field(name='Floor Price', value=floor_price, inline=True)
    embed.add_field(name='Owners', value=num_owners, inline=True)
    embed.add_field(name='Total Supply', value=total_supply, inline=True)

    embed.add_field(name='1H Volume', value=one_hour_volume, inline=True)
    embed.add_field(name='1H Sales', value=one_hour_sales, inline=True)
    embed.add_field(name='1H Avg Price', value=one_hour_average_price, inline=True)
    
    embed.add_field(name='1D Volume', value=one_day_volume, inline=True)
    embed.add_field(name='1D Sales', value=one_day_sales, inline=True)
    embed.add_field(name='1D Avg Price', value=one_day_average_price, inline=True)
    
    embed.add_field(name='7D Volume', value=seven_day_volume, inline=True)
    embed.add_field(name='7D Sales', value=seven_day_sales, inline=True)
    embed.add_field(name='7D Avg Price', value=seven_day_average_price, inline=True)

    embed.add_field(name='30D Volume', value=thirty_day_volume, inline=True)
    embed.add_field(name='30D Sales', value=thirty_day_sales, inline=True)
    embed.add_field(name='30D Avg Price', value=thirty_day_average_price, inline=True)

    embed.add_field(name='Total Volume', value=total_volume, inline=True)
    embed.add_field(name='Total Sales', value=total_sales, inline=True)
    embed.add_field(name='Total Average Price', value=total_average_price, inline=True)

    embed.set_author(name=f'{name}', url=f'https://opensea.io/collection/{collection}', icon_url=image_url)
    embed.set_footer(text='Data provided by Kizmeow NFT Bot', icon_url='https://user-images.githubusercontent.com/80938768/204983971-d7cf0e40-f4ce-4737-ba07-85ed62112dab.png')
    embed.timestamp = datetime.datetime.now()

    
    view = View(timeout=None)
    view.add_item(etherscan_button)
    view.add_item(twitter_button)
    view.add_item(discord_button)
    view.add_item(site_button)
    view.add_item(return_button)

    return(embed, view)