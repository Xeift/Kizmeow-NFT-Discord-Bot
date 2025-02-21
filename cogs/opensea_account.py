from discord import (ApplicationContext, ButtonStyle, Embed, IntegrationType,
                     InteractionContextType, Option, PartialEmoji)
from discord.ext import commands
from discord.ui import Button, View

from api.get_os_account import get_os_account
from embed.err_embed import general_err_embed
from embed.opensea_account_embed import opensea_account_embed
from utils.load_config import load_config_from_json
from view.opensea_account_view import opensea_account_view


class opensea_account(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(
        name='opensea_account',
        description='View the details of a specific OpenSea account.',
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
    async def opensea_account(
        self,
        ctx: ApplicationContext,
        address_or_username: Option(
            str,
            'EVM address (ENS supported) or OpenSea username.'
        )
    ):
        await ctx.defer()
        
        mid = str(ctx.author.id)
        (enable_link_button, _, visibility, _, _) = load_config_from_json(mid)
        disable_link_button = not enable_link_button
        (success, account_data) = get_os_account(address_or_username)
        embed = Embed()
        view = View()

        if success:
            embed = opensea_account_embed(account_data)
            view = opensea_account_view(account_data, view, disable_link_button)

        else:
            embed = general_err_embed(account_data)

        await ctx.respond(embed=embed, view=view, ephemeral=not visibility)


def setup(bot):
    bot.add_cog(opensea_account(bot))
