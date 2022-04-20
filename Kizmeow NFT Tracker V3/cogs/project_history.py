import discord
from discord.commands import slash_command
from discord.ext import commands
from discord.commands import Option
import os
import json
import urllib.request as ur
from core.cog_core import cogcore

class project_history(commands.Cog):
    @slash_command(name='project_history',description='display project history information')
    async def project_history(
        self,
        ctx: discord.ApplicationContext,
        project_name: Option(str, 'collection slug at the end of OpenSea url')
    ):
        api0 = json.loads(ur.urlopen('https://api.opensea.io/api/v1/collection/'+project_name+'?format=json').read().decode())

        project_icon = api0['collection']['primary_asset_contracts'][0]['image_url']

        if api0['collection']['stats']['one_day_volume'] == None:
            one_day_volume = 'no data'
        else:
            one_day_volume = float(api0['collection']['stats']['one_day_volume'])#one_day_volume

        if api0['collection']['stats']['one_day_change'] == None:
            one_day_change = 'no data'
        else:
            one_day_change = float(api0['collection']['stats']['one_day_change'])

        if api0['collection']['stats']['one_day_sales'] == None:
            one_day_sales = 'no data'
        else:
            one_day_sales = float(api0['collection']['stats']['one_day_sales'])

        if api0['collection']['stats']['one_day_average_price'] == None:
            one_day_average_price = 'no data'
        else:
            one_day_average_price = float(api0['collection']['stats']['one_day_average_price'])

        if api0['collection']['stats']['seven_day_volume'] == None:
            seven_day_volume = 'no data'
        else:
            seven_day_volume = float(api0['collection']['stats']['seven_day_volume'])

        if api0['collection']['stats']['seven_day_change'] == None:
            seven_day_change = 'no data'
        else:
            seven_day_change = float(api0['collection']['stats']['seven_day_change'])

        if api0['collection']['stats']['seven_day_sales'] == None:
            seven_day_sales = 'no data'
        else:
            seven_day_sales = float(api0['collection']['stats']['seven_day_sales'])

        if api0['collection']['stats']['seven_day_average_price'] == None:
            seven_day_average_price = 'no data'
        else:
            seven_day_average_price = float(api0['collection']['stats']['seven_day_average_price'])

        if api0['collection']['stats']['thirty_day_volume'] == None:
            thirty_day_volume = 'no data'
        else:
            thirty_day_volume = float(api0['collection']['stats']['thirty_day_volume'])

        if api0['collection']['stats']['thirty_day_change'] == None:
            thirty_day_change = 'no data'
        else:
            thirty_day_change = float(api0['collection']['stats']['thirty_day_change'])

        if api0['collection']['stats']['thirty_day_sales'] == None:
            thirty_day_sales = 'no data'
        else:
            thirty_day_sales = float(api0['collection']['stats']['thirty_day_sales'])

        if api0['collection']['stats']['thirty_day_average_price'] == None:
            thirty_day_average_price = 'no data'
        else:
            thirty_day_average_price = float(api0['collection']['stats']['thirty_day_average_price'])

        if(one_day_volume != 0):
            embed=discord.Embed(title='**[project realtime]**', color=0xFFA46E)
            embed.set_thumbnail(url=project_icon)
            embed.add_field(name='1 day total trade volume' , value=f'{one_day_volume:.2f} ETH', inline=False) 
            embed.add_field(name='1 day total trade volume change' , value=f'{one_day_change:.2f} ETH', inline=False) 
            embed.add_field(name='1 day sales quantity' , value=f'{one_day_sales:.2f} NFT', inline=False)
            embed.add_field(name='1 day average price' , value=f'{one_day_average_price:.2f} ETH', inline=False) 
            embed.add_field(name='7 days total trade volume' , value=f'{seven_day_volume:.2f} ETH', inline=False) 
            embed.add_field(name='7 day total trade volume change' , value=f'{seven_day_change:.2f} ETH', inline=False) 
            embed.add_field(name='7 day sales quantity' , value=f'{seven_day_sales:.2f} NFT', inline=False)
            embed.add_field(name='7 day average price' , value=f'{seven_day_average_price:.2f} ETH', inline=False) 
            embed.add_field(name='30 day total trade volume' , value=f'{thirty_day_volume:.2f} ETH', inline=False)
            embed.add_field(name='30 day total trade volume change' , value=f'{thirty_day_change:.2f} ETH', inline=False)
            embed.add_field(name='30 day sales quantity' , value=f'{thirty_day_sales:.2f} NFT', inline=False)
            embed.add_field(name='30 day average price' , value=f'{thirty_day_average_price:.2f} ETH', inline=False) 
            
            await ctx.respond(embed=embed)
        else:
            embed=discord.Embed(title='**[ERROR] cannot fetch data because the collection is too new**', color=0xFFA46E)
            await ctx.respond(embed=embed)
def setup(bot):
    bot.add_cog(project_history(bot))