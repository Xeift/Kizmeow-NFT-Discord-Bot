import datetime
import asyncio
import json
import urllib.request as ur
import discord
from discord.commands import slash_command
from discord.ext import commands


class eth(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @slash_command(name='eth', description='check eth price')
    async def gas(
            self,
            ctx: discord.ApplicationContext,
    ):
        with open('Kizmeow NFT Tracker V3/config.json','r') as of:
            config = json.load(of)
            
        url = 'https://api.etherscan.io/api?module=stats&action=ethprice&apikey=' + config['ETHERSCAN_API_KEY']  # api url

        site = ur.urlopen(url)
        page = site.read()
        contents = page.decode()
        data = json.loads(contents)

        ethusd = data['result']['ethusd']

        embed = discord.Embed(title='**ETH Prices**', url='https://etherscan.io', color=0xFFA46E)
        embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/960985313608605728/992414103962390588/ETH.png')
        embed.add_field(name='1 ETH', value='`' + ethusd + ' USD`', inline=False)
        embed.timestamp = datetime.datetime.now()
        embed.set_footer(text='Fetched from etherscan')

        await ctx.respond(embed=embed)


def setup(bot):
    bot.add_cog(eth(bot))
