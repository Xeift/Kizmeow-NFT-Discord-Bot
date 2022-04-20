import discord
from discord_slash.utils.manage_commands import create_option
import urllib.request as ur
import json
from discord_slash import cog_ext
from core.cog_core import cogcore

class project_realtime(cogcore):
  @cog_ext.cog_slash(name="project_realtime",
  description="return some useful realtime information from the project name you entered from OpenSea API",
  options=
  [
    create_option
    (
      name="project_name",
      description="enter the project name which is at the end of OpenSea url",
      option_type=3,
      required=True
    )
  ]
  )

  async def project_realtime(self,ctx,project_name):
    url0='https://api.opensea.io/api/v1/collection/'+project_name+'?format=json' #api url
    site0 = ur.urlopen(url0)
    page0 = site0.read()
    contents0 = page0.decode()
    data0 = json.loads(contents0)
    img0 = data0['collection']['primary_asset_contracts'][0]['image_url']

    url1='https://api.opensea.io/api/v1/collection/'+project_name+'/stats?format=json' #api url
    site1 = ur.urlopen(url1)
    page1 = site1.read()
    contents1 = page1.decode()
    data1 = json.loads(contents1)

    if data1['stats']['floor_price'] == None:
      floor_price = "no data"
    else:
      floor_price = str(float(round(data1['stats']['floor_price'],3)))


    if data1['stats']['total_volume'] == None:
      total_volume = "no data"
    else:
      total_volume = str(float(round(data1['stats']['total_volume'],3)))


    if data1['stats']['total_sales'] == None:
      total_sales = "no data"
    else:
      total_sales = str(float(round(data1['stats']['total_sales'],3)))

    if data1['stats']['total_supply'] == None:
      total_supply = "no data"
    else:
      total_supply = str(float(round(data1['stats']['total_supply'],3)))

    if data1['stats']['num_owners'] == None:
      num_owners = "no data"
    else:
      num_owners = str(float(round(data1['stats']['num_owners'],3)))

    if data1['stats']['average_price'] == None:
      average_price = "no data"
    else:
      average_price = str(float(round(data1['stats']['average_price'],3)))

    if data1['stats']['num_reports'] == None:
      num_reports = "no data"
    else:
      num_reports = str(float(round(data1['stats']['num_reports'],3)))

    if data1['stats']['market_cap'] == None:
      market_cap = "no data"
    else:
      market_cap = str(float(round(data1['stats']['market_cap'],3)))

    if(total_volume != 0):
      embed=discord.Embed(title="["+project_name+" realtime information]", color=0xe8006f)
      embed.set_thumbnail(url=img0)
      embed.add_field(name="total supply" , value=total_supply+"  NFT", inline=False) 
      embed.add_field(name="holders" , value=num_owners, inline=False)     
      embed.add_field(name="floor price" , value=floor_price+" ETH", inline=False) 
      embed.add_field(name="total volume" , value=total_volume+" ETH", inline=False) 
      embed.add_field(name="total sales" , value=total_sales+"  NFT", inline=False)
      embed.add_field(name="average price" , value=average_price+"ETH", inline=False) 
      embed.add_field(name="reports" , value=num_reports+" times", inline=False) 
      embed.add_field(name="market cap" , value=market_cap+" ETH", inline=False) 
      
      await ctx.send(embed=embed)
    else:
        await ctx.send("error")
def setup(bot):
  bot.add_cog(project_realtime(bot))
