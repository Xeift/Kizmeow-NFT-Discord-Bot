import discord
from discord_slash.utils.manage_commands import create_option
import urllib.request as ur
import json
from discord_slash import cog_ext
from core.cog_core import cogcore

class nft(cogcore):
  @cog_ext.cog_slash(name="nft",
  description="return some useful information about your NFT from the contract address and token id you entered",
  options=
  [
    create_option
    (
      name="contract_address",
      description="enter the contract address of yor NFT",
      option_type=3,
      required=True
    ),
    create_option
    (
      name="token_id",
      description="enter the token id of your NFT",
      option_type=3,
      required=True
    )
  ],
  )

  async def nft(self,ctx,contract_address,token_id):
    url1='https://api.opensea.io/api/v1/asset/'+contract_address+'/'+token_id+'/?format=json' #api url
    site1 = ur.urlopen(url1)
    page1 = site1.read()
    contents1 = page1.decode()
    data1 = json.loads(contents1)

    if data1['name'] == None:
      name = "no data"
    else:
      name = str(data1['name'])
      

    if data1['image_original_url'] == None:
      image_original_url = "no data"
    else:
      image_original_url = str(data1['image_original_url'])


    if data1['top_ownerships'][0]['owner']['user'] == None:
      top_ownerships = "no data"
    else:
      top_ownerships = str(data1['top_ownerships'][0]['owner']['user']['username'])


    if data1['description'] == None:
      description = "no data"
    else:
      description = str(data1['description'])


    if data1['collection']['primary_asset_contracts'][0]['external_link'] == None:
      external_link = "no data"
    else:
      external_link = str(data1['collection']['primary_asset_contracts'][0]['external_link'])


    if data1['collection']['primary_asset_contracts'][0]['schema_name'] == None:
      schema_name = "no data"
    else:
      schema_name = str(data1['collection']['primary_asset_contracts'][0]['schema_name'])


    if data1['token_id'] == None:
      token_id1 = "no data"
    else:
      token_id1 = str(data1['token_id'])


    if data1['permalink'] == None:
      permalink = "no data"
    else:
      permalink = str(data1['permalink'])


    embed=discord.Embed(title="["+name+"]", color=0xe8006f)
    embed.set_thumbnail(url=image_original_url)
    embed.add_field(name="token id" , value=token_id1, inline=False) 
    embed.add_field(name="description" , value=description, inline=False)     
    embed.add_field(name="official website" , value=external_link, inline=False) 
    embed.add_field(name="token type" , value=schema_name, inline=False) 
    embed.add_field(name="owner" , value=top_ownerships, inline=False)
    embed.add_field(name="OpenSea" , value=permalink, inline=False)
    embed.add_field(name="original resolution image" , value=image_original_url, inline=False)

    await ctx.send(embed=embed)

def setup(bot):
  bot.add_cog(nft(bot))
