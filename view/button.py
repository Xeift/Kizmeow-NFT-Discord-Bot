from discord import ButtonStyle, PartialEmoji
from discord.ui import Button


def opensea_button(url, text=None):
    return Button(
        label='OpenSea' if not text else text,
        style=ButtonStyle.link,
        url=url,
        emoji=PartialEmoji(
            name='opensea_logo',
            id=1326452492644515963
        )
    )

def etherscan_button(url, text=None):
    return Button(
        label='Etherscan' if not text else text,
        style=ButtonStyle.link,
        url=url,
        emoji=PartialEmoji(
            name='etherscan_logo',
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
            name='x_logo',
            id=1326452546742648862
        )
    )

def instagram_button(url, text=None):
    return Button(
        label='Instagram' if not text else text,
        style=ButtonStyle.link,
        url=url,
        emoji=PartialEmoji(
            name='instagram_logo',
            id=1326452562186211379
        )
    )

def blocknative_button(url, text=None):
    return Button(
        label='Blocknative' if not text else text,
        style=ButtonStyle.link,
        url=url,
        emoji=PartialEmoji(
            name='blocknative_logo',
            id=1341781218827698247
        )
    )

def wiki_button(url, text=None):
    return Button(
        label='Wiki' if not text else text,
        style=ButtonStyle.link,
        url=url,
        emoji='📖'
    )

def discord_button(url, text=None):
    return Button(
        label='Discord' if not text else text,
        style=ButtonStyle.link,
        url=url,
        emoji=PartialEmoji(
            name='discord_logo',
            id=1326452569882759200
        )
    )

def telegram_button(url, text = None):
    return Button(
        label='Telegram' if not text else text,
        style=ButtonStyle.link,
        url=url,
        emoji=PartialEmoji(
            name='telegram_logo',
            id=1326452582117281843
        )
    )

def exp_button(exp_name, url, exp_emoji):
    return Button(
        label=exp_name,
        style=ButtonStyle.link,
        url=url,
        emoji=PartialEmoji(
            name=f'{exp_name.lower()}_logo',
            id=exp_emoji
        )
    )