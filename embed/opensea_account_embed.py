from discord import Embed


def opensea_account_embed(account_data):
    embed = Embed(color=0xFFA46E)
    address = account_data['address']
    username = account_data['username']
    bio = account_data['bio']
    joined_date = account_data['joined_date']
    short_address = account_data['address'][:7]
    pfp_img = account_data['profile_image_url']
    banner_img = account_data['banner_image_url']
    etherscan_url = f'https://etherscan.io/address/{address}'

    embed.title = f'OpenSea Account Info of {short_address}'
    embed.set_thumbnail(url=pfp_img)
    if banner_img != '':
        embed.set_image(url=banner_img)
    embed.set_footer(
        text='Source: OpenSea API',
        icon_url='https://raw.githubusercontent.com/Xeift/Kizmeow-NFT-Discord-Bot/refs/heads/main/img/opensea_logo.png'
    )

    embed.add_field(
        name='Address',
        value=f'[{address}]({etherscan_url})',
        inline=False
    )
    embed.add_field(name='Username', value=username, inline=True)
    embed.add_field(name='Bio', value=bio, inline=True)
    embed.add_field(name='Joined Date', value=joined_date, inline=True)

    return embed