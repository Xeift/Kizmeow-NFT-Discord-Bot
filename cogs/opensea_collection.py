
import json

from discord import (ApplicationContext, AutocompleteContext, ButtonStyle,
                     Embed, IntegrationType, InteractionContextType, Option,
                     PartialEmoji)
from discord.ext import commands
from discord.ui import Button, View

from api.get_os_collection import get_os_collection
from api.get_os_collection_statistics import get_os_collection_statistics


class opensea_collection(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    def collection_name_autocomplete(self: AutocompleteContext):
        with open('collection_name_autocomplete.json', 'r') as of:
            collection_name_data = json.load(of)
        return collection_name_data.keys()

    @commands.slash_command(
        name='opensea_collection',
        description='View details of a specific OpenSea NFT collection',
        integration_types=[
            IntegrationType.user_install,
            IntegrationType.guild_install,
        ],
        contexts=[
            InteractionContextType.guild,
            InteractionContextType.bot_dm,
            InteractionContextType.private_channel,
        ],
    )
    async def opensea_collection(
        self,
        ctx: ApplicationContext,
        collection: Option(
            str,
            'Specify the collection slug',
            autocomplete=collection_name_autocomplete
        )
    ):
        await ctx.defer()

        with open('collection_name_autocomplete.json','r') as of:
            collection_name_data = json.load(of)
        if collection in collection_name_data:
            collection = collection_name_data[collection]
        
        (success, collection_data) = get_os_collection(collection)


        embed = Embed(color=0xFFA46E)
        view = View()

        if success:
            name = collection_data['name']
            cas = collection_data['contracts']
            cas_text = ''
            description = collection_data['description']
            if description != '': description = f'>>> {description}'
            supply = collection_data['total_supply']
            category = collection_data['category']
            created_date = collection_data['created_date']
            owner_address = collection_data['owner']
            owner_address_short = collection_data['owner'][:7]
            owner_exp_url = f'https://etherscan.io/address/{owner_address}'
            owner_os_url = f'https://opensea.io/{owner_address}'
            fees = collection_data['fees']
            fees_text = ''
            verify_state = collection_data['safelist_status']
            pfp_img = collection_data['image_url']
            banner_img = collection_data['banner_image_url']
            
            embed.title = f'OpenSea Collection Info of {name}'
            embed.set_thumbnail(url=pfp_img) 
            if banner_img != '':
                embed.set_image(url=banner_img)

            for ca in cas:
                cas_text += f'[{ca['address'][:7]}](https://etherscan.io/address/{ca['address']}) ({ca['chain']})\n'
            embed.add_field(name='Contract Address', value=cas_text, inline=False)
            embed.add_field(name='Description', value=description, inline=False)
            embed.add_field(name='Total Supply', value=supply, inline=True)
            embed.add_field(name='Category', value=category, inline=True)
            embed.add_field(name='Created Date', value=created_date, inline=True)
            embed.add_field(name='Owner', value=f'{owner_address_short}\n[Exp]({owner_exp_url})｜[OpenSea]({owner_os_url})', inline=True)
            for fee in fees:
                if fee['required'] == True:
                    fee['required'] = 'Required'
                else:
                    fee['required'] = 'Optional'

                fees_text += f"{fee['required']} [{fee['fee']}%](https://etherscan.io/address/{fee['recipient']})\n"
            embed.add_field(name='Fees', value=fees_text, inline=True)
            embed.add_field(name='Verification', value=verify_state, inline=True)

            (success, collection_statistic_data) = get_os_collection_statistics(collection)
            if success:
                num_holders = collection_statistic_data['total']['num_owners']
                market_cap = round(collection_statistic_data['total']['market_cap'], 2)
                floor_price = round(collection_statistic_data['total']['floor_price'], 2)
                floor_price_symbol = collection_statistic_data['total']['floor_price_symbol']

                volume_all = round(collection_statistic_data['total']['volume'], 2)
                volume_1d = round(collection_statistic_data['intervals'][0]['volume'], 2)
                volume_1d_del = round(collection_statistic_data['intervals'][0]['volume_change'], 2)
                volume_7d = round(collection_statistic_data['intervals'][1]['volume'], 2)
                volume_7d_del = round(collection_statistic_data['intervals'][1]['volume_change'], 2)
                volume_30d = round(collection_statistic_data['intervals'][2]['volume'], 2)
                volume_30d_del = round(collection_statistic_data['intervals'][2]['volume_change'], 2)

                sales_all = round(collection_statistic_data['total']['sales'], 2)
                sales_1d = round(collection_statistic_data['intervals'][0]['sales'], 2)
                sales_7d = round(collection_statistic_data['intervals'][1]['sales'], 2)
                sales_30d = round(collection_statistic_data['intervals'][2]['sales'], 2)

                average_price_all = round(collection_statistic_data['total']['average_price'], 2)
                average_price_1d = round(collection_statistic_data['intervals'][0]['average_price'], 2)
                average_price_7d = round(collection_statistic_data['intervals'][1]['average_price'], 2)
                average_price_30d = round(collection_statistic_data['intervals'][2]['average_price'], 2)

                embed.add_field(name='Unique Holders', value=num_holders, inline=True)
                embed.add_field(name='Market Cap', value=f'{market_cap} {floor_price_symbol}', inline=True)
                embed.add_field(name='Floor Price', value=f'{floor_price} {floor_price_symbol}', inline=True)
                embed.add_field(
                    name='Volume',
                    value=(
                        f'```1D  {str(volume_1d).ljust(12)}{floor_price_symbol}({volume_1d_del}%)\n'
                        f'7D  {str(volume_7d).ljust(12)}{floor_price_symbol}({volume_7d_del}%)\n'
                        f'30D {str(volume_30d).ljust(12)}{floor_price_symbol}({volume_30d_del}%)\n'
                        f'All {str(volume_all).ljust(12)}{floor_price_symbol}```'
                    ),
                    inline=False
                )
                embed.add_field(
                    name='Average Price',
                    value=(
                        f'`1D  {str(average_price_1d).ljust(8)} {floor_price_symbol}`\n'
                        f'`7D  {str(average_price_7d).ljust(8)} {floor_price_symbol}`\n'
                        f'`30D {str(average_price_30d).ljust(8)} {floor_price_symbol}`\n'
                        f'`All {str(average_price_all).ljust(8)} {floor_price_symbol}`'
                    ),
                    inline=True
                )
                embed.add_field(
                    name='Sales',
                    value=(
                        f'`1D  {str(sales_1d).ljust(8)} {name}`\n'
                        f'`7D  {str(sales_7d).ljust(8)} {name}`\n'
                        f'`30D {str(sales_30d).ljust(8)} {name}`\n'
                        f'`All {str(sales_all).ljust(8)} {name}`'
                    ),
                    inline=True
                )


            # TODO: block exp converter


        else:
            embed.title = '[Failed]'
            embed.description = f'Command execution failed. Reason:\n```{
                collection_data}```'

        await ctx.respond(embed=embed, view=view)


def setup(bot):
    bot.add_cog(opensea_collection(bot))
