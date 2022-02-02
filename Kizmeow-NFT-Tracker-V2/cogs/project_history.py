import discord
from discord_slash.utils.manage_commands import create_option
import urllib.request as ur
import json
from discord_slash import cog_ext
from core.cog_core import cogcore

class project_history(cogcore):
  @cog_ext.cog_slash(name="project_history",
  description="return some useful history information from the project name you entered from OpenSea API",
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

  async def project_history(self,ctx,project_name):
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

    if data1['stats']['one_day_volume'] == None:
      one_day_volume = "no data"
    else:
      one_day_volume = str(round(data1['stats']['one_day_volume'],3))#one_day_volume

    if data1['stats']['one_day_change'] == None:
      one_day_change = "no data"
    else:
      one_day_change = str(round(data1['stats']['one_day_change'],3))

    if data1['stats']['one_day_sales'] == None:
      one_day_sales = "no data"
    else:
      one_day_sales = str(round(data1['stats']['one_day_sales'],3))

    if data1['stats']['one_day_average_price'] == None:
      one_day_average_price = "no data"
    else:
      one_day_average_price = str(round(data1['stats']['one_day_average_price'],3))

    if data1['stats']['seven_day_volume'] == None:
      seven_day_volume = "no data"
    else:
      seven_day_volume = str(round(data1['stats']['seven_day_volume'],3))

    if data1['stats']['seven_day_change'] == None:
      seven_day_change = "no data"
    else:
      seven_day_change = str(round(data1['stats']['seven_day_change'],3))

    if data1['stats']['seven_day_sales'] == None:
      seven_day_sales = "no data"
    else:
      seven_day_sales = str(round(data1['stats']['seven_day_sales'],3))

    if data1['stats']['seven_day_average_price'] == None:
      seven_day_average_price = "no data"
    else:
      seven_day_average_price = str(round(data1['stats']['seven_day_average_price'],3))

    if data1['stats']['thirty_day_volume'] == None:
      thirty_day_volume = "no data"
    else:
      thirty_day_volume = str(round(data1['stats']['thirty_day_volume'],3))

    if data1['stats']['thirty_day_change'] == None:
      thirty_day_change = "no data"
    else:
      thirty_day_change = str(round(data1['stats']['thirty_day_change'],3))

    if data1['stats']['thirty_day_sales'] == None:
      thirty_day_sales = "no data"
    else:
      thirty_day_sales = str(round(data1['stats']['thirty_day_sales'],3))

    if data1['stats']['thirty_day_average_price'] == None:
      thirty_day_average_price = "no data"
    else:
      thirty_day_average_price = str(round(data1['stats']['thirty_day_average_price'],3))

    if(one_day_volume != 0):
      embed=discord.Embed(title="["+project_name+" history volume]", color=0xe8006f)
      embed.set_thumbnail(url=img0)
      embed.add_field(name="1 day total trade volume" , value=one_day_volume+" ETH", inline=False) 
      embed.add_field(name="1 day total trade volume change" , value=one_day_change+" ETH", inline=False) 
      embed.add_field(name="1 day sales quantity" , value=one_day_sales+" NFT", inline=False)
      embed.add_field(name="1 day average price" , value=one_day_average_price+"ETH\n ㅤ", inline=False) 
      embed.add_field(name="7 days total trade volume" , value=seven_day_volume+" ETH", inline=False) 
      embed.add_field(name="7 day total trade volume change" , value=seven_day_change+" ETH", inline=False) 
      embed.add_field(name="7 day sales quantity" , value=seven_day_sales+" NFT", inline=False)
      embed.add_field(name="7 day average price" , value=seven_day_average_price+" ETH\n ㅤ", inline=False) 
      embed.add_field(name="30 day total trade volume" , value=thirty_day_volume+" ETH", inline=False)
      embed.add_field(name="30 day total trade volume change" , value=thirty_day_change+" ETH", inline=False)
      embed.add_field(name="30 day sales quantity" , value=thirty_day_sales+" NFT", inline=False)
      embed.add_field(name="30 day average price" , value=thirty_day_average_price+" ETH", inline=False)        
      await ctx.send(embed=embed)
    else:
        await ctx.send("error")

def setup(bot):
  bot.add_cog(project_history(bot))
