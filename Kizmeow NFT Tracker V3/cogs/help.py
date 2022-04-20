from certifi import contents
import discord
from discord.commands import slash_command
from discord.ext import commands
from core.cog_core import cogcore
from discord.ui import Button,View

class help(cogcore):
    @slash_command(name='help',description='display help message')
    async def help(
        self,
        ctx: discord.ApplicationContext
    ):
      #----------------------------------------------------------------------------------------------------buttons
      b_bot_info = Button(label='bot info', style=discord.ButtonStyle.blurple)
      b_system_commands = Button(label='system commands', style=discord.ButtonStyle.blurple)
      b_nft_commands = Button(label='NFT commands', style=discord.ButtonStyle.blurple)
      b_return = Button(style=discord.ButtonStyle.gray,emoji='↩️')
      #----------------------------------------------------------------------------------------------------buttons

      # callback
      #----------------------------------------------------------------------------------------------------return callback
      async def b_return_callback(interaction):
        view = View()

        view.add_item(b_bot_info)
        view.add_item(b_system_commands)
        view.add_item(b_nft_commands)
        view.add_item(b_return)

        embed=discord.Embed(title='**[help]**', description='click the button below to select different section', color=0xFFA46E)
        embed.add_field(name='bot info',value='information about the bot',inline=False)
        embed.add_field(name='system commands',value='list of system commands',inline=False)
        embed.add_field(name='NFT commands',value='list of NFT commands',inline=False)
        await interaction.response.edit_message(embed=embed,view=view)
      b_return.callback = b_return_callback
      #----------------------------------------------------------------------------------------------------return callback

      #----------------------------------------------------------------------------------------------------bot info callback
      async def b_bot_info_callback(interaction):
        embed=discord.Embed(title='**[bot info]**', description='', color=0xFFA46E)
        embed.add_field(name='bot name',value='Kizmeow NFT Tracker V3#2184',inline=False)
        embed.add_field(name='developer',value='Xeift#1230',inline=False)
        embed.add_field(name='bot avatar illustrator',value='Kiyue',inline=False)
        embed.add_field(name='programming language', value='Python', inline=False)
        b_github = Button(label='GitHub',style=discord.ButtonStyle.link,url='https://github.com/Xeift/Kizmeow-OpenSea-and-Etherscan-Discord-Bot')
        view = View()
        view.add_item(b_github)
        view.add_item(b_return)
        await interaction.response.edit_message(embed=embed,view=view)
      b_bot_info.callback = b_bot_info_callback
      #----------------------------------------------------------------------------------------------------bot info callback

      #----------------------------------------------------------------------------------------------------system commands callback
      async def b_system_commands_callback(interaction):
        embed=discord.Embed(title='**[system commands]**', description='', color=0xFFA46E)
        embed.add_field(name='`/help`',value='display this message',inline=False)
        embed.add_field(name='`/meow`',value='return bot latency',inline=False)
        embed.add_field(name='`/invite`',value='invite Kizmeow to your server',inline=False)
        # b_github = Button(label='GitHub',style=discord.ButtonStyle.link,url='https://github.com/Xeift/Kizmeow-OpenSea-and-Etherscan-Discord-Bot')
        view = View()
        # view.add_item(b_github)
        view.add_item(b_return)
        await interaction.response.edit_message(embed=embed,view=view)
      b_system_commands.callback = b_system_commands_callback
      #----------------------------------------------------------------------------------------------------system commands callback

      #----------------------------------------------------------------------------------------------------NFT commands callback
      async def b_nft_commands_callback(interaction):
        embed=discord.Embed(title='**[NFT commands]**', description='', color=0xFFA46E)
        embed.add_field(name='`/project_realtime`',value='display project realtime information',inline=False)
        embed.add_field(name='`/project_history`',value='display project history information',inline=False)
        embed.add_field(name='`/project_nft`', value='display information of specific NFT', inline=False)
        # b_github = Button(label='GitHub',style=discord.ButtonStyle.link,url='https://github.com/Xeift/Kizmeow-OpenSea-and-Etherscan-Discord-Bot')
        view = View()
        # view.add_item(b_github)
        view.add_item(b_return)
        await interaction.response.edit_message(embed=embed,view=view)
      b_nft_commands.callback = b_nft_commands_callback
      #----------------------------------------------------------------------------------------------------NFT commands callback      

      #----------------------------------------------------------------------------------------------------default buttons
      view = View()

      view.add_item(b_bot_info)
      view.add_item(b_system_commands)
      view.add_item(b_nft_commands)
      view.add_item(b_return)
      #----------------------------------------------------------------------------------------------------default buttons

      #----------------------------------------------------------------------------------------------------default embed
      embed=discord.Embed(title='**[help]**', description='click the button below to select different section', color=0xFFA46E)
      embed.add_field(name='bot info',value='information about the bot',inline=False)
      embed.add_field(name='system commands',value='list of system commands',inline=False)
      embed.add_field(name='NFT commands',value='list of NFT commands',inline=False)
      await ctx.respond(embed=embed,view=view)
      #----------------------------------------------------------------------------------------------------default embed
def setup(bot):
  bot.add_cog(help(bot))