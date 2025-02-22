from discord import ButtonStyle, PartialEmoji
from discord.ui import Button

from view.button import (etherscan_button, instagram_button, opensea_button,
                         website_button, x_button)


def opensea_account_view(account_data, view, disable_link_button):
    address = account_data['address']
    username = account_data['username']
    opensea_url = f'https://opensea.io/{address}'
    etherscan_url = f'https://etherscan.io/address/{address}'
    website_url = account_data['website']
    social_media_accounts = account_data['social_media_accounts']


    view.add_item(opensea_button(opensea_url))
    view.add_item(etherscan_button(etherscan_url))
    if website_url: view.add_item(website_button(website_url))

    for social_media_account in social_media_accounts:
        platform = social_media_account['platform']
        username = social_media_account['username']

        if platform == 'twitter':
            x_url = f'https://x.com/{username}'
            view.add_item(x_button(x_url))
        elif platform == 'instagram':
            instagram_url=f'https://www.instagram.com/{username}'
            view.add_item(instagram_button(instagram_url))
    
    return view