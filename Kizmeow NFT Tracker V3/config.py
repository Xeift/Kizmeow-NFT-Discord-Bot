import json

config = {}
config['ETHERSCAN_API_KEY'] = str(input('enter etherscan api key: '))
config['DISCORD_BOT_TOKEN'] = str(input('enter discord bot token: '))

print(f'\nsuccess!\nyour config is:\n{config}')
with open('Kizmeow NFT Tracker V3/config.json','w') as of:
    json.dump(config,of)