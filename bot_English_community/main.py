import discord
from discord.ext import commands
from discord_slash import SlashCommand
from discord_slash.utils.manage_commands import create_option
import urllib.request as ur
import urllib.parse
from urllib.error import HTTPError
from datetime import datetime, timezone, timedelta
import json
import qrcode
import asyncio 
import os
import requests
import keep_alive

discord_token = os.environ['discord_token']
etherscan_api_key = os.environ['etherscan_api_key']
#opensea_api_key = os.environ['opensea_api_key']

bot = commands.Bot(command_prefix="k!",
intents=discord.Intents.all(),
help_command=None)
slash = SlashCommand(bot, sync_commands=True) 

@bot.event
async def on_ready():
  print("Ready!")
  while True:
    url1='https://api.etherscan.io/api?module=stats&action=ethprice&apikey='+etherscan_api_key #api url

    site1 = ur.urlopen(url1)
    page1 = site1.read()
    contents1 = page1.decode()
    data1 = json.loads(contents1)

    ethusd = data1['result']['ethusd']
    #####
    url2='https://api.etherscan.io/api?module=gastracker&action=gasoracle&apikey='+etherscan_api_key #api url

    site2 = ur.urlopen(url2)
    page2 = site2.read()
    contents2 = page2.decode()
    data2 = json.loads(contents2)

    SafeGasPrice = data2['result']['SafeGasPrice']
    ProposeGasPrice = data2['result']['ProposeGasPrice']
    FastGasPrice = data2['result']['FastGasPrice']

    presence_ctx1 = 'Ξ '+ethusd
    presence_ctx2 = '🚀'+FastGasPrice+'🚗'+ProposeGasPrice+'🚲'+SafeGasPrice

    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=presence_ctx1))
    await asyncio.sleep(10)
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=presence_ctx2))
    await asyncio.sleep(10)
################################################################################help
@slash.slash(name="help",description="display help message")
async def help(ctx):
  BUTTONS = ["◀️","0️⃣","1️⃣","2️⃣","3️⃣","4️⃣"]
  embed=discord.Embed(title="**/help**", description="command list\npress the emoji to select page ", color=0xe8006f)

  embed.add_field(name="[back]", value="◀️", inline=True)
  embed.add_field(name="[bot information]", value="0️⃣", inline=True)
  embed.add_field(name="ㅤ", value="ㅤ", inline=True)#弄一行空白 單純排版用
  embed.add_field(name="[system]", value="1️⃣", inline=True)
  embed.add_field(name="[NFT]", value="2️⃣", inline=True)
  embed.add_field(name="[3(in development)]", value="3️⃣", inline=True)
  embed.add_field(name="[4(in development)]", value="4️⃣", inline=True)
  embed.add_field(name="options", value="some commands must input option(s)\ne.g. /demi-nft token_id: 824 \n`824`is the option of this command.If there are more than 2 options, after entered the first one, you can press `tab` on the keyboard to switch to the next option.", inline=False)
  embed.set_footer(text="last update:\n2021.12.17 4:01 p.m.")
  msg = await ctx.send(embed=embed)
  embed0=discord.Embed(title="**[bot information]**", description="information about this bot", color=0xe8006f)
  embed0.add_field(name="bot name", value="Kizmeow", inline=False)
  embed0.add_field(name="developer", value="Xeift", inline=False)
  embed0.add_field(name="bot avatar illustrator", value="Kiyue", inline=False)
  embed0.add_field(name="programming language", value="Python", inline=False)
  embed0.add_field(name="GitHub", value="https://github.com/Xeift/Kizmeow-OpenSea-and-Etherscan-Discord-Bot", inline=False)
  embed0.add_field(name="contact information", value="Xeift: Xeift#1230\nKiyue: https://www.facebook.com/profile.php?id=100026170072950", inline=False)
  embed0.add_field(name="note", value="transaction record function calls Etherscan API, OpenSea related functions calls OpenSea API.", inline=False)

  embed1=discord.Embed(title="**[system]**", description="system commands", color=0xe8006f)
  embed1.add_field(name="/help", value="display help message.", inline=False)
  embed1.add_field(name="/invite", value="get bot invite link, invite bot to your server. `admin permission is required in the server you invite to`", inline=False)
  embed1.add_field(name="/ping", value="return bot latency.", inline=False)

  embed2=discord.Embed(title="**[NFT]**", description="search information of NFT project.", color=0xe8006f)
  embed2.add_field(name="/project", value="display real-time price of specific project. option:`project_name`", inline=False)
  embed2.add_field(name="/project-history", value="display history price of specific project. option:`project_name`", inline=False)
  embed2.add_field(name="/nft", value="search the NFT of a specific item and a specific number. option:`contract_address` `token_id`", inline=False)
  embed2.add_field(name="/txn", value="enter the address and display the transaction record. option: `eth_address`", inline=False)
  embed2.add_field(name="/account_info", value="enter the address to display ETH balance and Demi NFT balance. option: `eth_address`", inline=False)

  embed3=discord.Embed(title="**[3]**", description="3", color=0xe8006f)
  embed3.add_field(name="3", value="3", inline=False)

  embed4=discord.Embed(title="**[4]**", description="4", color=0xe8006f)
  embed4.add_field(name="4", value="4", inline=False)

  for b in BUTTONS:
    await msg.add_reaction(b)
  
  while True:
    try:
      react, user = await bot.wait_for("reaction_add", timeout=60.0, check=lambda r, u: r.message.id == msg.id and u.id == ctx.author.id and r.emoji in BUTTONS)
      await msg.remove_reaction(react.emoji, user) #user按了以後馬上清掉reaction
    
    except asyncio.TimeoutError:
      pass

    else:
      if react.emoji == BUTTONS[0]:
        await msg.edit(embed=embed)
      if react.emoji == BUTTONS[1]:
        await msg.edit(embed=embed0)
      elif react.emoji == BUTTONS[2]:
        await msg.edit(embed=embed1)
      elif react.emoji == BUTTONS[3]:
        await msg.edit(embed=embed2)
      elif react.emoji == BUTTONS[4]:
        await msg.edit(embed=embed3)
      elif react.emoji == BUTTONS[5]:
        await msg.edit(embed=embed4)

