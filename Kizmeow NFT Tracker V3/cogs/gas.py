import datetime
import asyncio
import json
import urllib.request as ur
import discord
from discord.commands import slash_command
from discord.ext import commands


class gas(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @slash_command(name='gas', description='check ETH gas')
    async def gas(
            self,
            ctx: discord.ApplicationContext,
    ):
        url = 'https://api.etherscan.io/api?module=gastracker&action=gasoracle&apikey' \
              '=6QWR9PMXTHM9B5SCN756Q6BPCRRYA8WC92'  # api url 

        site = ur.urlopen(url)
        page = site.read()
        contents = page.decode()
        data = json.loads(contents)

        SafeGasPrice = data['result']['SafeGasPrice']
        ProposeGasPrice = data['result']['ProposeGasPrice']
        FastGasPrice = data['result']['FastGasPrice']

        embed = discord.Embed(title='**⛽ETH Gas Prices**', url='https://etherscan.io/gastracker', color=0xFFA46E)
        embed.set_image(url=)
        embed.add_field(name='Slow🐢', value='`' + SafeGasPrice + ' Gwei`', inline=False)
        embed.add_field(name='Normal🚶🏼‍♂', value='`' + ProposeGasPrice + ' Gwei`', inline=False)
        embed.add_field(name='Fast⚡', value='`' + FastGasPrice + ' Gwei`', inline=False)
        embed.timestamp = datetime.datetime.now()
        embed.set_footer(text='Fetched from etherscan')

        await ctx.respond(embed=embed)


def setup(bot):
    bot.add_cog(gas(bot))
