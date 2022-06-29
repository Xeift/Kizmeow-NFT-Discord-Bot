import datetime

import discord
from discord.commands import Option
from discord.commands import slash_command
from discord.ext import commands
from opensea import OpenseaAPI


class project_realtime(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @slash_command(name='project_realtime', description='display project realtime information')
    async def project_realtime(
            self,
            ctx: discord.ApplicationContext,
            project_name: Option(str, 'collection slug at the end of OpenSea url')
    ):
        api = OpenseaAPI(apikey='OS_API')
        info = api.collection(collection_slug=project_name)

        banner_image_url = info['collection']['banner_image_url']

        project = info['collection']['name']

        slug = info['collection']['slug']

        if info['collection']['stats']['floor_price'] == None:
            floor_price = 'no data'
        else:
            floor_price = float(info['collection']['stats']['floor_price'])

        if info['collection']['stats']['total_volume'] == None:
            total_volume = 'no data'
        else:
            total_volume = float(info['collection']['stats']['total_volume'])

        if info['collection']['stats']['total_sales'] == None:
            total_sales = 'no data'
        else:
            total_sales = float(info['collection']['stats']['total_sales'])

        if info['collection']['stats']['total_supply'] == None:
            total_supply = 'no data'
        else:
            total_supply = float(info['collection']['stats']['total_supply'])

        if info['collection']['stats']['num_owners'] == None:
            num_owners = 'no data'
        else:
            num_owners = float(info['collection']['stats']['num_owners'])

        if info['collection']['stats']['average_price'] == None:
            average_price = 'no data'
        else:
            average_price = float(info['collection']['stats']['average_price'])

        if info['collection']['stats']['num_reports'] == None:
            num_reports = 'no data'
        else:
            num_reports = float(info['collection']['stats']['num_reports'])

        if info['collection']['stats']['market_cap'] == None:
            market_cap = 'no data'
        else:
            market_cap = float(info['collection']['stats']['market_cap'])

        if (total_volume != 0):
            embed = discord.Embed(title='**' + project + '**', url='https://opensea.io/collection/' + slug,
                                  color=0xFFA46E)
            embed.set_image(url=banner_image_url)
            embed.add_field(name='Total volume', value='`'f'{total_volume:.2f} ETH''`', inline=True)
            embed.add_field(name='Total supply', value='`'f'{total_supply:.2f}  NFT''`', inline=True)
            embed.add_field(name='Total sales', value='`'f'{total_sales:.2f}  NFT''`', inline=True)
            embed.add_field(name='Holders', value='`'f'{num_owners:.2f}''`', inline=True)
            embed.add_field(name='Floor price', value='`'f'{floor_price:.2f} ETH''`', inline=True)
            embed.add_field(name='Average price', value='`'f'{average_price:.2f} ETH''`', inline=True)
            embed.add_field(name='Reports', value='`'f'{num_reports:.2f} times''`', inline=True)
            embed.add_field(name='Market cap', value='`'f'{market_cap:.2f} ETH''`', inline=True)
            embed.add_field(name='** **', value='** **', inline=True)
            embed.timestamp = datetime.datetime.now()
            embed.set_footer(text=project)

            await ctx.respond(embed=embed)
        else:
            embed = discord.Embed(title='**[ERROR] cannot fetch data because the collection is too new**',
                                  color=0xFFA46E)
            await ctx.respond(embed=embed)


def setup(bot):
    bot.add_cog(project_realtime(bot))
