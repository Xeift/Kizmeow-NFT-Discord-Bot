from discord import ButtonStyle, PartialEmoji
from discord.ui import Button, View


def gas_etherscan_view():
    view = View()
    etherscan_button = Button(
        label='Etherscan Gas Tracker',
        style=ButtonStyle.link,
        url='https://etherscan.io/gastracker',
        emoji=PartialEmoji(
            name='etherscan_icon_transparent',
            id=1326452528920920125
        )
    )
    view.add_item(etherscan_button)

    return view