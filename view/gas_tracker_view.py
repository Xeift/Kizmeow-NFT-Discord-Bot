from discord import ButtonStyle, PartialEmoji
from discord.ui import Button


def gas_etherscan_view(view):
    etherscan_button = Button(
        label='Etherscan Gas Tracker',
        style=ButtonStyle.link,
        url='https://etherscan.io/gastracker',
        emoji=PartialEmoji(
            name='etherscan_icon',
            id=1326452528920920125
        )
    )
    view.add_item(etherscan_button)

    return view

def gas_blocknative_view(view):
    blocknative_button = Button(
        label='Blocknative Gas Tracker',
        style=ButtonStyle.link,
        url='https://www.blocknative.com/gas-estimator',
        emoji=PartialEmoji(
            name='blocknative_icon',
            id=1341781218827698247
        )
    )
    view.add_item(blocknative_button)

    return view