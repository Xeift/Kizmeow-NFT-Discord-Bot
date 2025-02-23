from discord import Embed


def settings_embed():
    return Embed(
        title='User settings',
        description=f'Click the dropdown menu below to set the bot.',
        color=0xffa46e
    )