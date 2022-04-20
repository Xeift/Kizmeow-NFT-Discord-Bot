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
  'cogs.project_nft'
  #--------------------NFT commands
]

if __name__ == '__main__':# import cogs from cogs folder
	for extension in extensions:
		bot.load_extension(extension) 
        
bot.run('ABCDEF123456789')# bot token
