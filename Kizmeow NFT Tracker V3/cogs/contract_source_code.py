import discord
from discord.commands import slash_command
from discord.ext import commands
from discord.commands import Option
from core.cog_core import cogcore
import requests
import asyncio
import json
import os

class contract_source_code(cogcore):
    @slash_command(guild_ids=[936236815545954384],name='contract_source_code',description='display contract source code of the project')
    async def contract_source_code(
        self,
        ctx: discord.ApplicationContext,
        contract_address: Option(str, 'contract address of the project')
    ):
        r = requests.get('https://api.etherscan.io/api?module=contract&action=getsourcecode&address='+contract_address+'&apikey=6R8V8PKQRUXT55CFAX827CG8QB7FNNEBIR')
        resj = json.loads(r.text)
        source_code = resj['result'][0]['SourceCode'][1:-1]
        all_contract = json.loads(source_code)['sources']
        embed=discord.Embed(title='sending contracts...', color=0xFFA46E)
        await ctx.respond(embed=embed)
        for contract in all_contract:
            single_contract_code = all_contract[contract]['content']
            fname = contract[contract.rfind('/')+1:]
            with open('contracts/'+fname,'w') as outfile:
                outfile.write(single_contract_code)
        for filename in os.listdir('contracts'):
            await ctx.send(file=discord.File('contracts/'+filename))
            os.remove('contracts/'+filename)
            await asyncio.sleep(5)

def setup(bot):# add cog
    bot.add_cog(contract_source_code(bot))
