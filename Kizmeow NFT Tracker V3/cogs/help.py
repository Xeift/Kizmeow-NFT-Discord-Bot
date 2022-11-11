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
        # ----------------------------------------------------------------------------------------------------buttons
        b_bot_info = Button(label='Bot info', style=discord.ButtonStyle.blurple)
        b_system_commands = Button(label='System commands', style=discord.ButtonStyle.blurple)
        b_nft_commands = Button(label='NFT commands', style=discord.ButtonStyle.blurple)
        b_eth_commands = Button(label='eth commands', style=discord.ButtonStyle.blurple)
        b_return = Button(style=discord.ButtonStyle.gray, emoji='↩️')

        # ----------------------------------------------------------------------------------------------------buttons

        # callback
        # ----------------------------------------------------------------------------------------------------return callback
        async def b_return_callback(interaction):
            view = View()

            view.add_item(b_bot_info)
            view.add_item(b_system_commands)
            view.add_item(b_nft_commands)
            view.add_item(b_eth_commands)
            #view.add_item(b_return)

            embed = discord.Embed(title='**Help**', description='`click the button below to select different section`',
                                  color=0xFFA46E)
            embed.add_field(name='**Bot info**', value='`information about the bot`', inline=False)
            embed.add_field(name='**System commands**', value='`list of system commands`', inline=False)
            embed.add_field(name='**NFT commands**', value='`list of NFT commands`', inline=False)
            embed.timestamp = datetime.datetime.now()
            await interaction.response.edit_message(embed=embed, view=view)

        b_return.callback = b_return_callback

        # ----------------------------------------------------------------------------------------------------return callback

        # ----------------------------------------------------------------------------------------------------bot info callback
        async def b_bot_info_callback(interaction):
            embed = discord.Embed(title='**Bot info**', description='', color=0xFFA46E)
            embed.add_field(name='**Bot name**', value='[Kizmeow NFT Tracker V3#2184]('
                                                       'https://discord.com/api/oauth2/authorize?client_id'
                                                       '=923512417907015693&permissions=277025508352&scope=applications'
                                                       '.commands%20bot)', inline=False)
            embed.add_field(name='**Developer**', value='[Xeift#1230](https://discord.com/users/874806243208871977)',
                            inline=False)
            embed.add_field(name='**Bot avatar illustrator**', value='[Kiyue](https://www.facebook.com/profile.php?id'
                                                                     '=100026170072950)', inline=False)
            embed.add_field(name='**Programming language**', value='[Python](https://www.python.org/)', inline=False)
            b_github = Button(label='GitHub', style=discord.ButtonStyle.link,
                              url='https://github.com/Xeift/Kizmeow-OpenSea-and-Etherscan-Discord-Bot')
            embed.timestamp = datetime.datetime.now()

            view = View()
            view.add_item(b_github)
            view.add_item(b_return)
            await interaction.response.edit_message(embed=embed, view=view)

        b_bot_info.callback = b_bot_info_callback

        # ----------------------------------------------------------------------------------------------------bot info callback

        # ----------------------------------------------------------------------------------------------------system commands callback
        async def b_system_commands_callback(interaction):
            embed = discord.Embed(title='**System commands**', description='', color=0xFFA46E)
            embed.add_field(name='**/help**', value='`display this message`', inline=False)
            embed.add_field(name='**/meow**', value='`return bot latency`', inline=False)
            embed.add_field(name='**/invite**', value='`invite Kizmeow to your server`', inline=False)
            embed.timestamp = datetime.datetime.now()

            view = View()
            view.add_item(b_return)
            await interaction.response.edit_message(embed=embed, view=view)

        b_system_commands.callback = b_system_commands_callback

        # ----------------------------------------------------------------------------------------------------system commands callback

        # ----------------------------------------------------------------------------------------------------NFT commands callback
        async def b_nft_commands_callback(interaction):
            embed = discord.Embed(title='**NFT commands**', description='', color=0xFFA46E)
            embed.add_field(name='**/project_realtime**', value='`display project realtime information`', inline=False)
            embed.add_field(name='**/project_history**', value='`display project history information`', inline=False)
            embed.add_field(name='**/project_nft**', value='`display information of specific NFT`', inline=False)
            embed.add_field(name='**/project_rarity**', value='`calculate the rarity of a specific NFT`', inline=False)
            embed.timestamp = datetime.datetime.now()

            view = View()
            view.add_item(b_return)
            await interaction.response.edit_message(embed=embed, view=view)

        b_nft_commands.callback = b_nft_commands_callback
        # ----------------------------------------------------------------------------------------------------NFT commands callback

        # ----------------------------------------------------------------------------------------------------eth commands callback
        async def b_eth_commands_callback(interaction):
            embed = discord.Embed(title='**ETH commands**', description='', color=0xFFA46E)
            embed.add_field(name='**/gas**', value='`returns the last price for gas`', inline=False)
            embed.add_field(name='**/eth**', value='`returns the last price for eth in usd`', inline=False)
            embed.timestamp = datetime.datetime.now()

            view = View()
            view.add_item(b_return)
            await interaction.response.edit_message(embed=embed, view=view)

        b_eth_commands.callback = b_eth_commands_callback

        # ----------------------------------------------------------------------------------------------------eth commands callback

        # ----------------------------------------------------------------------------------------------------default buttons
        view = View()

        view.add_item(b_bot_info)
        view.add_item(b_system_commands)
        view.add_item(b_nft_commands)
        view.add_item(b_eth_commands)
        #view.add_item(b_return)
        # ----------------------------------------------------------------------------------------------------default buttons

        # ----------------------------------------------------------------------------------------------------default embed
        embed = discord.Embed(title='**Help**', description='`click the button below to select different section`',
                              color=0xFFA46E)
        embed.add_field(name='**Bot info**', value='`information about the bot`', inline=False)
        embed.add_field(name='**System commands**', value='`list of system commands`', inline=False)
        embed.add_field(name='**NFT commands**', value='`list of NFT commands`', inline=False)
        embed.timestamp = datetime.datetime.now()
        await ctx.respond(embed=embed, view=view)
        # ----------------------------------------------------------------------------------------------------default embed


def setup(bot):
    bot.add_cog(help(bot))
