import discord
from discord.commands import slash_command
from discord.ext import commands
from core.cog_core import cogcore
from discord.ui import Button,View

class invite(cogcore):
    @slash_command(name='invite',description='invite bot to your server')
    async def invite(
        self,
        ctx: discord.ApplicationContext
    ):
      button = Button(label='bot invite link', style=discord.ButtonStyle.link, url='https://discord.com/api/oauth2/authorize?client_id=923512417907015693&permissions=277025508352&scope=applications.commands%20bot')
      view = View()
      view.add_item(button)
      embed=discord.Embed(title='**[invite]**', description='click the button below to invite bot to your server', color=0xFFA46E)
      await ctx.respond(embed = embed, view = view)

def setup(bot):
  bot.add_cog(invite(bot))