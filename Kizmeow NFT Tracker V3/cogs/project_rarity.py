import datetime
import discord
import requests
from discord.commands import Option
from discord.commands import slash_command
from discord.ext import commands
from opensea import OpenseaAPI


class project_rarity(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @slash_command(name='project_rarity',
                   description='query your NFT rarity from the contract address and token id you entered')
    async def project_rarity(
            self,
            ctx: discord.ApplicationContext,
            contract_address: Option(str, 'smart contract address of the project'),
            token_id: Option(str, 'token id of the NFT')
    ):
        global rank
        api = OpenseaAPI(apikey='OS_API')
        info = api.asset(asset_contract_address=contract_address,
                         token_id=token_id)

        if info['name'] == None:
            name = 'no data'
        else:
            name = info['name']

        if info['image_url'] == None:
            image_url = 'no data'
        else:
            image_url = info['image_url']

        if info['top_ownerships'][0]['owner']['user'] == None:
            top_ownerships = 'no data'
        else:
            top_ownerships = info['top_ownerships'][0]['owner']['user']['username']

        if info['permalink'] == None:
            permalink = 'no data'
        else:
            permalink = info['permalink']

            url = 'https://api.nftgo.dev/eth/v1/nft/' + contract_address + '/' + token_id + '/info'

            headers = {
                "Accept": "application/json",
                "X-API-KEY": "API_NFT_GO"
            }

            response = requests.get(url, headers=headers).json()

            if response['rarity']['score'] == None:
                score = 'no data'
            else:
                score = float(response['rarity']['score'])

            if response['rarity']['rank'] == None:
                rank = 'no data'
            else:
                rank = float(response['rarity']['rank'])

        embed = discord.Embed(title='**' + name + '**', url=permalink, color=0xFFA46E)
        embed.set_image(url=image_url)
        embed.add_field(name='Owner', value='`' + top_ownerships + '`', inline=True)
        embed.add_field(name='Score', value='`'f'{score}`', inline=True)
        embed.add_field(name='Rank', value='`'f'{rank}`', inline=True)
        embed.add_field(name='Detailed Rarity',
                        value='>>> [watch](https://nftgo.io/asset/ETH/' + contract_address + '/' + token_id + ')',
                        inline=True)
        embed.timestamp = datetime.datetime.now()
        embed.set_footer(text=name)

        await ctx.respond(embed=embed)


def setup(bot):
    bot.add_cog(project_rarity(bot))
