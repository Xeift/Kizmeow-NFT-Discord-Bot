
import json

from discord import (ApplicationContext, AutocompleteContext, ButtonStyle,
                     Embed, IntegrationType, InteractionContextType, Option,
                     PartialEmoji)
from discord.ext import commands
from discord.ui import Button, View

from api.get_os_collection import get_os_collection


class opensea_collection(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    def collection_name_autocomplete(self: AutocompleteContext):
        with open('collection_name_autocomplete.json', 'r') as of:
            collection_name_data = json.load(of)
        return collection_name_data.keys()

    @commands.slash_command(
        name='opensea_collection',
        description='View details of a specific OpenSea NFT collection',
        integration_types=[
            IntegrationType.user_install,
            IntegrationType.guild_install,
        ],
        contexts=[
            InteractionContextType.guild,
            InteractionContextType.bot_dm,
            InteractionContextType.private_channel,
        ],
    )
    async def opensea_collection(
        self,
        ctx: ApplicationContext,
        collection: Option(
            str,
            'Specify the collection slug',
            autocomplete=collection_name_autocomplete
        )
    ):
        await ctx.defer()

        with open('collection_name_autocomplete.json','r') as of:
            collection_name_data = json.load(of)
        if collection in collection_name_data:
            collection = collection_name_data[collection]
        
        (success, collection_data) = get_os_collection(collection)


        embed = Embed(color=0xFFA46E)
        view = View()

        if success:
            name = collection_data['name']
            description = collection_data['description']
            supply = collection_data['total_supply']
            category = collection_data['category']
            created_date = collection_data['created_date']
            owner_address = collection_data['owner']
            owner_address_short = collection_data['owner'][:7]
            owner_etherscan_url = f'https://etherscan.io/address/{owner_address}'
            owner_opensea_url = f'https://opensea.io/{owner_address}'
            # fee = # TODO:
            verify_state = collection_data['safelist_status']
            pfp_img = collection_data['image_url']
            banner_img = collection_data['banner_image_url']
            



            print(description)

        else:
            embed.title = '[Failed]'
            embed.description = f'Command execution failed. Reason:\n```{
                collection_data}```'

        # await ctx.respond(embed=embed, view=view)
        embed.add_field(name='test', value='>>> asdf\ntest\nbaslsasa')
        await ctx.respond(embed=embed)


def setup(bot):
    bot.add_cog(opensea_collection(bot))
