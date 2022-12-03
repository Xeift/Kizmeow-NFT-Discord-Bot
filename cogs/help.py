import discord
import datetime
from discord.ext import commands
from discord.commands import slash_command
from discord.ui import Button, View


class help(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @slash_command(name='help', description='display help message')
    async def help(
        self,
        ctx: discord.ApplicationContext
    ):
        gitbook_button = Button(label='GitBook', style=discord.ButtonStyle.link, emoji='<:gitbook_button:1047912317427400704>')
        gitbook_button.url = 'https://kizmeow.gitbook.io/kizmeow-nft-discord-bot/information/faq'
        gitbook_button.custom_id = None
        invite_button = Button(label='Kizmeow Support Server', style=discord.ButtonStyle.link, emoji='<:kizmeow:1047912736224448562>')
        invite_button.url = 'https://discord.gg/PxNF9PaSKv'
        invite_button.custom_id = None

        view = View(timeout=None)
        view.add_item(gitbook_button)
        view.add_item(invite_button)
        embed = discord.Embed(title='help', description='Click below button to join support server or read the doc UwU.', color=0xFFA46E)
        await ctx.respond(embed=embed, view=view, ephemeral=True)

def setup(bot):
    bot.add_cog(help(bot))