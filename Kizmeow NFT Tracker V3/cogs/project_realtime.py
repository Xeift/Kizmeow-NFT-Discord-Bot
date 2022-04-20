import discord
from discord.commands import slash_command
from discord.ext import commands
from discord.commands import Option
import os
import json
import urllib.request as ur
from core.cog_core import cogcore

class project_realtime(commands.Cog):
    @slash_command(name='project_realtime',description='display project realtime information')
    async def project_realtime(
        self,
        ctx: discord.ApplicationContext,
        project_name: Option(str, 'collection slug at the end of OpenSea url')
    ):
        api0 = json.loads(ur.urlopen('https://api.opensea.io/api/v1/collection/'+project_name+'?format=json').read().decode())

        project_icon = api0['collection']['primary_asset_contracts'][0]['image_url']

        if api0['collection']['stats']['floor_price'] == None:
            floor_price = 'no data'
        else:
            floor_price = float(api0['collection']['stats']['floor_price'])

        if api0['collection']['stats']['total_volume'] == None:
            total_volume = 'no data'
        else:
            total_volume = float(api0['collection']['stats']['total_volume'])

        if api0['collection']['stats']['total_sales'] == None:
            total_sales = 'no data'
        else:
            total_sales = float(api0['collection']['stats']['total_sales'])

        if api0['collection']['stats']['total_supply'] == None:
            total_supply = 'no data'
        else:
            total_supply = float(api0['collection']['stats']['total_supply'])

        if api0['collection']['stats']['num_owners'] == None:
            num_owners = 'no data'
        else:
            num_owners = float(api0['collection']['stats']['num_owners'])

        if api0['collection']['stats']['average_price'] == None:
            average_price = 'no data'
        else:
            average_price = float(api0['collection']['stats']['average_price'])

        if api0['collection']['stats']['num_reports'] == None:
            num_reports = 'no data'
        else:
            num_reports = float(api0['collection']['stats']['num_reports'])

        if api0['collection']['stats']['market_cap'] == None:
            market_cap = 'no data'
        else:
            market_cap = float(api0['collection']['stats']['market_cap'])

        if(total_volume != 0):
            embed=discord.Embed(title='**[project realtime]**', color=0xFFA46E)
            embed.set_thumbnail(url=project_icon)
            embed.add_field(name='total supply' , value=f'{total_supply:.2f}  NFT', inline=False) 
            embed.add_field(name='holders' , value=f'{num_owners:.2f}', inline=False)     
            embed.add_field(name='floor price' , value=f'{floor_price:.2f} ETH', inline=False) 
            embed.add_field(name='total volume' , value=f'{total_volume:.2f} ETH', inline=False) 
            embed.add_field(name='total sales' , value=f'{total_sales:.2f}  NFT', inline=False)
            embed.add_field(name='average price' , value=f'{average_price:.2f} ETH', inline=False) 
            embed.add_field(name='reports' , value=f'{num_reports:.2f} times', inline=False) 
            embed.add_field(name='market cap' , value=f'{market_cap:.2f} ETH', inline=False) 
            
            await ctx.respond(embed=embed)
        else:
            embed=discord.Embed(title='**[ERROR] cannot fetch data because the collection is too new**', color=0xFFA46E)
            await ctx.respond(embed=embed)
def setup(bot):
    bot.add_cog(project_realtime(bot))