
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

        # TODO: get collection
        (success, account_data) = get_os_account(collection)
        embed = Embed(color=0xFFA46E)
        view = View()
        success = True

        if success:
            await ctx.respond(collection)

        else:
            embed.title = '[Failed]'
            embed.description = f'Command execution failed. Reason:\n```{
                account_data}```'

            await ctx.respond(embed=embed, view=view)


def setup(bot):
    bot.add_cog(opensea_collection(bot))
