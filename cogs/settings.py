import discord
from discord import (ApplicationContext, Embed, IntegrationType,
                     InteractionContextType)
from discord.ext import commands
from discord.ui import Select, View

from embed.settings_embed import settings_embed
from utils.load_config import load_config_from_json, update_config_to_json


class SettingPanel(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(
        name='settings',
        description='Show preference settings panel.',
        integration_types=[
            IntegrationType.user_install,
            IntegrationType.guild_install,
        ],
        contexts=[
            InteractionContextType.guild,
            InteractionContextType.bot_dm,
            InteractionContextType.private_channel,
        ],
    )
    async def panel(self, ctx: ApplicationContext):

        mid = ctx.author.id
        (
            user_button,
            user_language,
            user_visibility,
            favorite_collections,
            favorite_nfts
        ) = load_config_from_json(str(mid))

        # ---------- user_button_select  ----------
        # user_button_select = Select(
        #     placeholder='enable/disable button',
        #     options=[
        #         discord.SelectOption(
        #             label='Button: Clickable',
        #             description='Makes buttons clickable.',
        #             emoji='✅',
        #             default=user_button
        #         ),
        #         discord.SelectOption(
        #             label='Button: Non clickable',
        #             description='Makes button not clickable.',
        #             emoji='❌',
        #             default=not user_button
        #         )
        #     ]
        # )

        # async def user_button_select_callback(interaction: discord.Interaction):
        #     selected_opt = user_button_select.values[0]
        #     button_status = False
        #     if selected_opt == 'Button: Clickable':
        #         button_status = True

        #     update_config_to_json(str(mid), button=button_status)
        #     embed = Embed(
        #         title='[Success]',
        #         description=f'The setting `{selected_opt}` has been applied',
        #         color=0xffa46e
        #     )
        #     await interaction.response.send_message(embed=embed, ephemeral=True)
        # user_button_select.callback = user_button_select_callback
        # ---------- user_button_select  ----------

        # ---------- user_visibility_select  ----------
        user_visibility_select = Select(
            placeholder='toggle command visibility',
            options=[
                discord.SelectOption(
                    label='Command visibility: Only you',
                    description='Only you can see the command response.',
                    emoji='🔒',
                    default=not user_visibility
                ),
                discord.SelectOption(
                    label='Command visibility: All',
                    description='Everyone can see the command response.',
                    emoji='🌐',
                    default=user_visibility
                )
            ]
        )

        async def user_visibility_select_callback(interaction: discord.Interaction):
            selected_opt = user_visibility_select.values[0]
            visibility_status = True
            if selected_opt == 'Command visibility: Only you':
                visibility_status = False

            update_config_to_json(str(mid), visibility=visibility_status)
            embed = Embed(
                title='[Success]',
                description=f'The setting `{selected_opt}` has been applied',
                color=0xffa46e
            )
            await interaction.response.send_message(embed=embed, ephemeral=True)
        user_visibility_select.callback = user_visibility_select_callback
        # ---------- user_visibility_select  ----------

        # TODO: language
        # TODO: custom IPFS gsteway(select)
        # TODO: custom block exp(select)


        view = View()
        # view.add_item(user_button_select)
        view.add_item(user_visibility_select)

        await ctx.respond(embed=settings_embed(), view=view, ephemeral=True)


def setup(bot):
    bot.add_cog(SettingPanel(bot))
