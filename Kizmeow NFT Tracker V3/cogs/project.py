import os
import discord
import datetime
import requests
from dotenv import load_dotenv
from discord.ext import commands
from discord.ui import Button, View
from discord.commands import Option
from discord.commands import slash_command


class project(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @slash_command(name='project', description='Display project history information')
    async def project(
            self,
            ctx: discord.ApplicationContext,
            collection: Option(str, 'collection slug at the end of OpenSea url')
    ):
        b_opensea = Button(label='OpenSea🌊', style=discord.ButtonStyle.blurple)
        b_looksrare = Button(label='LooksRare👀', style=discord.ButtonStyle.green)
        b_x2y2 = Button(label='X2Y2🌀', style=discord.ButtonStyle.grey)
        b_return = Button(label='EXIT', style=discord.ButtonStyle.red)

        async def b_return_callback(interaction):
            global author_url
            view = View()
            view.add_item(b_opensea)
            view.add_item(b_looksrare)
            view.add_item(b_x2y2)

            load_dotenv()
            url0 = "https://api.modulenft.xyz/api/v2/eth/nft/collection?slug="f'{collection}'

            headers0 = {
                "accept": "application/json",
                "X-API-KEY": os.getenv('MODULE_API_KEY')
            }

            r0 = requests.get(url0, headers=headers0).json()

            if r0['data']['name'] == None:
                name = 'no data'
            else:
                name = r0['data']['name']

            if r0['data']['slug'] == None:
                slug = 'no data'
            else:
                slug = r0['data']['slug']

            if r0['data']['description'] == None:
                description = 'no data'
            else:
                description = r0['data']['description']

            if r0['data']['socials']['external_url'] == None:
                external_url = 'https://www.youtube.com/watch?v=dQw4w9WgXcQ'
            else:
                external_url = r0['data']['socials']['external_url']

            if r0['data']['socials']['discord_url'] == None:
                discord_url = 'https://www.youtube.com/watch?v=dQw4w9WgXcQ'
            else:
                discord_url = r0['data']['socials']['discord_url']

            if r0['data']['socials']['twitter_username'] == None:
                twitter_username = 'rickastley'
            else:
                twitter_username = r0['data']['socials']['twitter_username']

            if r0['data']['images']['image_url'] == None:
                image_url = 'https://imgur.com/aSSH1jL'
            else:
                image_url = r0['data']['images']['image_url']

            if r0['data']['images']['banner_image_url'] == None:
                banner_image_url = 'https://tenor.com/view/glitch-discord-gif-gif-20819419'
            else:
                banner_image_url = r0['data']['images']['banner_image_url']

            if r0['data']['createdDate'] == None:
                time_ = '757371600'
            else:
                time_ = r0['data']['createdDate']

            dt = datetime.datetime.fromisoformat(time_)
            stamp = int(dt.timestamp())
            result = str(stamp)

            embed = discord.Embed(title=f'{name}', color=0xFFA46E)
            embed.set_image(url=banner_image_url)
            embed.add_field(name='Description', value=f'{description}...', inline=False)
            embed.add_field(name='Created', value='<t:'f'{result}'':R>', inline=False)
            embed.add_field(name='_ _',
                            value='[Website]('f'{external_url})║[Discord]('f'{discord_url})║[Twitter](https://twitter.com/'f'{twitter_username})',
                            inline=False)
            embed.set_author(name=f'{name}', url="https://opensea.io/collection/"f'{slug}', icon_url=image_url)
            embed.set_footer(text=f'{name}', icon_url=image_url)
            embed.timestamp = datetime.datetime.now()

            await interaction.response.edit_message(embed=embed, view=view)

        b_return.callback = b_return_callback

        async def b_opensea_callback(interaction):
            load_dotenv()
            url1 = "https://api.modulenft.xyz/api/v2/eth/nft/stats?slug="f'{collection}'"&marketplace=Opensea"

            headers1 = {
                "accept": "application/json",
                "X-API-KEY": os.getenv('MODULE_API_KEY')
            }

            r1 = requests.get(url1, headers=headers1).json()

            if r1['data']['dailyVolume'] == None:
                dailyVolume_opensea = 0
            else:
                dailyVolume_opensea = float(r1['data']['dailyVolume'])

            if r1['data']['WeeklyVolume'] == None:
                WeeklyVolume_opensea = 0
            else:
                WeeklyVolume_opensea = float(r1['data']['WeeklyVolume'])

            if r1['data']['monthlyVolume'] == None:
                monthlyVolume_opensea = 0
            else:
                monthlyVolume_opensea = float(r1['data']['monthlyVolume'])

            if r1['data']['dailySalesCount'] == None:
                dailySalesCount_opensea = 0
            else:
                dailySalesCount_opensea = float(r1['data']['dailySalesCount'])

            if r1['data']['weeklySalesCount'] == None:
                weeklySalesCount_opensea = 0
            else:
                weeklySalesCount_opensea = float(r1['data']['weeklySalesCount'])

            if r1['data']['monthlySalesCount'] == None:
                monthlySalesCount_opensea = 0
            else:
                monthlySalesCount_opensea = float(r1['data']['monthlySalesCount'])

            if r1['data']['dailyAveragePrice'] == None:
                dailyAveragePrice_opensea = 0
            else:
                dailyAveragePrice_opensea = float(r1['data']['dailyAveragePrice'])

            if r1['data']['weeklyAveragePrice'] == None:
                weeklyAveragePrice_opensea = 0
            else:
                weeklyAveragePrice_opensea = float(r1['data']['weeklyAveragePrice'])

            if r1['data']['monthlyAveragePrice'] == None:
                monthlyAveragePrice_opensea = 0
            else:
                monthlyAveragePrice_opensea = float(r1['data']['monthlyAveragePrice'])

            embed = discord.Embed(title=f'{name}', color=0x6495ed)
            embed.set_image(url='https://open-graph.opensea.io/v1/collections/'f'{slug}')
            embed.add_field(name='Volume daily', value=f'{dailyVolume_opensea:.2f} ETH', inline=True)
            embed.add_field(name='Volume Weekly', value=f'{WeeklyVolume_opensea:.2f} ETH', inline=True)
            embed.add_field(name='Volume Monthly', value=f'{monthlyVolume_opensea:.2f} ETH', inline=True)
            embed.add_field(name='Sales daily', value=f'{dailySalesCount_opensea} NFT', inline=True)
            embed.add_field(name='Sales Weekly', value=f'{weeklySalesCount_opensea} NFT', inline=True)
            embed.add_field(name='Sales Monthly', value=f'{monthlySalesCount_opensea} NFT', inline=True)
            embed.add_field(name='Average daily', value=f'{dailyAveragePrice_opensea:.2f} ETH', inline=True)
            embed.add_field(name='Average Weekly', value=f'{weeklyAveragePrice_opensea:.2f} ETH', inline=True)
            embed.add_field(name='Average Monthly', value=f'{monthlyAveragePrice_opensea:.2f} ETH', inline=True)
            embed.set_author(name=f'{name}', url='https://opensea.io/collection/'f'{slug}', icon_url=image_url)
            embed.set_footer(text='OpenSea🌊',
                             icon_url='https://storage.googleapis.com/opensea-static/Logomark/Logomark-Blue.png')
            embed.timestamp = datetime.datetime.now()

            view = View()
            view.add_item(b_return)
            await interaction.response.edit_message(embed=embed, view=view)

        b_opensea.callback = b_opensea_callback

        async def b_looksrare_callback(interaction):
            load_dotenv()
            url2 = "https://api.modulenft.xyz/api/v2/eth/nft/stats?slug="f'{collection}'"&marketplace=Looksrare"

            headers2 = {
                "accept": "application/json",
                "X-API-KEY": os.getenv('MODULE_API_KEY')
            }

            r2 = requests.get(url2, headers=headers2).json()

            if r2['data']['address'] == None:
                address_looksrare = 'no data'
            else:
                address_looksrare = r2['data']['address']

            if r2['data']['DailyVolume'] == None:
                dailyVolume_looksrare = 0
            else:
                dailyVolume_looksrare = float(r2['data']['DailyVolume'])

            if r2['data']['WeeklyVolume'] == None:
                WeeklyVolume_looksrare = 0
            else:
                WeeklyVolume_looksrare = float(r2['data']['WeeklyVolume'])

            if r2['data']['MonthlyVolume'] == None:
                monthlyVolume_looksrare = 0
            else:
                monthlyVolume_looksrare = float(r2['data']['MonthlyVolume'])

            if r2['data']['dailySalesCount'] == None:
                dailySalesCount_looksrare = 0
            else:
                dailySalesCount_looksrare = float(r2['data']['dailySalesCount'])

            if r2['data']['weeklySalesCount'] == None:
                weeklySalesCount_looksrare = 0
            else:
                weeklySalesCount_looksrare = float(r2['data']['weeklySalesCount'])

            if r2['data']['monthlySalesCount'] == None:
                monthlySalesCount_looksrare = 0
            else:
                monthlySalesCount_looksrare = float(r2['data']['monthlySalesCount'])

            if r2['data']['dailyAveragePrice'] == None:
                dailyAveragePrice_looksrare = 0
            else:
                dailyAveragePrice_looksrare = float(r2['data']['dailyAveragePrice'])

            if r2['data']['weeklyAveragePrice'] == None:
                weeklyAveragePrice_looksrare = 0
            else:
                weeklyAveragePrice_looksrare = float(r2['data']['weeklyAveragePrice'])

            if r2['data']['monthlyAveragePrice'] == None:
                monthlyAveragePrice_looksrare = 0
            else:
                monthlyAveragePrice_looksrare = float(r2['data']['monthlyAveragePrice'])

            if r2['data']['tokenListedCount'] == None:
                tokenListedCount_looksrare = 0
            else:
                tokenListedCount_looksrare = float(r2['data']['tokenListedCount'])

            if r2['data']['holders'] == None:
                holders_looksrare = 0
            else:
                holders_looksrare = float(r2['data']['holders'])

            if r2['data']['floorPrice']['price'] == None:
                floor_looksrare = 0
            else:
                floor_looksrare = float(r2['data']['floorPrice']['price'])

            embed = discord.Embed(title=f'{name}', color=0x5ccf51)
            embed.set_image(url=banner_image_url)
            embed.add_field(name='Volume daily', value=f'{dailyVolume_looksrare:.2f} ETH', inline=True)
            embed.add_field(name='Volume Weekly', value=f'{WeeklyVolume_looksrare:.2f} ETH', inline=True)
            embed.add_field(name='Volume Monthly', value=f'{monthlyVolume_looksrare:.2f} ETH', inline=True)
            embed.add_field(name='Sales daily', value=f'{dailySalesCount_looksrare} NFT', inline=True)
            embed.add_field(name='Sales Weekly', value=f'{weeklySalesCount_looksrare} NFT', inline=True)
            embed.add_field(name='Sales Monthly', value=f'{monthlySalesCount_looksrare} NFT', inline=True)
            embed.add_field(name='Average daily', value=f'{dailyAveragePrice_looksrare} ETH', inline=True)
            embed.add_field(name='Average Weekly', value=f'{weeklyAveragePrice_looksrare:.2f} ETH', inline=True)
            embed.add_field(name='Average Monthly', value=f'{monthlyAveragePrice_looksrare:.2f} ETH', inline=True)
            embed.add_field(name='Listed Count', value=f'{tokenListedCount_looksrare} NFT', inline=True)
            embed.add_field(name='Holders', value=f'{holders_looksrare} PPL', inline=True)
            embed.add_field(name='Floor', value=f'{floor_looksrare:.2f} ETH', inline=True)
            embed.set_author(name=f'{name}', url='https://looksrare.org/collections/'f'{address_looksrare}',
                             icon_url=image_url)
            embed.set_footer(text='LooksRare👀',
                             icon_url='https://raw.githubusercontent.com/Xeift/Kizmeow-NFT-Discord-Bot/main/access/looks-green.png')
            embed.timestamp = datetime.datetime.now()

            view = View()
            view.add_item(b_return)
            await interaction.response.edit_message(embed=embed, view=view)

        b_looksrare.callback = b_looksrare_callback

        async def b_x2y2_callback(interaction):
            load_dotenv()
            url3 = "https://api.modulenft.xyz/api/v2/eth/nft/stats?slug="f'{collection}'"&marketplace=X2Y2"

            headers3 = {
                "accept": "application/json",
                "X-API-KEY": os.getenv('MODULE_API_KEY')
            }

            r3 = requests.get(url3, headers=headers3).json()

            if r3['data']['dailyVolume'] == None:
                dailyVolume_x2y2 = 0
            else:
                dailyVolume_x2y2 = float(r3['data']['dailyVolume'])

            if r3['data']['WeeklyVolume'] == None:
                WeeklyVolume_x2y2 = 0
            else:
                WeeklyVolume_x2y2 = float(r3['data']['WeeklyVolume'])

            if r3['data']['MonthlyVolume'] == None:
                monthlyVolume_x2y2 = 0
            else:
                monthlyVolume_x2y2 = float(r3['data']['MonthlyVolume'])

            if r3['data']['dailySalesCount'] == None:
                dailySalesCount_x2y2 = 0
            else:
                dailySalesCount_x2y2 = float(r3['data']['dailySalesCount'])

            if r3['data']['weeklySalesCount'] == None:
                weeklySalesCount_x2y2 = 0
            else:
                weeklySalesCount_x2y2 = float(r3['data']['weeklySalesCount'])

            if r3['data']['monthlySalesCount'] == None:
                monthlySalesCount_x2y2 = 0
            else:
                monthlySalesCount_x2y2 = float(r3['data']['monthlySalesCount'])

            if r3['data']['dailyAveragePrice'] == None:
                dailyAveragePrice_x2y2 = 0
            else:
                dailyAveragePrice_x2y2 = float(r3['data']['dailyAveragePrice'])

            if r3['data']['weeklyAveragePrice'] == None:
                weeklyAveragePrice_x2y2 = 0
            else:
                weeklyAveragePrice_x2y2 = float(r3['data']['weeklyAveragePrice'])

            if r3['data']['monthlyAveragePrice'] == None:
                monthlyAveragePrice_x2y2 = 0
            else:
                monthlyAveragePrice_x2y2 = float(r3['data']['monthlyAveragePrice'])

            if r3['data']['tokenListedCount'] == None:
                tokenListedCount_x2y2 = 0
            else:
                tokenListedCount_x2y2 = float(r3['data']['tokenListedCount'])

            if r3['data']['holders'] == None:
                holders_x2y2 = 0
            else:
                holders_x2y2 = float(r3['data']['holders'])

            if r3['data']['floorPrice']['price'] == None:
                floor_x2y2 = 0
            else:
                floor_x2y2 = float(r3['data']['floorPrice']['price'])

            embed = discord.Embed(title=f'{name}', color=0x444072)
            embed.set_image(url=banner_image_url)
            embed.add_field(name='Volume daily', value=f'{dailyVolume_x2y2:.2f} ETH', inline=True)
            embed.add_field(name='Volume Weekly', value=f'{WeeklyVolume_x2y2:.2f} ETH', inline=True)
            embed.add_field(name='Volume Monthly', value=f'{monthlyVolume_x2y2:.2f} ETH', inline=True)
            embed.add_field(name='Sales daily', value=f'{dailySalesCount_x2y2} NFT', inline=True)
            embed.add_field(name='Sales Weekly', value=f'{weeklySalesCount_x2y2} NFT', inline=True)
            embed.add_field(name='Sales Monthly', value=f'{monthlySalesCount_x2y2} NFT', inline=True)
            embed.add_field(name='Average daily', value=f'{dailyAveragePrice_x2y2} ETH', inline=True)
            embed.add_field(name='Average Weekly', value=f'{weeklyAveragePrice_x2y2:.2f} ETH', inline=True)
            embed.add_field(name='Average Monthly', value=f'{monthlyAveragePrice_x2y2:.2f} ETH', inline=True)
            embed.add_field(name='Listed Count', value=f'{tokenListedCount_x2y2} NFT', inline=True)
            embed.add_field(name='Holders', value=f'{holders_x2y2} PPL', inline=True)
            embed.add_field(name='Floor', value=f'{floor_x2y2:.2f} ETH', inline=True)
            embed.set_author(name=f'{name}', url="https://x2y2.io/collection/"f'{slug}'"/items", icon_url=image_url)
            embed.set_footer(text='X2Y2🌀',
                             icon_url='https://raw.githubusercontent.com/Xeift/Kizmeow-NFT-Discord-Bot/main/access/x2y2_logo.png')
            embed.timestamp = datetime.datetime.now()

            view = View()
            view.add_item(b_return)
            await interaction.response.edit_message(embed=embed, view=view)

        b_x2y2.callback = b_x2y2_callback

        view = View()

        view.add_item(b_opensea)
        view.add_item(b_looksrare)
        view.add_item(b_x2y2)

        load_dotenv()
        url0 = "https://api.modulenft.xyz/api/v2/eth/nft/collection?slug="f'{collection}'

        headers0 = {
            "accept": "application/json",
            "X-API-KEY": os.getenv('MODULE_API_KEY')
        }

        r0 = requests.get(url0, headers=headers0).json()

        if r0['data']['name'] == None:
            name = 'no data'
        else:
            name = r0['data']['name']

        if r0['data']['slug'] == None:
            slug = 'no data'
        else:
            slug = r0['data']['slug']

        if r0['data']['description'] == None:
            description = 'no data'
        else:
            description = r0['data']['description']

        if r0['data']['socials']['external_url'] == None:
            external_url = 'https://www.youtube.com/watch?v=dQw4w9WgXcQ'
        else:
            external_url = r0['data']['socials']['external_url']

        if r0['data']['socials']['discord_url'] == None:
            discord_url = 'https://www.youtube.com/watch?v=dQw4w9WgXcQ'
        else:
            discord_url = r0['data']['socials']['discord_url']

        if r0['data']['socials']['twitter_username'] == None:
            twitter_username = 'rickastley'
        else:
            twitter_username = r0['data']['socials']['twitter_username']

        if r0['data']['images']['image_url'] == None:
            image_url = 'https://imgur.com/aSSH1jL'
        else:
            image_url = r0['data']['images']['image_url']

        if r0['data']['images']['banner_image_url'] == None:
            banner_image_url = 'https://tenor.com/view/glitch-discord-gif-gif-20819419'
        else:
            banner_image_url = r0['data']['images']['banner_image_url']

        if r0['data']['createdDate'] == None:
            time_ = '757371600'
        else:
            time_ = r0['data']['createdDate']

        dt = datetime.datetime.fromisoformat(time_)
        stamp = int(dt.timestamp())
        result = str(stamp)

        embed = discord.Embed(title=f'{name}', color=0xFFA46E)
        embed.set_image(url=banner_image_url)
        embed.add_field(name='Description', value=f'{description}...', inline=False)
        embed.add_field(name='Created', value='<t:'f'{result}'':R>', inline=False)
        embed.add_field(name='_ _',
                        value='[Website]('f'{external_url})║[Discord]('f'{discord_url})║[Twitter](https://twitter.com/'f'{twitter_username})',
                        inline=False)
        embed.set_author(name=f'{name}', url="https://opensea.io/collection/"f'{slug}', icon_url=image_url)
        embed.set_footer(text=f'{name}', icon_url=image_url)
        embed.timestamp = datetime.datetime.now()

        await ctx.respond(embed=embed, view=view)


def setup(bot):
    bot.add_cog(project(bot))
