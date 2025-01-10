import discord
from discord.ext import commands
from discord.ui import Button, View

class SettingPanel(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(name='setting', description='Show user setting pannel')
    async def panel(self, ctx: discord.ApplicationContext):
        embed = discord.Embed(title='User setting', description='Open user setting pannel', color=0xffa46e)

        view = View()

        button1 = Button(label='btn1', style=discord.ButtonStyle.primary)
        button1.callback = self.button1_callback
        view.add_item(button1)

        button2 = Button(label='btn2', style=discord.ButtonStyle.secondary)
        button2.callback = self.button2_callback
        view.add_item(button2)


        await ctx.respond(embed=embed, view=view, ephemeral=True)

    async def button1_callback(self, interaction: discord.Interaction):
        await interaction.response.send_message('btn1', ephemeral=True)

    async def button2_callback(self, interaction: discord.Interaction):
        await interaction.response.send_message('btn2', ephemeral=True)

def setup(bot):
    bot.add_cog(SettingPanel(bot))
