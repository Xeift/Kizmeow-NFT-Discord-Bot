import json

from discord import Embed

from utils.chain import get_info_by_code
from utils.datetime_to_timestamp import datetime_to_timestamp


def opensea_nft_embed(chain, nft_data):
    embed = Embed(color=0xFFA46E)
    (
        chain_name,
        _,
        exp_address_url,
        exp_token_url,
        _,
        _,
        token_standards
    ) = get_info_by_code(chain)

    with open('collection_name_data.json', 'r', encoding='utf-8') as of:
        collection_name_data = json.load(of)
    nft_name = nft_data['name']
    contract = nft_data['contract']
    contract_address_short = contract[:7]
    contract_exp_url = f'{exp_token_url}{contract}'

    token_standard = nft_data['token_standard']
    for ts in token_standards:
        if token_standard == ts:
            token_standard = token_standards[ts]
            break

    collection = nft_data['collection']
    for c in collection_name_data:
        if collection_name_data[c]['slug'] == collection:
            collection = c
            break
    identifier = nft_data['identifier']
    if len(identifier) > 7:
        identifier = identifier[:7]

    if nft_name == None:
        nft_name = f'{collection}#{identifier}'

    display_img_url = nft_data['display_image_url']
    last_update_time = datetime_to_timestamp(nft_data['updated_at'])

    # is_disabled = nft_data['is_disabled']
    # is_nsfw = nft_data['is_nsfw']
    # is_suspicious = nft_data['is_suspicious']

    creator_address = nft_data['creator']
    if creator_address != None:
        creator_address_short = creator_address[:7]
        creator_os_url = f'https://www.opensea.io/{creator_address}'

    owners = nft_data['owners']
    owner_text = ''
    if owners == None:
        owner_text = '(Too much owners!)'
    elif len(owners) == 1:
        owner = owners[0]
        owner_address = owner['address']
        owner_address_short = owner['address'][:7]
        owner_exp_url = f'{exp_address_url}{owner_address}'
        owner_os_url = f'https://www.opensea.io/{owner_address}'
        owner_text = f'{owner_address_short}\n[Exp]({owner_exp_url})｜[OpenSea]({owner_os_url})'
    elif len(owners) <= 5:
        for owner in owners:
            owner_address = owner['address']
            owner_address_short = owner['address'][:7]
            owner_exp_url = f'{exp_address_url}{owner_address}'
            owner_os_url = f'https://www.opensea.io/{owner_address}'
            owner_text += f'{owner_address_short} [Exp]({owner_exp_url})｜[OpenSea]({owner_os_url})\n'
    else:
        owner_text = f'({len(owners)} owners)'

    rarity_rk = 0
    if nft_data['rarity'] != None:
        rarity_rk = nft_data['rarity']['rank']

    embed.title = nft_name
    embed.set_image(url=display_img_url)
    embed.set_footer(
        text='Source: OpenSea API',
        icon_url='https://raw.githubusercontent.com/Xeift/Kizmeow-NFT-Discord-Bot/refs/heads/main/img/opensea_logo.png'
    )
    embed.add_field(
        name='Contract Address',
        value=f'[{contract_address_short}]({contract_exp_url})',
    )
    embed.add_field(
        name='Owner',
        value=owner_text
    )
    if creator_address != None:
        embed.add_field(
            name='Creator',
            value=f'{creator_address_short}\n[Exp]({exp_address_url}{creator_address})｜[OpenSea]({creator_os_url})'
        )
    embed.add_field(
        name='Chain',
        value=chain_name
    )
    embed.add_field(
        name='Token Standard',
        value=token_standard
    )
    if rarity_rk != 0:
        embed.add_field(
            name='Rarity Rank',
            value=rarity_rk
        )

    embed.add_field(
        name='Last Update Time',
        value=f'<t:{last_update_time}:D>'
    )

    embed.add_field(
        name='════════════    Traits    ════════════',
        value='',
        inline=False
    )
    traits = nft_data['traits']
    if traits != None:
        for trait in traits:
            type = trait['trait_type']
            value = trait['value']

            embed.add_field(
                name=type,
                value=value if value != None else ''
            )

    return embed