import os
import discord
from dotenv import load_dotenv

bot = discord.Bot(intents=discord.Intents.all(), )


@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')


extensions = [  # load cogs
    # --------------------system commands
    'cogs.meow',
    'cogs.invite',
    'cogs.help',
    # --------------------system commands

    # --------------------etherscan commands
    'cogs.gas',
    'cogs.eth',
    # --------------------etherscan commands

    # --------------------NFT commands
    'cogs.project'
    # --------------------NFT commands
]

if __name__ == '__main__':  # import cogs from cogs folder
    for extension in extensions:
        bot.load_extension(extension)

load_dotenv()
bot.run(os.getenv('TOKEN'))  # bot token
