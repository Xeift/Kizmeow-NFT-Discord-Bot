import json

import discord
from discord.ext import commands
from discord.ui import Select, View

from utils.load_config import load_config_from_json, update_config_to_json


class SettingPanel(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(name='setting', description='Show user setting pannel')
    async def panel(self, ctx: discord.ApplicationContext):

        mid = ctx.author.id
        (user_button, user_language, user_visibility) = load_config_from_json(str(mid))

        user_button_select = Select(
            placeholder='enable/disable button',
            options=[
                discord.SelectOption(
                    label='Button: Clickable',
                    description='Makes buttons clickable.',
                    emoji='✅',
                    default=user_button
                ),
                discord.SelectOption(
                    label='Button: Non clickable',
                    description='Makes button not clickable.',
                    emoji='❌',
                    default=not user_button
                )
            ]
        )

        async def user_button_select_callback(interaction: discord.Interaction):
            selected_opt = user_button_select.values[0]
            button_status = False
            if selected_opt == 'Button: Clickable':
                button_status = True

            update_config_to_json(str(mid), button=button_status)

            await interaction.response.send_message(f'you selected {user_button_select.values[0]}', ephemeral=True)
        user_button_select.callback = user_button_select_callback

        # TODO: command visibility, language

        embed = discord.Embed(
            title='User setting',
            description=f'Click the dropdown menu below to set the bot.',
            color=0xffa46e
        )
        view = View()
        view.add_item(user_button_select)

        await ctx.respond(embed=embed, view=view, ephemeral=True)


def setup(bot):
    bot.add_cog(SettingPanel(bot))
