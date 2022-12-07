import os
import discord
import datetime
import aiohttp

from discord import Webhook
from dotenv import load_dotenv
from discord.ext import commands
from discord.ui import Button, View
from discord.commands import slash_command, Option


class feedback(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    async def get_option(self: discord.AutocompleteContext):
        OPTIONS = ["Report a bug", "Request a feature", "Leave a comment"]
        return OPTIONS

    @slash_command(name='feedback', description='Leave feedback on Kizmeow NFT Bot')
    async def feedback(
            self,
            ctx: discord.ApplicationContext,
            type: Option(str, 'Specify what type of feedback you want to leave', autocomplete=get_option)
    ):
        global moda
        moda = type
        modal = MyModal(title=f'{type}')
        await ctx.send_modal(modal=modal)


class MyModal(discord.ui.Modal):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.add_item(discord.ui.InputText(label=moda, placeholder="Tell us more about the bug", style=discord.InputTextStyle.long))

    async def callback(self, interaction: discord.Interaction):
        value = self.children[0].value
        label = self.children[0].label
        invite_button = Button(label='Kizmeow Support Server', style=discord.ButtonStyle.link, emoji='<:kizmeow:1047912736224448562>')
        invite_button.url = 'https://discord.gg/PxNF9PaSKv'
        invite_button.custom_id = None
        view = View(timeout=None)
        view.add_item(invite_button)
        embed_image = discord.Embed(title='', color=0xFFA46E)
        embed_image.set_image(url='https://cdn.discordapp.com/attachments/1049368137570721813/1049732968932966470/Thanks.png?width=1441&height=400')
        embed = discord.Embed(title="**Your feedback is being processed**", color=0xFFA46E)
        embed.set_image(url='https://cdn.discordapp.com/attachments/1049368137570721813/1049370333389541456/laine.png?width=1441&height=400')
        embed.add_field(name=f'{label}', value=f'`{value}`', inline=False)
        embed.set_author(name=f'{interaction.user.name}', icon_url=f'{interaction.user.avatar}')
        embed.set_footer(text='Data provided by Kizmeow NFT Bot', icon_url='https://user-images.githubusercontent.com/80938768/204983971-d7cf0e40-f4ce-4737-ba07-85ed62112dab.png')
        embed.timestamp = datetime.datetime.now()
        await interaction.response.send_message(embeds=[embed_image, embed], view=view, ephemeral=True)

        embed_image_submit = discord.Embed(title='', color=0xFFA46E)
        embed_image_submit.set_image(url='https://cdn.discordapp.com/attachments/1049368137570721813/1049769344428687460/eyes-horizontal-flipped.gif?width=1441&height=400')
        embed_submit = discord.Embed(title=f"**New {moda}**", color=0xFFA46E)
        embed_submit.set_image(url='https://cdn.discordapp.com/attachments/1049368137570721813/1049370333389541456/laine.png?width=1441&height=400')
        embed_submit.add_field(name=f'{label}', value=f'`{value}`', inline=False)
        embed_submit.add_field(name="Author's name", value=f'[{interaction.user.name}](https://discord.com/users/{interaction.user.id})', inline=True)
        embed_submit.add_field(name="Guild name", value=f'{interaction.guild.name}', inline=True)
        embed_submit.set_author(name=f'{interaction.user.name}', icon_url=f'{interaction.user.avatar}')
        embed_submit.set_footer(text='Data provided by Kizmeow NFT Bot', icon_url='https://user-images.githubusercontent.com/80938768/204983971-d7cf0e40-f4ce-4737-ba07-85ed62112dab.png')
        embed_submit.timestamp = datetime.datetime.now()

        async def foo():
            load_dotenv()
            async with aiohttp.ClientSession() as session:
                if moda == "Report a bug":
                    webhook = Webhook.from_url(os.getenv('REPORT_A_BUG'), session=session)
                    await webhook.send(embeds=[embed_image_submit, embed_submit], username=f"**New {moda}**", avatar_url="https://user-images.githubusercontent.com/80938768/204983971-d7cf0e40-f4ce-4737-ba07-85ed62112dab.png", content='||<@&1047816305060880454><@&1047819403657490513>||')
                elif moda == "Request a feature":
                    webhook = Webhook.from_url(os.getenv('REQUEST_A_FEATURE'), session=session)
                    await webhook.send(embeds=[embed_image_submit, embed_submit], username=f"**New {moda}**", avatar_url="https://user-images.githubusercontent.com/80938768/204983971-d7cf0e40-f4ce-4737-ba07-85ed62112dab.png", content='||<@&1047816305060880454><@&1047819403657490513>||')
                elif moda == "Leave a comment":
                    webhook = Webhook.from_url(os.getenv('LEAVE_A_COMMENT'), session=session)
                    await webhook.send(embeds=[embed_image_submit, embed_submit], username=f"**New {moda}**", avatar_url="https://user-images.githubusercontent.com/80938768/204983971-d7cf0e40-f4ce-4737-ba07-85ed62112dab.png", content='||<@&1047816305060880454><@&1047819403657490513>||')
                else:
                    webhook = Webhook.from_url(os.getenv('MISCELLANEOUS'), session=session)
                    await webhook.send(embeds=[embed_image_submit, embed_submit], username=f"**New {moda}**", avatar_url="https://user-images.githubusercontent.com/80938768/204983971-d7cf0e40-f4ce-4737-ba07-85ed62112dab.png", content='||<@&1047816305060880454><@&1047819403657490513>||')

        await foo()


def setup(bot):
    bot.add_cog(feedback(bot))