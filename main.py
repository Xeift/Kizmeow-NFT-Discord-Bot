import os

import discord
from dotenv import load_dotenv

intents = discord.Intents.default()
bot = discord.Bot(intents=intents)


@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

if __name__ == '__main__':
    extensions = [
        'cogs.ping',
        'cogs.settings',
        'cogs.opensea_account',
        'cogs.opensea_collection',
    	'cogs.opensea_nft',
    	'cogs.gas',
    	'cogs.address_converter'
    ]
    for extension in extensions:
        bot.load_extension(extension)

load_dotenv()
bot.run(os.getenv('DISCORD_BOT_TOKEN'))
