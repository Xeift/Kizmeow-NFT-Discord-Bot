import discord
import asyncio
import json
import urllib.request as ur

bot = discord.Bot(intents=discord.Intents.all(), )


@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')
    while True:
        url = 'https://api.etherscan.io/api?module=gastracker&action=gasoracle&apikey=' + etherscan_api_key  # api url

        site = ur.urlopen(url)
        page = site.read()
        contents = page.decode()
        data = json.loads(contents)

        SafeGasPrice = data['result']['SafeGasPrice']
        ProposeGasPrice = data['result']['ProposeGasPrice']
        FastGasPrice = data['result']['FastGasPrice']

        presence_ctx = '⚡️' + FastGasPrice + '| 🚶🏼‍♂️' + ProposeGasPrice + '| 🐢' + SafeGasPrice

        await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=presence_ctx))
        await asyncio.sleep(25)


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
    'cogs.project_rarity',
    'cogs.project_realtime',
    'cogs.project_history',
    'cogs.project_nft'
    # --------------------NFT commands
]

if __name__ == '__main__':  # import cogs from cogs folder
    for extension in extensions:
        bot.load_extension(extension)

bot.run('TOKEN')  # bot token