################################################################################ping
@slash.slash(name="ping",description="return bot latency")
async def _ping(ctx):
  await ctx.send(f"pong! ({bot.latency*1000} ms)")
################################################################################invite
@slash.slash(name="invite",description="invite bot to your server")
async def invite(ctx):
  embed=discord.Embed(title="**[bot invite link]**", description="https://discord.com/api/oauth2/authorize?client_id=886198731328868402&permissions=534727097920&scope=bot%20applications.commands", color=0xe8006f)
  await ctx.send(embed = embed)
################################################################################balance
@slash.slash(
name="account_info",
description="get the account info from the ETH address you enter",
options=
[
  create_option
  (
    name="eth_address",
    description="enter wallet address",
    option_type=3,
    required=True
  )
]
)

async def account_info(ctx, eth_address: str):
# await ctx.send(content=f"{eth_address}")
  url1='https://api.etherscan.io/api?module=account&action=balance&address='+eth_address+'&tag=latest&apikey='+etherscan_api_key #api url

  url2='https://api.etherscan.io/api?module=account&action=tokenbalance&contractaddress=0xa6916545a56f75acd43fb6a1527a73a41d2b4081&address='+eth_address+'&tag=latest&apikey='+etherscan_api_key

  site1 = ur.urlopen(url1)
  page1 = site1.read()
  contents1 = page1.decode()
  data1 = json.loads(contents1)

  bal_ori = data1['result']#eth balance
  eth_bal = int(bal_ori)/1000000000000000000

  site2 = ur.urlopen(url2)
  page2 = site2.read()
  contents2 = page2.decode()
  data2 = json.loads(contents2)

  demi_balance = data2['result']

  if(eth_bal != 0):
    embed=discord.Embed(title="[balance]", color=0xe8006f)
    embed.set_thumbnail(url="https://cdn.jsdelivr.net/gh/Xeift/image-hosting@main//a8eb74eaa4d1148c2b33db119edb9515.gif")
    embed.add_field(name="ETH balance" , value=str(eth_bal)[0:7]+"||"+str(eth_bal)[7:20]+"||"+" ETH", inline=False)
    await ctx.send(embed=embed)
  else:
      await ctx.send("no ETH in this address or you've entered the wrong address")
