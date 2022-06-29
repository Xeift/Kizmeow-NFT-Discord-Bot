import datetime

import discord
from discord.commands import Option
from discord.commands import slash_command
from discord.ext import commands
from discord.ui import Button, View
from opensea import OpenseaAPI


class project_nft(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @slash_command(name='project_nft', description='display information of specific NFT')
    async def project_nft(
            self,
            ctx: discord.ApplicationContext,
            contract_address: Option(str, 'smart contract address of the project'),
            token_id: Option(str, 'token id of the NFT')
    ):
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

        if info['description'] == None:
            description = 'no data'
        else:
            description = info['description']

        if info['collection']['primary_asset_contracts'][0]['external_link'] == None:
            external_link = 'no data'
        else:
            external_link = info['collection']['primary_asset_contracts'][0]['external_link']

        if info['collection']['primary_asset_contracts'][0]['schema_name'] == None:
            schema_name = 'no data'
        else:
            schema_name = info['collection']['primary_asset_contracts'][0]['schema_name']

        if info['permalink'] == None:
            permalink = 'no data'
        else:
            permalink = info['permalink']

        button1 = Button(label='Official website', style=discord.ButtonStyle.link,
                         url=external_link)
        button2 = Button(label='Original resolution image', style=discord.ButtonStyle.link,
                         url=image_url)
        view = View()
        view.add_item(button1)
        view.add_item(button2)

        embed = discord.Embed(title='**' + name + '**', url=permalink, color=0xFFA46E)
        embed.set_image(url=image_url)
        embed.add_field(name='Owner', value='`' + top_ownerships + '`', inline=True)
        embed.add_field(name='Token type', value='`' + schema_name + '`', inline=True)
        embed.add_field(name='Description', value='`' + description + '`', inline=False)
        embed.timestamp = datetime.datetime.now()
        embed.set_footer(text=name)

        await ctx.respond(embed=embed, view=view)


def setup(bot):
    bot.add_cog(project_nft(bot))
