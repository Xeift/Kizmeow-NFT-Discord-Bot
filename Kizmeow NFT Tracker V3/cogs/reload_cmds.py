import os
import discord
import datetime
from etherscan import Etherscan
from dotenv import load_dotenv
from discord.ext import commands


class reload_cmds(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(name='r', description='reload cmds [for debug]')
    async def reload_cmds(
            self,
            ctx: discord.ApplicationContext,
    ):
        extensions = [  # load cogs
            # --------------------system commands
            'cogs.ping',
            'cogs.help',
            # --------------------system commands

            # --------------------etherscan commands
            'cogs.gas',
            'cogs.eth',
            # --------------------etherscan commands

            # --------------------NFT commands
            'cogs.project',
            'cogs.nft'
            # --------------------NFT commands
        ]
        for extension in extensions:
            self.bot.unload_extension(extension)
            self.bot.load_extension(extension)

        await ctx.respond('reload complete', ephemeral=True)

def setup(bot):
    bot.add_cog(reload_cmds(bot))
