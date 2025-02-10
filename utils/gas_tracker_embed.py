from discord import Embed


def gas_etherscan_embed(gas_data):
    gas_data = gas_data['result']
    low = float(gas_data['SafeGasPrice'])
    medium = float(gas_data['ProposeGasPrice'])
    high = float(gas_data['FastGasPrice'])
    gasUsedRatio = gas_data['gasUsedRatio'].split(',')
    gasUsedRatioText = ''
    for gas in gasUsedRatio:
        gasUsedRatioText += f'{float(gas) * 100:.2f}% '

    embed = Embed(color=0xFFA46E)
    embed.title = f'Gas Tracker'
    embed.add_field(name='🐢', value=f'{low:.2f} gwei')
    embed.add_field(name='🚗', value=f'{medium:.2f} gwei')
    embed.add_field(name='🚀', value=f'{high:.2f} gwei')
    embed.add_field(name='Last 5 block gas use ratio', value=gasUsedRatioText)

    # TODO: add gas source footer

    return embed