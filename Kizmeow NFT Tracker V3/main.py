import discord

bot = discord.Bot(intents=discord.Intents.all(),)
@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

extensions = [# load cogs
  #--------------------system commands
  'cogs.meow',
  'cogs.invite',
  'cogs.help',
  #--------------------system commands

  #--------------------NFT commands
  'cogs.project_realtime',
  'cogs.project_history',
  'cogs.project_nft',
  'cogs.contract_source_code'
  #--------------------NFT commands
]

if __name__ == '__main__':# import cogs from cogs folder
	for extension in extensions:
		bot.load_extension(extension) 
        
bot.run('OTIzNTEyNDE3OTA3MDE1Njkz.YcRF9g.wMJN53-MfAYefMQ1LsjB5a3-j8k')# bot token