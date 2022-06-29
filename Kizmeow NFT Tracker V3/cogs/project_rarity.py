import datetime
import json

import discord
from discord.commands import Option
from discord.commands import slash_command
from discord.ext import commands
from opensea import OpenseaAPI


class project_rarity(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @slash_command(name='project_rarity',
                   description='query your NFT rarity from the collection slug and token id you entered')
    async def project_rarity(
            self,
            ctx: discord.ApplicationContext,
            project_name: Option(str, 'smart contract address of the project'),
            token_id: Option(str, 'token id of the NFT')
    ):
        api = OpenseaAPI(apikey='OS_API')
        info0 = api.collection(collection_slug=project_name)

        contract_address = info0['collection']['primary_asset_contracts'][0]['address']

        total_supply = info0['collection']['stats']['total_supply']

        collection_trait = info0['collection']['traits']

        #
        file = open("traits.json", "r")
        data = json.load(file)

        for t_type in collection_trait:
            except_none = 0
            for t_name in collection_trait[t_type]:
                except_none += (collection_trait[t_type][t_name])
                data[t_type] = collection_trait[t_type]
                data[t_type][t_name] = round(total_supply / collection_trait[t_type][t_name], 2)

            if (total_supply - except_none) != 0:
                data[t_type]["none"] = round(total_supply / (total_supply - except_none), 2)
        with open('traits.json', 'w') as outfile:
            json.dump(data, outfile)
        file.close()

        # query nft traits from opensea and get rarity from traits.json

        file = open("traits.json", "r")
        data = json.load(file)

        api = OpenseaAPI(apikey="bc734b71e4c94692992026987967b1fc")
        info1 = api.asset(asset_contract_address=contract_address,
                          token_id=token_id)

        if info1['name'] == None:
            name = "no data"
        else:
            name = str(info1['name'])

        if info1['image_url'] == None:
            image_url = "no data"
        else:
            image_url = str(info1['image_url'])

        if info1['top_ownerships'][0]['owner']['user'] == None:
            top_ownerships = "no data"
        else:
            top_ownerships = str(info1['top_ownerships'][0]['owner']['user']['username'])

        if info1['permalink'] == None:
            permalink = "no data"
        else:
            permalink = str(info1['permalink'])

        finaldata = {}
        total_traits_score = 0.0
        single_traitscount = 0
        for all_element in data:  # all
            match = 0

            for element in info1['traits']:  # nft
                if all_element == element['trait_type']:
                    ev = element['value'].lower()

                    finaldata[all_element] = {"1": element['value'], "2": data[all_element][ev]}
                    match = 1
                    single_traitscount += 1
                    total_traits_score += float(data[all_element][ev])

            if match != 1:
                finaldata[all_element] = {"1": 'none', "2": data[all_element]['none']}
                total_traits_score += float(data[all_element]['none'])
        print(str(single_traitscount))
        print(total_traits_score)

        with open('finaldata.json', 'w') as outfile:
            json.dump(finaldata, outfile)

        file = open("finaldata.json", "r")
        fdata = json.load(file)

        embed = discord.Embed(title="**" + name + "**", url=permalink, color=0xFFA46E)
        embed.set_image(url=image_url)
        embed.add_field(name="Owner", value='`' + top_ownerships + '`', inline=False)
        embed.add_field(name="Traits count", value='`' + str(single_traitscount) + '`', inline=False)
        embed.add_field(name="Total traits score", value='`' + str(total_traits_score) + '`',
                        inline=False)  # round(total_traits_score, 2)
        embed.add_field(name=" ㅤ", value=" ㅤ", inline=False)
        for result in fdata:
            embed.add_field(name=result, value=str(fdata[result]['1']) + '`' + str(fdata[result]['2']) + '`',
                            inline=True)
            embed.timestamp = datetime.datetime.now()
            embed.set_footer(text=name)

        await ctx.respond(embed=embed)


def setup(bot):
    bot.add_cog(project_rarity(bot))
