import json
import discord
from discord.ext import commands
from discord.ui import Button, Select, View

class SettingPanel(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(name='setting', description='Show user setting pannel')
    async def panel(self, ctx: discord.ApplicationContext):
        with open('setting.json', 'r', encoding='utf-8') as file:
            setting_data = json.load(file)

        mid = ctx.author.id
        user_setting_data = setting_data.get(str(mid))
        print(user_setting_data)

        user_button = True
        user_language = 'en'
        if user_setting_data:
            user_button = user_setting_data.get('button', True)
            user_language = user_setting_data.get('language', 'en')

        user_button_select = Select(
            placeholder='test',
            options = [
                discord.SelectOption(label = 'menu 1 A opt', description = 'description of menu 1 a opt'),
                discord.SelectOption(label = 'menu 1 B opt', description = 'description of menu 1 b opt')
            ]
        )

        async def user_button_select_callback(interaction: discord.Interaction):
            await interaction.response.send_message(f'you selected {user_button_select.values[0]}', ephemeral = True)
        user_button_select.callback = user_button_select_callback
                            
        embed = discord.Embed(title='User setting', description='Open user setting pannel', color=0xffa46e)
        view = View()
        view.add_item(user_button_select)



        await ctx.respond(embed=embed, view=view, ephemeral=True)

def setup(bot):
    bot.add_cog(SettingPanel(bot))
