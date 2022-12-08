import discord
from discord.ext import commands
from discord.commands import slash_command


class reload_cmds(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @slash_command(guild_ids=[1041165809013243924], name='reload_cmds', description='reload cmds [for debug]')
    async def reload_cmds(
            self,
            ctx: discord.ApplicationContext,
    ):
        if ctx.author.id == 510830627893805069 or ctx.author.id == 874806243208871977:
            extensions = [  # load cogs
                # --------------------system commands
                'cogs.ping',
                'cogs.help',
                'cogs.feedback',
                # --------------------system commands

                # --------------------Web3 commands
                'cogs.gas',
                'cogs.eth',
                # --------------------Web3 commands

                # --------------------NFT commands
                'cogs.collection',
                'cogs.nft'
                # --------------------NFT commands
            ]
            for extension in extensions:
                self.bot.unload_extension(extension)
                self.bot.load_extension(extension)

            await ctx.respond('reload complete', ephemeral=True)
        else:
            await ctx.respond('[PERMISSION DENIED] only owner can use this command', ephemeral=True)


def setup(bot):
    bot.add_cog(reload_cmds(bot))
