import discord
import datetime
from discord.commands import slash_command
from discord.ext import commands
from discord.ui import Button, View


class invite(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @slash_command(name='invite', description='invite bot to your server')
    async def invite(
            self,
            ctx: discord.ApplicationContext
    ):
        button = Button(label='bot invite link', style=discord.ButtonStyle.link,
                        url='https://discord.com/api/oauth2/authorize?client_id=923512417907015693&permissions'
                            '=277025508352&scope=applications.commands%20bot')
        view = View()
        view.add_item(button)
        embed = discord.Embed(title='**Invite**', description='**Click the button below to invite bot to your server**',
                              color=0xFFA46E)
        embed.set_thumbnail(url='https://user-images.githubusercontent.com/80938768/146544100-315cdd44-7461-441b-a3dd'
                                '-d3ee653b145a.png')
        embed.timestamp = datetime.datetime.now()
        await ctx.respond(embed=embed, view=view)


def setup(bot):
    bot.add_cog(invite(bot))
