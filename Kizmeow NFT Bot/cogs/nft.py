import re
import os
import discord
import datetime
import requests
from dotenv import load_dotenv
from discord.ext import commands
from discord.ui import Button, View
from discord.commands import Option, slash_command


class nft(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        
    @commands.slash_command(name='nft', description='View NFT information')
    async def nft(
            self,
            ctx: discord.ApplicationContext,
            collection: Option(str, 'Specify the collection slug'),
            token_id: Option(str, 'Enter the token number')
    ):
        #----------------------------------------------------------------------------------------------------------------------------------------------------------------
        rarity_button = Button(label='Rarity💎', style=discord.ButtonStyle.blurple)
        lastSale_button = Button(label='Last Sale💳', style=discord.ButtonStyle.green)
        ipfs_button = Button(label='IPFS🧊', style=discord.ButtonStyle.link)
        return_button = Button(label='EXIT', style=discord.ButtonStyle.red)
        #----------------------------------------------------------------------------------------------------------------------------------------------------------------
        load_dotenv()
        url = f'https://api.modulenft.xyz/api/v2/eth/nft/token?slug={collection}&tokenId={token_id}'
        headers = {
            'accept': 'application/json',
            'X-API-KEY': os.getenv('MODULE_API_KEY')
        }
        r = requests.get(url=url, headers=headers).json()
        print(r)
        if r['error'] != None:
            embed = discord.Embed(title='[ERROR]', description=f'`{r["error"]["message"]}`\n\nOther possible reasons:\nhttps://kizmeow.gitbook.io/kizmeow-nft-discord-bot/information/faq\nJoin support server to report the problem.\nhttps://discord.gg/PxNF9PaSKv', color=0xFFA46E)
            await ctx.respond(embed=embed, ephemeral=True)
            return

        collection_name = 'no dara' if r['data']['collection']['name'] == None else r['data']['collection']['name']
        nft_image = 'no data' if r['data']['metadata']['image_cached'] == None else r['data']['metadata']['image_cached']
        nft_owner = 'no data' if r['data']['owner']['owner'] == None else r['data']['owner']['owner']
        collection_image = 'https://imgur.com/aSSH1jL' if r['data']['collection']['images']['image_url'] == None else r['data']['collection']['images']['image_url']
        collection_contract_address = 'no data' if r['data']['collection']['contractAddress'] == None else r['data']['collection']['contractAddress']
        nft_IPFS_image = 'https://imgur.com/aSSH1jL' if r['data']['metadata']['image'] == None else r['data']['metadata']['image']
        nft_IPFS_image = re.sub('ipfs://', 'https://ipfs.io/ipfs/', nft_IPFS_image)
        erc_type = 'no data' if r['data']['collection']['ercType'] == None else r['data']['collection']['ercType']

        from_address = 'no data' if r['data']['lastSale']['from_address'] == None else r['data']['lastSale']['from_address']
        to_address = 'no data' if r['data']['lastSale']['to_address'] == None else r['data']['lastSale']['to_address']
        timestamp = 'no data' if r['data']['lastSale']['timestamp'] == None else r['data']['lastSale']['timestamp']
        sale_price = 'no data' if r['data']['lastSale']['sale_price_in_eth'] == None else r['data']['lastSale']['sale_price_in_eth']
        #----------------------------------------------------------------------------------------------------------------------------------------------------------------
        url = f'https://api.traitsniper.com/v1/collections/{collection_contract_address}/nfts?token_ids={token_id}'
        headers = {
            'accept': 'application/json',
            'x-ts-api-key': os.getenv('TRAITSNIPER_API_KEY')
        }
        r = requests.get(url, headers=headers).json()
        print(r)
        if r['error'] != None:
            embed = discord.Embed(title='[ERROR]', description=f'`{r["error"]["message"]}`\n\nOther possible reasons:\nhttps://kizmeow.gitbook.io/kizmeow-nft-discord-bot/information/faq\nJoin support server to report the problem.\nhttps://discord.gg/PxNF9PaSKv', color=0xFFA46E)
            await ctx.respond(embed=embed, ephemeral=True)
            return

        rarity_rank = 'no data' if r['nfts'][0]['rarity_rank'] == None else r['nfts'][0]['rarity_rank']
        rarity_score = 'no data' if r['nfts'][0]['rarity_score'] == None else r['nfts'][0]['rarity_score']
        nft_traits = 'no data' if r['nfts'][0]['traits'] == None else r['nfts'][0]['traits']
        #----------------------------------------------------------------------------------------------------------------------------------------------------------------
        async def initial_embed():
            ipfs_button.url = nft_IPFS_image
            ipfs_button.custom_id = None
            view = View(timeout=None)
            view.add_item(rarity_button)
            view.add_item(lastSale_button)
            view.add_item(ipfs_button)
            
            embed = discord.Embed(title='', color=0xFFA46E)
            embed.set_image(url=nft_image)
            embed.set_author(name=f'{collection_name}#{token_id}', url=f'https://opensea.io/assets/{collection_contract_address}/{token_id}', icon_url=collection_image)
            embed.add_field(name='Owner', value=f'[{nft_owner[0:6]}](https://etherscan.io/address/{nft_owner})', inline=False)
            embed.add_field(name='Type', value=erc_type, inline=False)
            embed.timestamp = datetime.datetime.now()

            return (embed, view)

        (embed, view) = await initial_embed()
        await ctx.defer()
        await ctx.respond(embed=embed, view=view)
        #----------------------------------------------------------------------------------------------------------------------------------------------------------------
        async def return_button_callback(interaction):
            (embed, view) = await initial_embed()
            await interaction.response.edit_message(embed=embed, view=view)

        return_button.callback = return_button_callback
        #----------------------------------------------------------------------------------------------------------------------------------------------------------------   
        async def rarity_button_callback(interaction):
            embed = discord.Embed(title=f'{collection_name}#{token_id}', color=0xFFA46E)
            embed.set_image(url=nft_image)
            embed.add_field(name='Owner', value=f'[{nft_owner[0:6]}](https://etherscan.io/address/{nft_owner})', inline=False)
            embed.add_field(name='Rank', value=rarity_rank, inline=True)
            embed.add_field(name='Score', value=f'{rarity_score:.2f}', inline=True)
            embed.add_field(name='═════════════Traits═════════════', value='_ _', inline=False)

            for t in nft_traits:
                trait_name = t['name']
                trait_value = t['value']
                trait_score = t['score']
                embed.add_field(name=trait_name, value=f'{trait_value}\n`{trait_score:.2f}`', inline=True)

            embed.set_author(name=collection_name, url=f'https://opensea.io/assets/{collection_contract_address}/{token_id}', icon_url=collection_image)
            embed.timestamp = datetime.datetime.now()

            view = View(timeout=None)
            view.add_item(return_button)
            await interaction.response.edit_message(embed=embed, view=view)

        rarity_button.callback = rarity_button_callback
        #----------------------------------------------------------------------------------------------------------------------------------------------------------------   
        async def lastSale_button_callback(interaction):
            embed = discord.Embed(title=f'{collection_name}#{token_id}', color=0xFFA46E)
            embed.set_image(url=nft_image)
            embed.add_field(name='From', value=f'[{from_address[0:6]}](https://etherscan.io/address/{from_address})', inline=True)
            embed.add_field(name='To', value=f'[{to_address[0:6]}](https://etherscan.io/address/{to_address})', inline=True)
            embed.add_field(name='It was', value=f'<t:{timestamp}:R>', inline=True)
            embed.add_field(name='Sales Price', value=f'{sale_price} ETH', inline=True)
            embed.timestamp = datetime.datetime.now()

            view = View(timeout=None)
            view.add_item(return_button)
            await interaction.response.edit_message(embed=embed, view=view)

        lastSale_button.callback = lastSale_button_callback
        #----------------------------------------------------------------------------------------------------------------------------------------------------------------   
def setup(bot):
    bot.add_cog(nft(bot))