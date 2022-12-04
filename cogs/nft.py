import re
import os
import json
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

    def collection_name_autocomplete(self: discord.AutocompleteContext):
        with open('collection_name_autocomplete.json','r') as of:
            collection_name_data = json.load(of)
        return collection_name_data.keys()

    @slash_command(name='nft', description='View NFT information')
    async def nft(
        self,
        ctx: discord.ApplicationContext,
        collection: Option(str, 'Specify the collection slug', autocomplete=collection_name_autocomplete),
        token_id: Option(str, 'Enter the token id')
    ):
        #----------------------------------------------------------------------------------------------------------------------------------------------------------------
        with open('collection_name_autocomplete.json', 'r') as of:
            collection_name_data = json.load(of)
        if collection in collection_name_data:
            collection = collection_name_data[collection]
        #----------------------------------------------------------------------------------------------------------------------------------------------------------------
        rarity_button = Button(label='Rarity', style=discord.ButtonStyle.blurple, emoji='💎')
        lastSale_button = Button(label='Last Sale', style=discord.ButtonStyle.green, emoji='💳')
        ipfs_button = Button(label='IPFS', style=discord.ButtonStyle.link, emoji='🧊')
        return_button = Button(label='EXIT', style=discord.ButtonStyle.red)
        gitbook_button = Button(label='GitBook', style=discord.ButtonStyle.link, emoji='<:gitbook_button:1047912317427400704>')
        gitbook_button.url = 'https://kizmeow.gitbook.io/kizmeow-nft-discord-bot/information/faq'
        gitbook_button.custom_id = None
        invite_button = Button(label='Kizmeow Support Server', style=discord.ButtonStyle.link, emoji='<:kizmeow:1047912736224448562>')
        invite_button.url = 'https://discord.gg/PxNF9PaSKv'
        invite_button.custom_id = None
        #----------------------------------------------------------------------------------------------------------------------------------------------------------------
        load_dotenv()
        url = f'https://api.modulenft.xyz/api/v2/eth/nft/token?slug={collection}&tokenId={token_id}'
        headers = {
            'accept': 'application/json',
            'X-API-KEY': os.getenv('MODULE_API_KEY')
        }
        r = requests.get(url=url, headers=headers).json()

        if r['error'] != None:
            view = View(timeout=None, )
            view.add_item(gitbook_button)
            view.add_item(invite_button)
            embed = discord.Embed(title='[ERROR]', description=f'`{r["error"]["message"]}`\n\nOther possible reasons:\nhttps://kizmeow.gitbook.io/kizmeow-nft-discord-bot/information/faq\nJoin support server to report the problem.\nhttps://discord.gg/PxNF9PaSKv', color=0xFFA46E)
            await ctx.respond(embed=embed, view=view, ephemeral=True)
            return

        collection_name = 'no data' if r['data']['collection']['name'] == None else r['data']['collection']['name']
        nft_image = 'https://i.imgur.com/aSSH1jL.gif' if r['data']['metadata'] == {} else r['data']['metadata']['image']
        nft_image = re.sub('ipfs://', 'https://ipfs.io/ipfs/', nft_image)
        nft_owner = '0x0000000000000000000000000000000000000000' if r['data']['owner'] == {} else r['data']['owner']['owner']
        collection_image = 'https://i.imgur.com/aSSH1jL.gif' if r['data']['collection']['images']['image_url'] == None else r['data']['collection']['images']['image_url']
        collection_contract_address = 'no data' if r['data']['collection']['contractAddress'] == None else r['data']['collection']['contractAddress']
        nft_IPFS_image = 'https://i.imgur.com/aSSH1jL.gif' if r['data']['metadata'] == {} else r['data']['metadata']['image']
        nft_IPFS_image = re.sub('ipfs://', 'https://ipfs.io/ipfs/', nft_IPFS_image)
        erc_type = 'no data' if r['data']['collection']['ercType'] == None else r['data']['collection']['ercType']

        if r['data']['lastSale'] == {}:
            last_sale_exist = False
        else:
            last_sale_exist = True
            from_address = r['data']['lastSale']['from_address']
            to_address = r['data']['lastSale']['to_address']
            timestamp = r['data']['lastSale']['timestamp']
            sale_price = r['data']['lastSale']['sale_price_in_eth']
        #----------------------------------------------------------------------------------------------------------------------------------------------------------------
        url = f'https://api.traitsniper.com/v1/collections/{collection_contract_address}/nfts?token_ids={token_id}'
        headers = {
            'accept': 'application/json',
            'x-ts-api-key': os.getenv('TRAITSNIPER_API_KEY')
        }
        r = requests.get(url, headers=headers).json()

        if 'code' in r:
            if r['code'] == 'error':
                traitsniper_available = False
        else:
            traitsniper_available = True

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
            embed.add_field(name='Owner', value=f'[{nft_owner[0:6]}](https://etherscan.io/address/{nft_owner})', inline=True)
            embed.add_field(name='Type', value=erc_type, inline=True)
            embed.set_footer(text='Data provided by Kizmeow NFT Bot', icon_url='https://user-images.githubusercontent.com/80938768/204983971-d7cf0e40-f4ce-4737-ba07-85ed62112dab.png')
            embed.timestamp = datetime.datetime.now()

            return (embed, view)

        (embed, view) = await initial_embed()

        await ctx.defer()
        await ctx.respond(embed=embed, view=view)
        #----------------------------------------------------------------------------------------------------------------------------------------------------------------
        async def return_button_callback(interaction):
            if ctx.author == interaction.user:
                (embed, view) = await initial_embed()
                await interaction.response.edit_message(embed=embed, view=view)
            else:
                embed = discord.Embed(title='Consider use `/nft` command by yourself.', color=0xFFA46E)
                await interaction.response.send_message(embed=embed, ephemeral=True)
        return_button.callback = return_button_callback
        #----------------------------------------------------------------------------------------------------------------------------------------------------------------
        async def rarity_button_callback(interaction):
            if ctx.author == interaction.user:
                if traitsniper_available:
                    embed = discord.Embed(title=f'{collection_name}#{token_id}', color=0xFFA46E)
                    embed.set_image(url=nft_image)
                    embed.add_field(name='Owner', value=f'[{nft_owner[0:6]}](https://etherscan.io/address/{nft_owner})', inline=False)
                    embed.add_field(name='Rank', value=rarity_rank, inline=True)
                    embed.add_field(name='Score', value=f'{rarity_score:.2f}', inline=True)
                    embed.set_author(name=collection_name, url=f'https://opensea.io/assets/{collection_contract_address}/{token_id}', icon_url=collection_image)
                    embed.set_footer(text='Data provided by Kizmeow NFT Bot', icon_url='https://user-images.githubusercontent.com/80938768/204983971-d7cf0e40-f4ce-4737-ba07-85ed62112dab.png')
                    embed.add_field(name='═════════════Traits═════════════', value='_ _', inline=False)

                    for t in nft_traits:
                        trait_name = t['name']
                        trait_value = t['value']
                        trait_score = t['score']
                        embed.add_field(name=trait_name, value=f'{trait_value}\n`{trait_score:.2f}`', inline=True)
                        embed.timestamp = datetime.datetime.now()
                else:
                    embed = discord.Embed(title=f'{collection_name} is not available on traitsniper.', color=0xFFA46E)
                    embed.set_author(name=collection_name, url=f'https://opensea.io/assets/{collection_contract_address}/{token_id}', icon_url=collection_image)
                    embed.set_footer(text='Data provided by Kizmeow NFT Bot', icon_url='https://user-images.githubusercontent.com/80938768/204983971-d7cf0e40-f4ce-4737-ba07-85ed62112dab.png')
                    embed.timestamp = datetime.datetime.now()

                view = View(timeout=None)
                view.add_item(return_button)
                await interaction.response.edit_message(embed=embed, view=view)
            else:
                embed = discord.Embed(title='Consider use `/nft` command by yourself.', color=0xFFA46E)
                await interaction.response.send_message(embed=embed, ephemeral=True)
        rarity_button.callback = rarity_button_callback
        #----------------------------------------------------------------------------------------------------------------------------------------------------------------
        async def lastSale_button_callback(interaction):
            if ctx.author == interaction.user:
                if last_sale_exist:
                    embed = discord.Embed(title=f'{collection_name}#{token_id}', color=0xFFA46E)
                    embed.set_image(url=nft_image)
                    embed.add_field(name='From', value=f'[{from_address[0:6]}](https://etherscan.io/address/{from_address})', inline=True)
                    embed.add_field(name='To', value=f'[{to_address[0:6]}](https://etherscan.io/address/{to_address})', inline=True)
                    embed.add_field(name='It was', value=f'<t:{timestamp}:R>', inline=True)
                    embed.add_field(name='Sales Price', value=f'{sale_price} ETH', inline=True)
                    embed.set_author(name=collection_name, url=f'https://opensea.io/assets/{collection_contract_address}/{token_id}', icon_url=collection_image)
                    embed.set_footer(text='Data provided by Kizmeow NFT Bot', icon_url='https://user-images.3ubusercontent.com/80938768/204983971-d7cf0e40-f4ce-4737-ba07-85ed62112dab.png')
                    embed.timestamp = datetime.datetime.now()
                else:
                    embed = discord.Embed(title=f'{collection_name}#{token_id} is never sold', color=0xFFA46E)
                    embed.set_author(name=collection_name, url=f'https://opensea.io/assets/{collection_contract_address}/{token_id}', icon_url=collection_image)
                    embed.set_footer(text='Data provided by Kizmeow NFT Bot', icon_url='https://user-images.githubusercontent.com/80938768/204983971-d7cf0e40-f4ce-4737-ba07-85ed62112dab.png')
                    embed.timestamp = datetime.datetime.now()
                view = View(timeout=None)
                view.add_item(return_button)
                await interaction.response.edit_message(embed=embed, view=view)
            else:
                embed = discord.Embed(title='Consider use `/nft` command by yourself.', color=0xFFA46E)
                await interaction.response.send_message(embed=embed, ephemeral=True)
        lastSale_button.callback = lastSale_button_callback
        #----------------------------------------------------------------------------------------------------------------------------------------------------------------
def setup(bot):
    bot.add_cog(nft(bot))