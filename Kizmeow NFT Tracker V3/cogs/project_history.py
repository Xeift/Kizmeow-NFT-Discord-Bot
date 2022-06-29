import datetime

import discord
from discord.commands import Option
from discord.commands import slash_command
from discord.ext import commands
from opensea import OpenseaAPI


class project_history(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @slash_command(name='project_history', description='display project history information')
    async def project_history(
            self,
            ctx: discord.ApplicationContext,
            project_name: Option(str, 'collection slug at the end of OpenSea url')
    ):

        api = OpenseaAPI(apikey='OS_API')
        info = api.collection(collection_slug=project_name)

        banner_image_url = info['collection']['banner_image_url']

        project = info['collection']['name']

        slug = info['collection']['slug']

        if info['collection']['stats']['one_day_volume'] == None:
            one_day_volume = 'no data'
        else:
            one_day_volume = float(info['collection']['stats']['one_day_volume'])  # one_day_volume

        if info['collection']['stats']['one_day_sales'] == None:
            one_day_sales = 'no data'
        else:
            one_day_sales = float(info['collection']['stats']['one_day_sales'])

        if info['collection']['stats']['one_day_average_price'] == None:
            one_day_average_price = 'no data'
        else:
            one_day_average_price = float(info['collection']['stats']['one_day_average_price'])

        if info['collection']['stats']['seven_day_volume'] == None:
            seven_day_volume = 'no data'
        else:
            seven_day_volume = float(info['collection']['stats']['seven_day_volume'])

        if info['collection']['stats']['seven_day_sales'] == None:
            seven_day_sales = 'no data'
        else:
            seven_day_sales = float(info['collection']['stats']['seven_day_sales'])

        if info['collection']['stats']['seven_day_average_price'] == None:
            seven_day_average_price = 'no data'
        else:
            seven_day_average_price = float(info['collection']['stats']['seven_day_average_price'])

        if info['collection']['stats']['thirty_day_volume'] == None:
            thirty_day_volume = 'no data'
        else:
            thirty_day_volume = float(info['collection']['stats']['thirty_day_volume'])

        if info['collection']['stats']['thirty_day_sales'] == None:
            thirty_day_sales = 'no data'
        else:
            thirty_day_sales = float(info['collection']['stats']['thirty_day_sales'])

        if info['collection']['stats']['thirty_day_average_price'] == None:
            thirty_day_average_price = 'no data'
        else:
            thirty_day_average_price = float(info['collection']['stats']['thirty_day_average_price'])

        if (one_day_volume != 0):
            embed = discord.Embed(title='**' + project + '**', url='https://opensea.io/collection/' + slug,
                                  color=0xFFA46E)
            embed.set_image(url=banner_image_url)
            embed.add_field(name='1 day total trade volume', value='`'f'{one_day_volume:.2f} ETH''`', inline=True)
            embed.add_field(name='1 day sales quantity', value='`'f'{one_day_sales:.2f} NFT''`', inline=True)
            embed.add_field(name='1 day average price', value='`'f'{one_day_average_price:.2f} ETH''`', inline=True)
            embed.add_field(name='7 days total trade volume', value='`'f'{seven_day_volume:.2f} ETH''`', inline=True)
            embed.add_field(name='7 day sales quantity', value='`'f'{seven_day_sales:.2f} NFT''`', inline=True)
            embed.add_field(name='7 day average price', value='`'f'{seven_day_average_price:.2f} ETH''`', inline=True)
            embed.add_field(name='30 day total trade volume', value='`'f'{thirty_day_volume:.2f} ETH''`', inline=True)
            embed.add_field(name='30 day sales quantity', value='`'f'{thirty_day_sales:.2f} NFT''`', inline=True)
            embed.add_field(name='30 day average price', value='`'f'{thirty_day_average_price:.2f} ETH''`', inline=True)
            embed.timestamp = datetime.datetime.now()
            embed.set_footer(text=project)

            await ctx.respond(embed=embed)
        else:
            embed = discord.Embed(title='**[ERROR] cannot fetch data because the collection is too new**',
                                  color=0xFFA46E)
            await ctx.respond(embed=embed)


def setup(bot):
    bot.add_cog(project_history(bot))
