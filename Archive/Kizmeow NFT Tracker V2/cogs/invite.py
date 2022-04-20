import discord
from discord_slash import cog_ext
from core.cog_core import cogcore

class invite(cogcore):
  @cog_ext.cog_slash(name="invite",description="invite bot to your server")
  async def invite(self,ctx):
    embed=discord.Embed(title="**[bot invite link]**", description="https://discord.com/api/oauth2/authorize?client_id=886198731328868402&permissions=534727097920&scope=bot%20applications.commands", color=0xe8006f)
    await ctx.send(embed = embed)

def setup(bot):
  bot.add_cog(invite(bot))
