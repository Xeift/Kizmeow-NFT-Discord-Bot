from discord import Embed

from api.get_os_collection_statistics import get_os_collection_statistics
from utils.chain import get_info_by_code
from view.button import exp_button


def opensea_collection_embed(collection_data, collection, view):
    embed = Embed(color=0xFFA46E)
    collection_name = collection_data['name']
    cas = collection_data['contracts']
    cas_text = ''
    description = collection_data['description']
    if description != '':
        description = f'>>> {description}'
    supply = collection_data['total_supply']
    category = collection_data['category']
    created_date = collection_data['created_date']
    owner_address = collection_data['owner']
    owner_address_short = collection_data['owner'][:7]
    default_chain = collection_data['payment_tokens'][0]['chain'] if cas == [] else cas[0]['chain']
    (
        chain_name,
        exp_name,
        exp_address_url,
        exp_token_url,
        _,
        ticker,
        _
    ) = get_info_by_code(default_chain)
    owner_exp_url = f'{exp_address_url}{owner_address}'
    owner_os_url = f'https://opensea.io/{owner_address}'
    fees = collection_data['fees']
    fees_text = ''
    verify_state = collection_data['safelist_status']
    pfp_img = collection_data['image_url']
    banner_img = collection_data['banner_image_url']

    opensea_url = collection_data['opensea_url']
    website_url = collection_data['project_url']
    wiki_url = collection_data['wiki_url']
    discord_url = collection_data['discord_url']
    telegram_url = collection_data['telegram_url']
    x_username = collection_data['twitter_username']
    x_url = f'https://x.com/{x_username}'
    instagram_username = collection_data['instagram_username']
    instagram_url = f'https://www.instagram.com/{instagram_username}'

    embed.title = f'{collection_name}'
    embed.set_thumbnail(url=pfp_img)
    if banner_img != '':
        embed.set_image(url=banner_img)

    for ca in cas:
        chain = ca['chain']
        address = ca['address']
        (
            chain_name,
            exp_name,
            exp_address_url,
            exp_token_url,
            exp_emoji,
            ticker,
            _
        ) = get_info_by_code(chain)


        view.add_item(exp_button(
            exp_name,
            f'{exp_token_url}{address}',
            exp_emoji
        ))
        cas_text += f"[{ca['address'][:7]}]({exp_token_url}{ca['address']}) ({chain_name})\n"

    if cas_text != '':
        embed.add_field(name='Contract Address',
                        value=cas_text, inline=False)
    embed.add_field(name='Description',
                    value=description, inline=False)
    embed.add_field(name='Total Supply', value=supply, inline=True)
    embed.add_field(name='Category', value=category, inline=True)
    embed.add_field(name='Created Date',
                    value=created_date, inline=True)
    if cas != []:
        embed.add_field(
            name='Owner',
            value=f'{owner_address_short} ({chain_name})\n[Exp]({owner_exp_url})｜[OpenSea]({owner_os_url})',
            inline=True
        )
    for fee in fees:
        if fee['required'] == True:
            fee['required'] = 'Required'
        else:
            fee['required'] = 'Optional'

        fees_text += f"{fee['required']} [{fee['fee']}%]({exp_address_url}{fee['recipient']})\n"
    embed.add_field(name='Fees', value=fees_text, inline=True)
    embed.add_field(name='Verification',
                    value=verify_state, inline=True)
    embed.set_footer(
        text='Source: OpenSea API',
        icon_url='https://raw.githubusercontent.com/Xeift/Kizmeow-NFT-Discord-Bot/refs/heads/main/img/opensea_logo.png'
    )
    (success, collection_statistic_data) = get_os_collection_statistics(collection)
    if success:
        num_holders = collection_statistic_data['total']['num_owners']
        market_cap = round(
            collection_statistic_data['total']['market_cap'], 2)
        floor_price = round(
            collection_statistic_data['total']['floor_price'], 2)

        volume_all = round(
            collection_statistic_data['total']['volume'], 2)
        volume_1d = round(
            collection_statistic_data['intervals'][0]['volume'], 2)
        volume_1d_del = round(
            collection_statistic_data['intervals'][0]['volume_change'], 2)
        volume_7d = round(
            collection_statistic_data['intervals'][1]['volume'], 2)
        volume_7d_del = round(
            collection_statistic_data['intervals'][1]['volume_change'], 2)
        volume_30d = round(
            collection_statistic_data['intervals'][2]['volume'], 2)
        volume_30d_del = round(
            collection_statistic_data['intervals'][2]['volume_change'], 2)

        sales_all = round(
            collection_statistic_data['total']['sales'], 2)
        sales_1d = round(
            collection_statistic_data['intervals'][0]['sales'], 2)
        sales_7d = round(
            collection_statistic_data['intervals'][1]['sales'], 2)
        sales_30d = round(
            collection_statistic_data['intervals'][2]['sales'], 2)

        average_price_all = round(
            collection_statistic_data['total']['average_price'], 2)
        average_price_1d = round(
            collection_statistic_data['intervals'][0]['average_price'], 2)
        average_price_7d = round(
            collection_statistic_data['intervals'][1]['average_price'], 2)
        average_price_30d = round(
            collection_statistic_data['intervals'][2]['average_price'], 2)

        embed.add_field(
            name='Unique Holders',
            value=num_holders,
            inline=True
        )
        embed.add_field(
            name='Market Cap',
            value=f'{market_cap} {ticker}',
            inline=True
        )
        embed.add_field(
            name='Floor Price',
            value=f'{floor_price} {ticker}',
            inline=True
        )
        embed.add_field(
            name='Volume',
            value=(
                f'```1D  {str(volume_1d).ljust(12)}{ticker}({volume_1d_del}%)\n'
                f'7D  {str(volume_7d).ljust(12)}{ticker}({volume_7d_del}%)\n'
                f'30D {str(volume_30d).ljust(12)}{ticker}({volume_30d_del}%)\n'
                f'All {str(volume_all).ljust(12)}{ticker}```'
            ),
            inline=False
        )
        embed.add_field(
            name='Average Price',
            value=(
                f'`1D  {str(average_price_1d).ljust(8)} {ticker}`\n'
                f'`7D  {str(average_price_7d).ljust(8)} {ticker}`\n'
                f'`30D {str(average_price_30d).ljust(8)} {ticker}`\n'
                f'`All {str(average_price_all).ljust(8)} {ticker}`'
            ),
            inline=True
        )
        embed.add_field(
            name='Sales',
            value=(
                f'`1D  {str(sales_1d).ljust(8)} NFT`\n'
                f'`7D  {str(sales_7d).ljust(8)} NFT`\n'
                f'`30D {str(sales_30d).ljust(8)} NFT`\n'
                f'`All {str(sales_all).ljust(8)} NFT`'
            ),
            inline=True
        )

    return embed