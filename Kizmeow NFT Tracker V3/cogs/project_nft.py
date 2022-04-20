import discord
from discord.commands import slash_command
from discord.ext import commands
from discord.commands import Option
import os
import json
import urllib.request as ur
from core.cog_core import cogcore
from discord.ui import Button,View

class project_nft(commands.Cog):
    @slash_command(name='project_nft',description='display information of specific NFT')
    async def project_nft(
        self,
        ctx: discord.ApplicationContext,
        contract_address: Option(str, 'smart contract address of the project'),
        token_id: Option(str, 'token id of the NFT')
    ):
        req = ur.Request(url='https://api.opensea.io/api/v1/asset/'+contract_address+'/'+token_id+'/?format=json',headers={'User-Agent': 'Mozilla/5.0'})
        api0 = json.loads(ur.urlopen(req).read().decode())

        if api0['name'] == None:
            name = 'no data'
        else:
            name = api0['name']
        
        if api0['image_original_url'] == None:
            image_original_url = 'no data'
        else:
            image_original_url = api0['image_original_url']

        if api0['image_thumbnail_url'] == None:
            image_thumbnail_url = 'no data'
        else:
            image_thumbnail_url = api0['image_thumbnail_url']

        if api0['top_ownerships'][0]['owner']['user'] == None:
            top_ownerships = 'no data'
        else:
            top_ownerships = api0['top_ownerships'][0]['owner']['user']['username']

        if api0['description'] == None:
            description = 'no data'
        else:
            description = api0['description']

        if api0['collection']['primary_asset_contracts'][0]['external_link'] == None:
            external_link = 'no data'
        else:
            external_link = api0['collection']['primary_asset_contracts'][0]['external_link']

        if api0['collection']['primary_asset_contracts'][0]['schema_name'] == None:
            schema_name = 'no data'
        else:
            schema_name = api0['collection']['primary_asset_contracts'][0]['schema_name']

        if api0['token_id'] == None:
            token_id1 = 'no data'
        else:
            token_id1 = api0['token_id']

        if api0['permalink'] == None:
            permalink = 'no data'
        else:
            permalink = api0['permalink']

        button = Button(label='Download original resolution image', style=discord.ButtonStyle.link, url=image_original_url)
        view = View()
        view.add_item(button)

        embed=discord.Embed(title='project NFT', color=0xFFA46E)
        embed.set_thumbnail(url=image_thumbnail_url)
        embed.add_field(name='token id' , value=token_id1, inline=False) 
        embed.add_field(name='description' , value=description, inline=False)     
        embed.add_field(name='official website' , value=external_link, inline=False) 
        embed.add_field(name='token type' , value=schema_name, inline=False) 
        embed.add_field(name='owner' , value=top_ownerships, inline=False)
        embed.add_field(name='OpenSea' , value=permalink, inline=False)
        embed.add_field(name='original resolution image' , value=image_original_url, inline=False)
        
        await ctx.respond(embed=embed,view=view)
def setup(bot):
    bot.add_cog(project_nft(bot))