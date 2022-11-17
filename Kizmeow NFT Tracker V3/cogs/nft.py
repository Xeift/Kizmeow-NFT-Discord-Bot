import re
import os
import discord
import datetime
import requests
from dotenv import load_dotenv
from discord.ext import commands
from discord.ui import Button, View
from discord.commands import Option
from discord.commands import slash_command


class nft(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(name='nft', description='View information about the NFT')
    async def nft(
            self,
            ctx: discord.ApplicationContext,
            collection: Option(str, 'Specify the collection slug'),
            token_id: Option(str, 'Enter the token number')
    ):
        b_rarity = Button(label='Rarity💎', style=discord.ButtonStyle.blurple)
        b_last_sale = Button(label='Last Sale💳', style=discord.ButtonStyle.green)
        b_return = Button(label='EXIT', style=discord.ButtonStyle.red)

        async def b_return_callback(interaction):
            view = View(timeout=None)
            view.add_item(b_rarity)
            view.add_item(b_last_sale)
            load_dotenv()
            url0 = f'https://api.modulenft.xyz/api/v2/eth/nft/token?slug={collection}&tokenId={token_id}'

            headers0 = {
                "accept": "application/json",
                "X-API-KEY": os.getenv('MODULE_API_KEY')
            }

            r0 = requests.get(url0, headers=headers0).json()
            print(r0)# TODO handle with no last sale
            if r0['data']['collection']['name'] == None:
                name = 'no data'
            else:
                name = r0['data']['collection']['name']

            if r0['data']['collection']['contractAddress'] == None:
                contractAddress = 'no data'
            else:
                contractAddress = str(r0['data']['collection']['contractAddress'])

            if r0['data']['collection']['images']['image_url'] == None:
                image_url = 'https://imgur.com/aSSH1jL'
            else:
                image_url = r0['data']['collection']['images']['image_url']

            if r0['data']['collection']['name'] == None:
                name_token = 'no data'
            else:
                name_token = r0['data']['collection']['name']

            if r0['data']['metadata']['image_cached'] == None:
                image_url_token = 'https://imgur.com/aSSH1jL'
            else:
                image_url_token = r0['data']['metadata']['image_cached']

            if r0['data']['metadata']['token_id'] == None:
                id_ = '0'
            else:
                id_ = str(r0['data']['metadata']['token_id'])

            if r0['data']['owner']['owner'] == None:
                owner = '0x0000000000000000000000000000000000000000'
            else:
                owner = r0['data']['owner']['owner']

            embed = discord.Embed(title=name_token, color=0xFFA46E)
            embed.set_image(url=image_url_token)
            embed.add_field(name='Owner', value=f'[{owner[0:6]}](https://etherscan.io/address/{owner})',
                            inline=False)
            embed.set_author(name=name, url=f'https://opensea.io/assets/{contractAddress}/{id_}',
                             icon_url=image_url)
            embed.set_footer(text=name, icon_url=image_url)
            embed.timestamp = datetime.datetime.now()

            await interaction.response.edit_message(embed=embed, view=view)

        b_return.callback = b_return_callback

        async def b_rarity_callback(interaction):
            load_dotenv()

            url1 = f'https://api.traitsniper.com/v1/collections/{contractAddress}/nfts?token_ids={id_}'

            headers1 = {
                'accept': 'application/json',
                'x-ts-api-key': os.getenv('TRAITSNIPER_API_KEY')
            }

            r1 = requests.get(url1, headers=headers1).json()

            if r1['nfts'][0]['rarity_rank'] == None:
                rarity_rank = '0'
            else:
                rarity_rank = r1['nfts'][0]['rarity_rank']

            if r1['nfts'][0]['rarity_score'] == None:
                rarity_score = '0'
            else:
                rarity_score = r1['nfts'][0]['rarity_score']

            embed = discord.Embed(title=f'{name_token}', color=0xFFA46E)
            embed.set_image(url=image_url_token)
            embed.add_field(name='Owner', value=f'[{owner[0:6]}](https://etherscan.io/address/{owner})',
                            inline=False)
            embed.add_field(name='Rank', value=rarity_rank, inline=True)
            embed.add_field(name='Score', value=f'{rarity_score:.2f}', inline=True)
            embed.add_field(name='═════════════Traits═════════════', value='_ _', inline=False)
            for t in r1['nfts'][0]['traits']:
                if (t['name']) == None:
                    name_t = 'no data'
                else:
                    name_t = (t['name'])
                if (t['value']) == None:
                    value = 'no data'
                else:
                    value = (t['value'])
                if (t['score']) == None:
                    score = 'no data'
                else:
                    score = float(t['score'])
                embed.add_field(name=name_t, value=f'{value}\n`{score:.2f}`', inline=True)
                embed.set_author(name=name, url=f'https://opensea.io/assets/{contractAddress}/{id_}',
                                 icon_url=image_url)
                embed.set_footer(text=name, icon_url=image_url)
                embed.timestamp = datetime.datetime.now()

            view = View(timeout=None)
            view.add_item(b_return)
            await interaction.response.edit_message(embed=embed, view=view)

        b_rarity.callback = b_rarity_callback

        async def b_last_sale_callback(interaction):
            if r0['data']['lastSale']['from_address'] == None:
                from_address = 'no data'
            else:
                from_address = r0['data']['lastSale']['from_address']

            if r0['data']['lastSale']['to_address'] == None:
                to_address = 'no data'
            else:
                to_address = r0['data']['lastSale']['to_address']

            if r0['data']['lastSale']['timestamp'] == None:
                time_stamp = datetime.datetime.now()
            else:
                time_stamp = r0['data']['lastSale']['timestamp']

            if r0['data']['lastSale']['sale_price_in_eth'] == None:
                sale_price_in_eth = 'no data'
            else:
                sale_price_in_eth = r0['data']['lastSale']['sale_price_in_eth']

            embed = discord.Embed(title=name_token, color=0xFFA46E)
            embed.set_image(url=image_url_token)
            embed.add_field(name='From',
                            value=f'[{from_address[0:6]}](https://etherscan.io/address/{from_address})',
                            inline=True)
            embed.add_field(name='To',
                            value=f'[{to_address[0:6]}](https://etherscan.io/address/{to_address})',
                            inline=True)
            embed.add_field(name='It was', value=f'<t:{time_stamp}:R>', inline=True)
            embed.add_field(name='Sales Price', value=f'{sale_price_in_eth} ETH', inline=True)
            embed.set_author(name=name, url=f'https://opensea.io/assets/{contractAddress}/{id_}',
                             icon_url=image_url)
            embed.set_footer(text=name, icon_url=image_url)
            embed.timestamp = datetime.datetime.now()

            view = View(timeout=None)
            view.add_item(b_return)
            await interaction.response.edit_message(embed=embed, view=view)

        b_last_sale.callback = b_last_sale_callback

        view = View(timeout=None)

        view.add_item(b_rarity)
        view.add_item(b_last_sale)

        load_dotenv()
        url0 = f'https://api.modulenft.xyz/api/v2/eth/nft/token?slug={collection}&tokenId={token_id}'

        headers0 = {
            'accept': 'application/json',
            'X-API-KEY': os.getenv('MODULE_API_KEY')
        }

        r0 = requests.get(url0, headers=headers0).json()

        if r0['data']['collection']['name'] == None:
            name = 'no data'
        else:
            name = r0['data']['collection']['name']

        if r0['data']['collection']['contractAddress'] == None:
            contractAddress = 'no data'
        else:
            contractAddress = str(r0['data']['collection']['contractAddress'])

        if r0['data']['collection']['images']['image_url'] == None:
            image_url = 'https://imgur.com/aSSH1jL'
        else:
            image_url = r0['data']['collection']['images']['image_url']

        if r0['data']['collection']['name'] == None:
            name_token = 'no data'
        else:
            name_token = r0['data']['collection']['name']

        if r0['data']['metadata']['image_cached'] == None:
            image_url_token = 'https://imgur.com/aSSH1jL'
        else:
            image_url_token = r0['data']['metadata']['image_cached']

        if r0['data']['metadata']['image'] == None:
            image_original = 'https://imgur.com/aSSH1jL'
        else:
            image_original = r0['data']['metadata']['image']
            image_original = re.sub('ipfs://', 'https://ipfs.io/ipfs/', r0['data']['metadata']['image'])

        if r0['data']['metadata']['token_id'] == None:
            id_ = '0'
        else:
            id_ = str(r0['data']['metadata']['token_id'])

        if r0['data']['owner']['owner'] == None:
            owner = '0x0000000000000000000000000000000000000000'
        else:
            owner = r0['data']['owner']['owner']

        b_image_link = Button(label='IPFS🧊', style=discord.ButtonStyle.link, url=image_original)
        view.add_item(b_image_link)

        embed = discord.Embed(title=f'{name_token}', color=0xFFA46E)
        embed.set_image(url=image_url_token)
        embed.add_field(name='Owner', value=f'[{owner[0:6]}](https://etherscan.io/address/{owner})',
                        inline=False)
        embed.set_author(name=name, url=f'https://opensea.io/assets/{contractAddress}/{id_}',
                         icon_url=image_url)
        embed.set_footer(text=name, icon_url=image_url)
        embed.timestamp = datetime.datetime.now()

        await ctx.respond(embed=embed, view=view)


def setup(bot):
    bot.add_cog(nft(bot))
