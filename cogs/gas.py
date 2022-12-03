import os
import discord
import datetime
from dotenv import load_dotenv
from etherscan import Etherscan
from discord.ext import commands
from discord.commands import slash_command


class gas(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @slash_command(name='gas', description='Check eth gas')
    async def gas(
            self,
            ctx: discord.ApplicationContext,
    ):
        load_dotenv()
        eth = Etherscan(os.getenv('ETHERSCAN_API_KEY'))
        gas_oracle = eth.get_gas_oracle()

        embed = discord.Embed(title='**ETH Gas Prices**', color=0xFFA46E)
        embed.set_thumbnail(
            url='https://raw.githubusercontent.com/Xeift/Kizmeow-OpenSea-and-Etherscan-Discord-Bot/main/access/eth-diamond-black.png')
        embed.add_field(name='_ _',
                        value='**Slow🐢 ║** `' + gas_oracle['SafeGasPrice'] + ' Gwei`\n\n**Normal🚶🏼‍♂ ║** `' +
                              gas_oracle[
                                  'ProposeGasPrice'] + ' Gwei`\n\n**Fast⚡ ║** `' + gas_oracle[
                                  'FastGasPrice'] + ' Gwei`',
                        inline=False)
        embed.timestamp = datetime.datetime.now()
        embed.set_footer(text='Powered by',
                         icon_url='https://raw.githubusercontent.com/Xeift/Kizmeow-OpenSea-and-Etherscan-Discord-Bot/main/access/etherscan-logo-circle.png')
        embed.set_author(name='Etherscan', url='https://etherscan.io/gastracker',
                         icon_url="https://raw.githubusercontent.com/Xeift/Kizmeow-OpenSea-and-Etherscan-Discord-Bot/main/access/etherscan-logo-circle.png")

        await ctx.respond(embed=embed, ephemeral=True)


def setup(bot):
    bot.add_cog(gas(bot))
