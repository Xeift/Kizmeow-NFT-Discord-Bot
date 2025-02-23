from discord import Embed


def ping_embed(latency):
    return Embed(
        title='Bot Latency',
        description=f'{latency * 1000:.2f} ms ({latency:.2f} s)',
        color=0xFFA46E
    )