import discord
import os
from discord.ext import commands
import json
import keep_alive
import requests
import time

discord_token = os.environ['discord_token']
osapikey = os.environ['osapikey']

bot = commands.Bot(
	command_prefix="k!", #  bot prefix
	case_insensitive=True, #  case-sensitive
  intents=discord.Intents.all(), #  特權網關意圖(接收特殊事件)
  help_command=None #  禁用預設help指令
)

@bot.event
async def on_ready():
  print("Ready!")
  while True:
    ################################################################################# event_list
    l_url = "https://api.opensea.io/api/v1/events?asset_contract_address=0xa6916545a56f75acd43fb6a1527a73a41d2b4081&event_type=created&only_opensea=false&offset=0&limit=1"
    l_headers = {
        "Accept": "application/json",
        "X-API-KEY": osapikey
    }
    l_response = requests.request("GET", l_url, headers=l_headers)
    l_data = json.loads(l_response.text)

    l_name = l_data['asset_events'][0]['asset']['name']
    #price
    l_starting_price = int(l_data['asset_events'][0]['starting_price'])/1000000000000000000
    #seller address
    l_seller_address = l_data['asset_events'][0]['from_account']['address']
    #os link
    l_permalink = l_data['asset_events'][0]['asset']['permalink']
    #image
    l_image_url = l_data['asset_events'][0]['asset']['image_url']

    file = open("temp.json", "r")
    p = json.load(file)
    listed = p['listed']
    file.close()
    #################################################################################

    ################################################################################# event_sold
    s_url = "https://api.opensea.io/api/v1/events?asset_contract_address=0xa6916545a56f75acd43fb6a1527a73a41d2b4081&event_type=successful&only_opensea=false&offset=0&limit=1"

    s_headers = {
        "Accept": "application/json",
        "X-API-KEY": osapikey
    }
    s_response = requests.request("GET", s_url, headers=s_headers)
    s_data = json.loads(s_response.text)

    #NFT name
    s_name = s_data['asset_events'][0]['asset']['name']
    #price
    s_starting_price = int(s_data['asset_events'][0]['total_price'])/1000000000000000000
    #seller address
    s_seller_address = s_data['asset_events'][0]['seller']['address']
    #buyer address
    s_buyer_address = s_data['asset_events'][0]['winner_account']['address']
    #os link
    s_permalink = s_data['asset_events'][0]['asset']['permalink']
    #image
    s_image_url = s_data['asset_events'][0]['asset']['image_url'] 
    
    file = open("temp.json", "r")
    p = json.load(file)
    sold = p['sold']
    file.close()

    if listed != l_name:
      jsonObject = {
          "listed": l_name,
          "sold": s_name,
      }
      file = open("temp.json", "w")
      json.dump(jsonObject, file)
      file.close()

      channel=bot.get_channel(931398747966042172)
      embed=discord.Embed(title=" ", description=" ", color=0xe8006f)
      embed.set_author(name=F"[list] {l_name}")
      embed.set_image(url=l_image_url)
      embed.add_field(name="price", value=f"{l_starting_price} ETH", inline=False) 
      embed.add_field(name="seller", value=f"{l_seller_address}", inline=False) 
      embed.add_field(name="OpenSea", value=f"{l_permalink}", inline=False) 
      await channel.send(embed=embed)
    time.sleep(5)

    if sold != s_name:
      jsonObject = {
          "listed": l_name,
          "sold": s_name,
      }
      file = open("temp.json", "w")
      json.dump(jsonObject, file)
      file.close()

      channel=bot.get_channel(931398747966042172)
      embed=discord.Embed(title=" ", description=" ", color=0x00ff00)
      embed.set_author(name=F"[sold] {s_name}")
      embed.set_image(url=s_image_url)
      embed.add_field(name="price", value=f"{s_starting_price} ETH", inline=False) 
      embed.add_field(name="seller", value=f"{s_seller_address}", inline=False) 
      embed.add_field(name="buyer", value=f"{s_buyer_address}", inline=False) 
      embed.add_field(name="OpenSea", value=f"{s_permalink}", inline=False) 
      await channel.send(embed=embed)
    time.sleep(5) 
    #################################################################################
keep_alive.keep_alive()
discord_token = os.environ['discord_token']
bot.run(discord_token)