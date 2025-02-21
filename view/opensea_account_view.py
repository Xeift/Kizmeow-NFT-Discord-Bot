from discord import ButtonStyle, PartialEmoji
from discord.ui import Button


def opensea_account_view(account_data, view, disable_link_button):
    address = account_data['address']
    username = account_data['username']
    opensea_url = f'https://opensea.io/{address}'
    etherscan_url = f'https://etherscan.io/address/{address}'
    website_url = account_data['website']
    social_media_accounts = account_data['social_media_accounts']

    opensea_button = Button(
        label='OpenSea',
        style=ButtonStyle.link,
        url=opensea_url,
        emoji=PartialEmoji(name='opensea_icon_transparent',
                            id=1326452492644515963),
        disabled=disable_link_button
    )
    view.add_item(opensea_button)

    etherscan_button = Button(
        label='Etherscan',
        style=ButtonStyle.link,
        url=etherscan_url,
        emoji=PartialEmoji(name='etherscan_icon_transparent',
                            id=1326452528920920125),
        disabled=disable_link_button
    )
    view.add_item(etherscan_button)

    website_button = Button(
        label='Website',
        style=ButtonStyle.link,
        url=website_url,
        emoji='🔗',
        disabled=disable_link_button
    )
    if website_url != '':
        view.add_item(website_button)

    for social_media_account in social_media_accounts:
        platform = social_media_account['platform']
        username = social_media_account['username']

        if platform == 'twitter':
            x_button = Button(
                label='X',
                style=ButtonStyle.link,
                url=f'https://x.com/{username}',
                emoji=PartialEmoji(name='x_icon_transparent',
                                    id=1326452546742648862),
                disabled=disable_link_button
            )
            view.add_item(x_button)
        elif platform == 'instagram':
            instagram_button = Button(
                label='Instagram',
                style=ButtonStyle.link,
                url=f'https://www.instagram.com/{username}',
                emoji=PartialEmoji(
                    name='instagram_icon_transparent',
                    id=1326452562186211379
                ),
                disabled=disable_link_button
            )
            view.add_item(instagram_button)
    
    return view