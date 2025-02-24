from discord import Embed
from web3 import Web3
def address_converter_embed(address):
    embed = Embed(
        color=0xFFA46E,
        title='Address converter'
    )
    embed.add_field(
        name='Checksum address',
        value=f'```{Web3.to_checksum_address(address)}```'
    )
    embed.add_field(
        name='Lower case address',
        value=f'```{address.lower()}```'
    )
    embed.add_field(
        name='Upper case address',
        value=f'```{address.upper()}```'
    )

    return embed
