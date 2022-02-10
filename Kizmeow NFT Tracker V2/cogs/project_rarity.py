import discord
from discord_slash.utils.manage_commands import create_option
import urllib.request as ur
import json
from discord_slash import cog_ext
from core.cog_core import cogcore

class project_rarity(cogcore):
  @cog_ext.cog_slash(name="project_rarity",
  description="query your NFT rarity from the collection slug and token id you entered",
  options=
  [
    create_option
    (
      name="collection_slug",
      description="enter the collection_slug of yor NFT",
      option_type=3,
      required=True
    ),
    create_option
    (
      name="token_id",
      description="enter the token id of your NFT",
      option_type=3,
      required=True
    )
  ],
  )

  async def project_rarity(self,ctx,collection_slug,token_id):
    url0="https://api.opensea.io/api/v1/collection/"+collection_slug #api url
    req = ur.Request(url=url0,headers={'User-Agent': 'Mozilla/5.0'})

    site0 = ur.urlopen(req)
    page0 = site0.read()
    contents0 = page0.decode()
    data0 = json.loads(contents0)

    contract_address = data0['collection']['primary_asset_contracts'][0]['address']

    total_supply = data0['collection']['stats']['total_supply']

    collection_trait = data0['collection']['traits']


    #
    file = open("traits.json", "r")
    data = json.load(file)



    for t_type in collection_trait:
      except_none = 0
      for t_name in collection_trait[t_type]:
        except_none += (collection_trait[t_type][t_name])
        data[t_type] = collection_trait[t_type]
        data[t_type][t_name] = round(total_supply / collection_trait[t_type][t_name],2)
        
      if (total_supply-except_none) != 0:
        data[t_type]["none"] = round(total_supply / (total_supply-except_none),2)
    with open('traits.json', 'w') as outfile:
      json.dump(data, outfile)
    file.close()

    #query nft traits from opensea and get rarity from traits.json

    file = open("traits.json", "r")
    data = json.load(file)


    url1='https://api.opensea.io/api/v1/asset/'+contract_address+'/'+token_id+'/?format=json' #api url
    req = ur.Request(url=url1,headers={'User-Agent': 'Mozilla/5.0'})

    site1 = ur.urlopen(req)
    page1 = site1.read()
    contents1 = page1.decode()
    data1 = json.loads(contents1)

    if data1['name'] == None:
      name = "no data"
    else:
      name = str(data1['name'])

    if data1['image_original_url'] == None:
      image_original_url = "no data"
    else:
      image_original_url = str(data1['image_original_url'])

    if data1['top_ownerships'][0]['owner']['user'] == None:
      top_ownerships = "no data"
    else:
      top_ownerships = str(data1['top_ownerships'][0]['owner']['user']['username'])

    if data1['permalink'] == None:
      permalink = "no data"
    else:
      permalink = str(data1['permalink'])

    finaldata = {}
    totalrarity = 0.0
    total_traits_score = 0.0
    single_traitscount = 0
    for all_element in data:#all
      match = 0
      
      for element in data1['traits']:#nft
        if all_element == element['trait_type']:
          
          ev = element['value'].lower()


          finaldata[all_element] = {"1":element['value'],"2":data[all_element][ev]}
          match = 1
          single_traitscount += 1
          total_traits_score += float(data[all_element][ev])
      
        #finaldata[all_element] = {"1":element['value'],"2":data[all_element][ev] }
      if match != 1:
        finaldata[all_element] = {"1":'none',"2":data[all_element]['none']}
        total_traits_score += float(data[all_element]['none'])
    print(single_traitscount)

    with open('finaldata.json', 'w') as outfile:
      json.dump(finaldata, outfile)

    file = open("finaldata.json", "r")
    fdata = json.load(file)    


    embed=discord.Embed(title="["+name+"]", color=0xe8006f)
    embed.set_thumbnail(url=image_original_url)
    embed.add_field(name="token id" , value=token_id, inline=False) 
    embed.add_field(name="owner" , value=top_ownerships, inline=False)
    embed.add_field(name="OpenSea" , value=permalink, inline=False)
    embed.add_field(name="traits count" , value=single_traitscount, inline=False)
    embed.add_field(name="total traits score" , value=round(total_traits_score,2), inline=False)
    embed.add_field(name=" ㅤ" , value=" ㅤ", inline=False)
    for result in fdata:
      embed.add_field(name=result, value=str(fdata[result]['1'])+" "+str(fdata[result]['2']), inline=True)
      
      

    await ctx.send(embed=embed)

def setup(bot):
  bot.add_cog(project_rarity(bot))