################################################################################transaction history
@slash.slash(
name="txn",
description="get the transaction history from the ETH address you enter",
options=
[
  create_option
  (
    name="eth_address",
    description="enter wallet address",
    option_type=3,
    required=True
  )
]
)

async def txn(ctx, eth_address: str):
  BUTTONS = ["◀️","▶️"]
  url1='https://api.etherscan.io/api?module=account&action=txlist&address='+eth_address+'&startblock=0&endblock=99999999&page=1&offset=10&sort=dsc&apikey='+etherscan_api_key #api url

  site1 = ur.urlopen(url1)
  page1 = site1.read()
  contents1 = page1.decode()
  data1 = json.loads(contents1)

  index = 9
  blockNumber = data1['result'][index]['blockNumber']
  timeStamp = data1['result'][index]['timeStamp']
  hash = data1['result'][index]['hash']
  nonce = data1['result'][index]['nonce']
  blockHash = data1['result'][index]['blockHash']
  transactionIndex = data1['result'][index]['transactionIndex']
  from1 = data1['result'][index]['from']
  to = data1['result'][index]['to']
  value1 = data1['result'][index]['value']
  gas = data1['result'][index]['gas']
  gasPrice = data1['result'][index]['gasPrice']
  isError = data1['result'][index]['isError']
  txreceipt_status = data1['result'][index]['txreceipt_status']
  input1 = data1['result'][index]['input']
  contractAddress = data1['result'][index]['contractAddress']
  if contractAddress == "":
    contractAddress = "empty"
  cumulativeGasUsed = data1['result'][index]['cumulativeGasUsed']
  gasUsed = data1['result'][index]['gasUsed']
  confirmations = data1['result'][index]['confirmations']

  icount = 10#index count

  embed=discord.Embed(title="[transaction history]", color=0xe8006f)
  embed.set_thumbnail(url="https://cdn.jsdelivr.net/gh/Xeift/image-hosting@main//a8eb74eaa4d1148c2b33db119edb9515.gif")
  embed.add_field(name="blockNumber" , value=f"{blockNumber}", inline=False)
  embed.add_field(name="timeStamp" , value=f"{timeStamp}", inline=False)
  embed.add_field(name="hash" , value=f"{hash}", inline=False)
  embed.add_field(name="nonce" , value=f"{nonce}", inline=False)
  embed.add_field(name="blockHash" , value=f"{blockHash}", inline=False)
  embed.add_field(name="transactionIndex" , value=f"{transactionIndex}", inline=False)
  embed.add_field(name="from" , value=f"{from1}", inline=False)
  embed.add_field(name="to" , value=f"{to}", inline=False)
  embed.add_field(name="value" , value=f"{value1}", inline=False)
  embed.add_field(name="gas" , value=f"{gas}", inline=False)
  embed.add_field(name="gasPrice" , value=f"{gasPrice}", inline=False)
  embed.add_field(name="isError" , value=f"{isError}", inline=False)
  embed.add_field(name="txreceipt_status" , value=f"{txreceipt_status}", inline=False)
  embed.add_field(name="input" , value=f"{input1}", inline=False)
  embed.add_field(name="contractAddress" , value=f"{contractAddress}", inline=False)
  embed.add_field(name="cumulativeGasUsed" , value=f"{cumulativeGasUsed}", inline=False)
  embed.add_field(name="gasUsed" , value=f"{gasUsed}", inline=False)
  embed.add_field(name="confirmations" , value=f"{confirmations}", inline=False)

  progresse = "◇" * icount 
  replacement = "◆"
  progresse2 = progresse[:9-index] + replacement + progresse[-index:]
  embed.add_field(name=f"{progresse2}" , value=f"page: {10-index}/{icount}", inline=False)
  msg = await ctx.send(embed=embed)

  for b in BUTTONS:
    await msg.add_reaction(b)

  while True:
    try:
      react, user = await bot.wait_for("reaction_add", timeout=60.0, check=lambda r, u: r.message.id == msg.id and u.id == ctx.author.id and r.emoji in BUTTONS)
      await msg.remove_reaction(react.emoji, user) #clear reaction when user add reaction
    
    except asyncio.TimeoutError:
      pass

    else:
      if react.emoji == BUTTONS[0] and index < 9: 
        index += 1#
      elif react.emoji == BUTTONS[1] and index > 1: 
        index -= 1

      blockNumber = data1['result'][index]['blockNumber']
      timeStamp = data1['result'][index]['timeStamp']
      hash = data1['result'][index]['hash']
      nonce = data1['result'][index]['nonce']
      blockHash = data1['result'][index]['blockHash']
      transactionIndex = data1['result'][index]['transactionIndex']
      from1 = data1['result'][index]['from']
      to = data1['result'][index]['to']
      value1 = data1['result'][index]['value']
      gas = data1['result'][index]['gas']
      gasPrice = data1['result'][index]['gasPrice']
      isError = data1['result'][index]['isError']
      txreceipt_status = data1['result'][index]['txreceipt_status']
      input1 = data1['result'][index]['input']
      contractAddress = data1['result'][index]['contractAddress']

      if contractAddress == "":
        contractAddress = "empty"
      cumulativeGasUsed = data1['result'][index]['cumulativeGasUsed']
      gasUsed = data1['result'][index]['gasUsed']
      confirmations = data1['result'][index]['confirmations']

      embed=discord.Embed(title="[transaction history]", color=0xe8006f)
      embed.set_thumbnail(url="https://cdn.jsdelivr.net/gh/Xeift/image-hosting@main//a8eb74eaa4d1148c2b33db119edb9515.gif")
      embed.add_field(name="blockNumber" , value=f"{blockNumber}", inline=False)
      embed.add_field(name="timeStamp" , value=f"{timeStamp}", inline=False)
      embed.add_field(name="hash" , value=f"{hash}", inline=False)
      embed.add_field(name="nonce" , value=f"{nonce}", inline=False)
      embed.add_field(name="blockHash" , value=f"{blockHash}", inline=False)
      embed.add_field(name="transactionIndex" , value=f"{transactionIndex}", inline=False)
      embed.add_field(name="from" , value=f"{from1}", inline=False)
      embed.add_field(name="to" , value=f"{to}", inline=False)
      embed.add_field(name="value" , value=f"{value1}", inline=False)
      embed.add_field(name="gas" , value=f"{gas}", inline=False)
      embed.add_field(name="gasPrice" , value=f"{gasPrice}", inline=False)
      embed.add_field(name="isError" , value=f"{isError}", inline=False)
      embed.add_field(name="txreceipt_status" , value=f"{txreceipt_status}", inline=False)
      embed.add_field(name="input" , value=f"{input1}", inline=False)
      embed.add_field(name="contractAddress" , value=f"{contractAddress}", inline=False)
      embed.add_field(name="cumulativeGasUsed" , value=f"{cumulativeGasUsed}", inline=False)
      embed.add_field(name="gasUsed" , value=f"{gasUsed}", inline=False)
      embed.add_field(name="confirmations" , value=f"{confirmations}", inline=False)

      progresse = "◇" * icount 
      replacement = "◆"
      progresse2 = progresse[:9-index] + replacement + progresse[-index:]
      embed.add_field(name=f"{progresse2}" , value=f"page: {10-index}/{icount}", inline=False)
      await msg.edit(embed = embed)

################################################################################project history volume
@slash.slash(name="project-history",
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

async def project_history(ctx,project_name):
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
    embed.set_thumbnail(url="https://cdn.jsdelivr.net/gh/Xeift/image-hosting@main//1c0e140d3293a88391abaaa1e02f8e0e.png")
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
################################################################################project
@slash.slash(name="project",
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

async def project(ctx,project_name):
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
    embed=discord.Embed(title="["+project_name+"realtime information]", color=0xe8006f)
    embed.set_thumbnail(url="https://cdn.jsdelivr.net/gh/Xeift/image-hosting@main//1c0e140d3293a88391abaaa1e02f8e0e.png")
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
      await ctx.send("錯誤")
################################################################################NFT
@slash.slash(name="nft",
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

async def nft(ctx,contract_address,token_id):
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

################################################################################
keep_alive.keep_alive()
bot.run(discord_token)