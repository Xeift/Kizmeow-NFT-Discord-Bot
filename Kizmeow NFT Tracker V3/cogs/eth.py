import os
import discord
import datetime
from etherscan import Etherscan
from dotenv import load_dotenv
from discord.ext import commands
from discord.commands import slash_command


class eth(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @slash_command(name='eth', description='Check eth price')
    async def gas(
            self,
            ctx: discord.ApplicationContext,
    ):
        load_dotenv()
        eth = Etherscan(os.getenv('ETHERSCAN_API_KEY'))
        get_eth_last_price = eth.get_eth_last_price()

        embed = discord.Embed(title='**ETH Prices**', color=0xFFA46E)
        embed.set_thumbnail(
            url='https://raw.githubusercontent.com/Xeift/Kizmeow-OpenSea-and-Etherscan-Discord-Bot/main/access/eth-diamond-black.png')
        embed.add_field(name='1 ETH', value='`' + get_eth_last_price['ethusd'] + ' USD`', inline=False)
        embed.timestamp = datetime.datetime.now()
        embed.set_footer(text='Powered by',
                         icon_url='https://raw.githubusercontent.com/Xeift/Kizmeow-OpenSea-and-Etherscan-Discord-Bot/main/access/etherscan-logo-circle.png')
        embed.set_author(name='Etherscan', url='https://etherscan.io',
                         icon_url="https://raw.githubusercontent.com/Xeift/Kizmeow-OpenSea-and-Etherscan-Discord-Bot/main/access/etherscan-logo-circle.png")

        await ctx.send_response(embed=embed)


def setup(bot):
    bot.add_cog(eth(bot))
