
from discord import (ApplicationContext, Embed, IntegrationType,
                     InteractionContextType, Option)
from discord.ext import commands

from api.get_os_account import get_os_account


class opensea_account(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(
        name='opensea_account',
        description='View account details of a specific OpenSea account',
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
            str, 'EVM address(ENS supported) or username on OpenSea')
    ):
        (success, account_data) = get_os_account(address_or_username)
        embed = Embed(color=0xFFA46E)
        if success:
            embed.title = f'OpenSea Account Info of {
                account_data['address'][:7]}'
            embed.set_thumbnail(url=account_data['profile_image_url'])
            embed.set_image(url=account_data['banner_image_url'])
            embed.set_footer(
                text='Source: OpenSea API',
                icon_url='https://raw.githubusercontent.com/Xeift/Kizmeow-NFT-Discord-Bot/refs/heads/main/V3/access/x2y2_logo.png'
            )

            embed.add_field(
                name='Address', value=account_data['address'], inline=False)
            embed.add_field(name='Username',
                            value=account_data['username'], inline=True)
            embed.add_field(
                name='Bio', value=account_data['bio'], inline=True)
            embed.add_field(name='Joined Date',
                            value=account_data['joined_date'], inline=True)
        else:
            embed.title = '[Failed]'
            embed.description = f'Command execution failed. Reason:\n```{
                account_data}```'

        await ctx.respond(embed=embed)


def setup(bot):
    bot.add_cog(opensea_account(bot))
