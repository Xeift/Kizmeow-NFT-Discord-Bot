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
import time
import keep_alive

discord_token = os.environ['discord_token']
etherscan_api_key = os.environ['etherscan_api_key']
opensea_api_key = os.environ['opensea_api_key']

bot = commands.Bot(command_prefix="k!",
intents=discord.Intents.all(),
help_command=None)
slash = SlashCommand(bot, sync_commands=True) 

@bot.event
async def on_ready():
  print("Ready!")

guild_ids = [906053473181769778] # Put your server ID in this array.

################################################################################ping
@slash.slash(name="ping",description="return bot latency", guild_ids=guild_ids)
async def _ping(ctx):
  await ctx.send(f"pong! ({bot.latency*1000} ms)")
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
    embed.add_field(name="Demi-Human balance" , value=demi_balance+" Demi", inline=False)
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
  print(url1)

  site1 = ur.urlopen(url1)
  page1 = site1.read()
  contents1 = page1.decode()
  data1 = json.loads(contents1)

  index = 9
  blockNumber = data1['result'][index]['blockNumber']
  print(blockNumber)
  timeStamp = data1['result'][index]['timeStamp']
  print(timeStamp)
  hash = data1['result'][index]['hash']
  print(hash)
  nonce = data1['result'][index]['nonce']
  print(nonce)
  blockHash = data1['result'][index]['blockHash']
  print(blockHash)
  transactionIndex = data1['result'][index]['transactionIndex']
  print(transactionIndex)
  from1 = data1['result'][index]['from']
  print(from1)
  to = data1['result'][index]['to']
  print(to)
  value1 = data1['result'][index]['value']
  print(value1)
  gas = data1['result'][index]['gas']
  print(gas)
  gasPrice = data1['result'][index]['gasPrice']
  print(gasPrice)
  isError = data1['result'][index]['isError']
  print(isError)
  txreceipt_status = data1['result'][index]['txreceipt_status']
  print(txreceipt_status)
  input1 = data1['result'][index]['input']
  print(input1)
  contractAddress = data1['result'][index]['contractAddress']
  print(contractAddress)
  if contractAddress == "":
    contractAddress = "empty"
  cumulativeGasUsed = data1['result'][index]['cumulativeGasUsed']
  print(cumulativeGasUsed)
  gasUsed = data1['result'][index]['gasUsed']
  print(gasUsed)
  confirmations = data1['result'][index]['confirmations']
  print(confirmations)

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
  embed.add_field(name=f"{progresse2}" , value=f"頁數：{10-index}/{icount}", inline=False)
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
      print(blockNumber)
      timeStamp = data1['result'][index]['timeStamp']
      print(timeStamp)
      hash = data1['result'][index]['hash']
      print(hash)
      nonce = data1['result'][index]['nonce']
      print(nonce)
      blockHash = data1['result'][index]['blockHash']
      print(blockHash)
      transactionIndex = data1['result'][index]['transactionIndex']
      print(transactionIndex)
      from1 = data1['result'][index]['from']
      print(from1)
      to = data1['result'][index]['to']
      print(to)
      value = data1['result'][index]['value']
      print(value)
      gas = data1['result'][index]['gas']
      print(gas)
      gasPrice = data1['result'][index]['gasPrice']
      print(gasPrice)
      isError = data1['result'][index]['isError']
      print(isError)
      txreceipt_status = data1['result'][index]['txreceipt_status']
      print(txreceipt_status)
      input1 = data1['result'][index]['input']
      print(input1)
      contractAddress = data1['result'][index]['contractAddress']
      if contractAddress == "":
        contractAddress = "empty"
      print(contractAddress)
      cumulativeGasUsed = data1['result'][index]['cumulativeGasUsed']
      print(cumulativeGasUsed)
      gasUsed = data1['result'][index]['gasUsed']
      print(gasUsed)
      confirmations = data1['result'][index]['confirmations']
      print(confirmations)

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
      embed.add_field(name=f"{progresse2}" , value=f"頁數：{10-index}/{icount}", inline=False)
      await msg.edit(embed = embed)
################################################################################project info(working)
@slash.slash(
name="project_info",
description="get the project info of ERC-20 token from the contract address you enter",
options=
[
  create_option
  (
    name="contract_address",
    description="enter contract address",
    option_type=3,
    required=False
  )
]
)

async def project_info(ctx, *contract_address: str):
# await ctx.send(content=f"{eth_address}")
  
  # etherscan_token = str(etherscan_api_key)
  # if contract_address == "kkk":
  #   url1='https://api.etherscan.io/api?module=stats&action=tokensupply&contractaddress=0xa6916545a56f75acd43fb6a1527a73a41d2b4081&apikey='+etherscan_token #api url
  #   print(url1)
  # else:
  #   url1='https://api.etherscan.io/api?module=stats&action=tokensupply&contractaddress='+contract_address+'&apikey='+etherscan_token #api url
  #   print(url1)
  
  url1='https://api.etherscan.io/api?module=stats&action=tokensupply&contractaddress=0xa6916545a56f75acd43fb6a1527a73a41d2b4081&apikey='+(etherscan_api_key) #api url
  print(url1)
  site1 = ur.urlopen(url1)
  page1 = site1.read()
  contents1 = page1.decode()
  data1 = json.loads(contents1)

  total_supply = data1['result']#total supply

  if(total_supply != 0):
    embed=discord.Embed(title="[total supply]", color=0xe8006f)
    embed.set_thumbnail(url="https://cdn.jsdelivr.net/gh/Xeift/image-hosting@main//1c0e140d3293a88391abaaa1e02f8e0e.png")
    embed.add_field(name="total supply" , value=total_supply, inline=False)
          
    await ctx.send(embed=embed)
  else:
      await ctx.send("no token in this address or you've entered the wrong address")
################################################################################demi_pass
#@slash.slash(name="demi_pass",description="generate a qrcode for verification if you have demi-pass", guild_ids=guild_ids)
@bot.command()
async def demi_pass(ctx,message=None):
  role = discord.utils.get(ctx.guild.roles, name="DemiPASS")


  if role in ctx.message.author.roles:
    userid = ctx.message.author.id
    tz = timezone(timedelta(hours=+8))
    t_qr = datetime.now(tz).isoformat(timespec="seconds")
    print(t_qr)
    date_qr = t_qr[:10]
    hour_qr = t_qr[11:13]
    minute_qr = t_qr[14:16]
    second_qr = t_qr[17:19]
    if int(minute_qr) >=50 :
      minute_qr2 = str(int(minute_qr)+10-60)
      if int(hour_qr) == 23 :
        hour_qr = str(int(hour_qr)+1-24)
    else:
      minute_qr2 =  str(int(minute_qr)+10)
    verifyctx = "[Demi-Pass]\n["+str(userid)+"]\n[創建時間："+date_qr+" "+hour_qr+":"+minute_qr+":"+second_qr+"]\n[失效時間："+date_qr+" "+hour_qr+":"+minute_qr2+":"+second_qr+"]\n[有效時間：10分鐘]"
    img = qrcode.make(verifyctx)
    type(img)  
    img.save("qr_temp/qrcodeimg.png")
    qrpic = discord.File("qr_temp/qrcodeimg.png")
    msg = await ctx.send(file = qrpic)
  else:
    msg = await ctx.send("你還沒有DemiPASS唷，可以去https://opensea.io/collection/demihuman ||花10ETH||買一個Demi Human NFT")

  BUTTONS = ["✅"]
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
        await msg.delete()
        await ctx.send("交易完成")
################################################################################
keep_alive.keep_alive()
bot.run(discord_token)