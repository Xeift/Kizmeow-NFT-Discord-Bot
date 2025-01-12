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
            placeholder='enable/disable button',
            options = [
                discord.SelectOption(
                    label = 'Button: Clickable',
                    description = 'Makes buttons clickable.',
                    emoji = '✅',
                    default = user_button
                ),
                discord.SelectOption(
                    label = 'Button: Non clickable', 
                    description = 'Makes button not clickable.',
                    emoji='❌',
                    default = not user_button
                )
            ]
        )

        async def user_button_select_callback(interaction: discord.Interaction):
            selected_opt = user_button_select.values[0]
            button_status = False
            if selected_opt == 'Button: Clickable':
                button_status = True
                
            with open('setting.json', 'w', encoding='utf-8') as file:
                setting_data.setdefault(str(mid), {})['button'] = True
                # setting_data[str(mid)]['button'] = True
                json.dump(setting_data, file, ensure_ascii=False, indent=4)

            await interaction.response.send_message(f'you selected {user_button_select.values[0]}', ephemeral = True)
        user_button_select.callback = user_button_select_callback
                            
        embed = discord.Embed(title='User setting', description='Click the dropdown menu below to set the bot.', color=0xffa46e)
        view = View()
        view.add_item(user_button_select)

        # TODO: command visibility, language

        await ctx.respond(embed=embed, view=view, ephemeral=True)

def setup(bot):
    bot.add_cog(SettingPanel(bot))
