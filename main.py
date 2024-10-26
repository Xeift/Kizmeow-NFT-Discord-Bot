import os
import discord
from dotenv import load_dotenv


intents = discord.Intents.default()
# intents.members=True
bot = discord.Bot(intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

if __name__ == '__main__':  # import cogs from cogs folder
    extensions = [
        'cogs.ping',

    ]
    for extension in extensions: bot.load_extension(extension)

load_dotenv()
bot.run(os.getenv('TOKEN'))
