import discord
import datetime
from discord.ext import commands
from discord.commands import slash_command
from discord.ui import Button, View


class help(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @slash_command(name='help', description='Display help message')
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
        github_button = Button(label='GitHub', style=discord.ButtonStyle.link, emoji='<:github_icon:1048426748330639360>')
        github_button.url = 'https://github.com/Xeift/Kizmeow-NFT-Discord-Bot'
        github_button.custom_id = None

        view = View(timeout=None)
        view.add_item(gitbook_button)
        view.add_item(invite_button)
        view.add_item(github_button)

        embed = discord.Embed(title='Help', description='**__Click below buttons to join support server, read the doc or visit the repository UwU.__**', color=0xFFA46E)
        embed.set_footer(text='Data provided by Kizmeow NFT Bot', icon_url='https://user-images.githubusercontent.com/80938768/204983971-d7cf0e40-f4ce-4737-ba07-85ed62112dab.png')
        embed.timestamp = datetime.datetime.now()
        await ctx.respond(embed=embed, view=view)

def setup(bot):
    bot.add_cog(help(bot))