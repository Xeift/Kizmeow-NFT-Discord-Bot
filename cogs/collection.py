import json
import discord
import requests
from dotenv import load_dotenv
from discord.ext import commands
from discord.ui import Button
from discord.commands import Option, slash_command
from api_requests.modulenft import modulenft_embed
from api_requests.opensea import opensea_embed
from api_requests.looksrare import looksrare_embed
from buttons.buttons import opensea_button, looksrare_button, return_button


class collection(commands.Cog):

    
    def __init__(self, bot):
        self.bot = bot

    
    def collection_name_autocomplete(self: discord.AutocompleteContext):
        with open('collection_name_autocomplete.json','r') as of:
            collection_name_data = json.load(of)
        return collection_name_data.keys()

    
    @slash_command(name='collection', description='Check collection information from Opensea, LooksRare and X2Y2')
    async def collection(
        self,
        ctx: discord.ApplicationContext.defer,
        collection: Option(
            str,
            'Specify the collection slug',
            autocomplete=collection_name_autocomplete
        )
    ):

        await ctx.defer()
        
        '''            handle autocomplete            '''
        with open('collection_name_autocomplete.json','r') as of:
            collection_name_data = json.load(of)
        if collection in collection_name_data:
            collection = collection_name_data[collection]

        
        '''            initial embed            '''
        (embed, view) = await modulenft_embed(collection)
        await ctx.respond(embed=embed, view=view)

        
        '''            return embed            '''
        async def return_button_callback(interaction):
            if ctx.author == interaction.user:
                (embed, view) = await modulenft_embed(collection)
                await interaction.response.edit_message(embed=embed, view=view)
            else:
                embed = discord.Embed(title='Consider use `/collection` command by yourself.', color=0xFFA46E)
                await interaction.response.send_message(embed=embed, ephemeral=True)
        return_button.callback = return_button_callback

        
        '''            opensea embed            '''
        async def opensea_button_callback(interaction):
            if ctx.author == interaction.user:
                (embed, view) = await opensea_embed(collection)
                await interaction.response.edit_message(embed=embed, view=view)
            else:
                embed = discord.Embed(title='Consider use `/collection` command by yourself.', color=0xFFA46E)
                await interaction.response.send_message(embed=embed, ephemeral=True)
        opensea_button.callback = opensea_button_callback


        '''            looksrare embed            '''
        async def looksrare_button_callback(interaction):
            if ctx.author == interaction.user:
                (embed, view) = await looksrare_embed(collection)
                await interaction.response.edit_message(embed=embed, view=view)
            else:
                embed = discord.Embed(title='Consider use `/collection` command by yourself.', color=0xFFA46E)
                await interaction.response.send_message(embed=embed, ephemeral=True)
        looksrare_button.callback = looksrare_button_callback
        

def setup(bot):
    bot.add_cog(collection(bot))
