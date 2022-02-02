import discord
import asyncio 
from discord_slash.utils.manage_commands import create_option
import urllib.request as ur
import json
from discord_slash import cog_ext
from core.cog_core import cogcore
import os

etherscan_api_key = os.environ['etherscan_api_key']
class txn(cogcore):
  @cog_ext.cog_slash(
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

  async def txn(self,ctx, eth_address: str):
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
        react, user = await self.bot.wait_for("reaction_add", timeout=60.0, check=lambda r, u: r.message.id == msg.id and u.id == ctx.author.id and r.emoji in BUTTONS)
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

def setup(bot):
  bot.add_cog(txn(bot))