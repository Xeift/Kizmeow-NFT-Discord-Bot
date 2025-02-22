from discord import ButtonStyle, PartialEmoji
from discord.ui import Button


def opensea_button(url, text=None):
    return Button(
        label='OpenSea' if not text else text,
        style=ButtonStyle.link,
        url=url,
        emoji=PartialEmoji(
            name='opensea_icon_transparent',
            id=1326452492644515963
        )
    )

def etherscan_button(url, text=None):
    return Button(
        label='Etherscan' if not text else text,
        style=ButtonStyle.link,
        url=url,
        emoji=PartialEmoji(
            name='etherscan_icon_transparent',
            id=1326452528920920125
        )
    )

def website_button(url, text=None):
    return Button(
        label='Website' if not text else text,
        style=ButtonStyle.link,
        url=url,
        emoji='🔗'
    )

def x_button(url, text=None):
    return Button(
        label='X' if not text else text,
        style=ButtonStyle.link,
        url=url,
        emoji=PartialEmoji(
            name='x_icon_transparent',
            id=1326452546742648862
        )
    )

def instagram_button(url, text=None):
    return Button(
        label='Instagram' if not text else text,
        style=ButtonStyle.link,
        url=url,
        emoji=PartialEmoji(
            name='instagram_icon_transparent',
            id=1326452562186211379
        )
    )