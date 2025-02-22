from discord import ButtonStyle, PartialEmoji
from discord.ui import Button


def opensea_button(url, disable_link_button):
    return Button(
        label='OpenSea',
        style=ButtonStyle.link,
        url=url,
        emoji=PartialEmoji(
            name='opensea_icon',
            id=1326452492644515963
        ),
        disabled=disable_link_button
    )