import os
import discord
from dotenv import load_dotenv

bot = discord.Bot(intents=discord.Intents.all(), )


@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')


extensions = [  # load cogs
    # --------------------system commands
    'cogs.ping',
    'cogs.help',
    'cogs.reload_cmds',  # only for debug
    # --------------------system commands

    # --------------------Web3 commands
    'cogs.gas',
    'cogs.eth',
    # --------------------Web3 commands

    # --------------------NFT commands
    'cogs.collection',
    'cogs.nft'
    # --------------------NFT commands
]

if __name__ == '__main__':  # import cogs from cogs folder
    for extension in extensions:
        bot.load_extension(extension)

load_dotenv()
bot.run(os.getenv('TOKEN'))  # bot token
