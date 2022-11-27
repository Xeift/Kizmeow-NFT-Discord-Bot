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
        
    @commands.slash_command(name='nft', description='View NFT information')
    async def nft(
            self,
            ctx: discord.ApplicationContext,
            collection: Option(str, 'Specify the collection slug'),
            token_id: Option(str, 'Enter the token number')
    ):
        #----------------------------------------------------------------------------------------------------------------------------------------------------------------
        rarityButton = Button(label='Rarity💎', style=discord.ButtonStyle.blurple)
        lastSaleButton = Button(label='Last Sale💳', style=discord.ButtonStyle.green)
        ipfsButton = Button(label='IPFS🧊', style=discord.ButtonStyle.link)
        returnButton = Button(label='EXIT', style=discord.ButtonStyle.red)
        #----------------------------------------------------------------------------------------------------------------------------------------------------------------
        load_dotenv()
        url = f'https://api.modulenft.xyz/api/v2/eth/nft/token?slug={collection}&tokenId={token_id}'
        headers = {
            'accept': 'application/json',
            'X-API-KEY': os.getenv('MODULE_API_KEY')
        }
        r = requests.get(url=url, headers=headers).json()

        collectionName = 'no dara' if r['data']['collection']['name'] == None else r['data']['collection']['name']
        nftImage = 'no data' if r['data']['metadata']['image_cached'] == None else r['data']['metadata']['image_cached']
        nftOwner = 'no data' if r['data']['owner']['owner'] == None else r['data']['owner']['owner']
        collectionImage = 'https://imgur.com/aSSH1jL' if r['data']['collection']['images']['image_url'] == None else r['data']['collection']['images']['image_url']
        collectionContractAddress = 'no data' if r['data']['collection']['contractAddress'] == None else r['data']['collection']['contractAddress']
        nftIPFSImage = 'https://imgur.com/aSSH1jL' if r['data']['metadata']['image'] == None else r['data']['metadata']['image']
        nftIPFSImage = re.sub('ipfs://', 'https://ipfs.io/ipfs/', nftIPFSImage)
        ercType = 'no data' if r['data']['collection']['ercType'] == None else r['data']['collection']['ercType']

        fromAddress = 'no data' if r['data']['lastSale']['from_address'] == None else r['data']['lastSale']['from_address']
        toAddress = 'no data' if r['data']['lastSale']['to_address'] == None else r['data']['lastSale']['to_address']
        timestamp = 'no data' if r['data']['lastSale']['timestamp'] == None else r['data']['lastSale']['timestamp']
        salePrice = 'no data' if r['data']['lastSale']['sale_price_in_eth'] == None else r['data']['lastSale']['sale_price_in_eth']
        #----------------------------------------------------------------------------------------------------------------------------------------------------------------
        url = f'https://api.traitsniper.com/v1/collections/{collectionContractAddress}/nfts?token_ids={token_id}'
        print(collectionContractAddress)
        print(token_id)
        headers = {
            'accept': 'application/json',
            'x-ts-api-key': os.getenv('TRAITSNIPER_API_KEY')
        }
        r = requests.get(url, headers=headers).json()

        rarityRank = 'no data' if r['nfts'][0]['rarity_rank'] == None else r['nfts'][0]['rarity_rank']
        rarityScore = 'no data' if r['nfts'][0]['rarity_score'] == None else r['nfts'][0]['rarity_score']
        nftTraits = 'no data' if r['nfts'][0]['traits'] == None else r['nfts'][0]['traits']
        #----------------------------------------------------------------------------------------------------------------------------------------------------------------
        async def initialEmbed():
            ipfsButton.url = nftIPFSImage
            ipfsButton.custom_id = None
            view = View(timeout=None)
            view.add_item(rarityButton)
            view.add_item(lastSaleButton)
            view.add_item(ipfsButton)
            
            embed = discord.Embed(title=f'{collectionName}#{token_id}', color=0xFFA46E)
            embed.set_image(url=nftImage)
            embed.set_author(name=collectionName, url=f'https://opensea.io/assets/{collectionContractAddress}/{token_id}', icon_url=collectionImage)
            embed.add_field(name='Owner', value=f'[{nftOwner[0:6]}](https://etherscan.io/address/{nftOwner})', inline=False)
            embed.add_field(name='Type', value=ercType, inline=False)
            embed.timestamp = datetime.datetime.now()

            return (embed, view)

        (embed, view) = await initialEmbed()
        await ctx.respond(embed=embed, view=view)
        #----------------------------------------------------------------------------------------------------------------------------------------------------------------
        async def rarityButtonCallback(interaction):
            embed = discord.Embed(title=f'{collectionName}#{token_id}', color=0xFFA46E)
            embed.set_image(url=nftImage)
            embed.add_field(name='Owner', value=f'[{nftOwner[0:6]}](https://etherscan.io/address/{nftOwner})', inline=False)
            embed.add_field(name='Rank', value=rarityRank, inline=True)
            embed.add_field(name='Score', value=f'{rarityScore:.2f}', inline=True)
            embed.add_field(name='═════════════Traits═════════════', value='_ _', inline=False)

            for t in nftTraits:
                nameTrait = t['name']
                valueTrait = t['value']
                scoreTrait = t['score']
                embed.add_field(name=nameTrait, value=f'{valueTrait}\n`{scoreTrait:.2f}`', inline=True)

            embed.set_author(name=collectionName, url=f'https://opensea.io/assets/{collectionContractAddress}/{token_id}', icon_url=collectionImage)
            embed.timestamp = datetime.datetime.now()

            view = View(timeout=None)
            view.add_item(returnButton)
            await interaction.response.edit_message(embed=embed, view=view)

        rarityButton.callback = rarityButtonCallback
        #----------------------------------------------------------------------------------------------------------------------------------------------------------------   
        async def lastSaleButtonCallback(interaction):
            embed = discord.Embed(title=f'{collectionName}#{token_id}', color=0xFFA46E)
            embed.set_image(url=nftImage)
            embed.add_field(name='From', value=f'[{fromAddress[0:6]}](https://etherscan.io/address/{fromAddress})', inline=True)
            embed.add_field(name='To', value=f'[{toAddress[0:6]}](https://etherscan.io/address/{toAddress})', inline=True)
            embed.add_field(name='It was', value=f'<t:{timestamp}:R>', inline=True)
            embed.add_field(name='Sales Price', value=f'{salePrice} ETH', inline=True)
            embed.timestamp = datetime.datetime.now()

            view = View(timeout=None)
            view.add_item(returnButton)
            await interaction.response.edit_message(embed=embed, view=view)

        lastSaleButton.callback = lastSaleButtonCallback
        #----------------------------------------------------------------------------------------------------------------------------------------------------------------   
        async def returnButtonCallback(interaction):
            (embed, view) = await initialEmbed()
            await interaction.response.edit_message(embed=embed, view=view)

        returnButton.callback = returnButtonCallback
        #----------------------------------------------------------------------------------------------------------------------------------------------------------------   
def setup(bot):
    bot.add_cog(nft(bot))