from discord import Embed, File

from utils.plot import gas_etherscan_plot


def gas_etherscan_embed(gas_data):
    gas_data = gas_data['result']
    low = float(gas_data['SafeGasPrice'])
    medium = float(gas_data['ProposeGasPrice'])
    high = float(gas_data['FastGasPrice'])
    last_block = int(gas_data['LastBlock'])
    last_five_blocks = [last_block - i for i in range(4, -1, -1)]

    gas_used_ratio = gas_data['gasUsedRatio'].split(',')
    gas_used_ratio = [round(float(gur), 2) for gur in gas_used_ratio]

    embed = Embed(color=0xFFA46E)
    embed.title = f'Gas Tracker'
    embed.add_field(name='🐢', value=f'{low:.2f} gwei')
    embed.add_field(name='🚗', value=f'{medium:.2f} gwei')
    embed.add_field(name='🚀', value=f'{high:.2f} gwei')
    embed.add_field(name='Last 5 block gas use ratio', value=gas_used_ratio)

    # TODO: add gas source footer

    gas_etherscan_plot(last_five_blocks, gas_used_ratio)
    file = File('tmp/gas_etherscan_plot.png', filename='gas_etherscan_plot.png')
    embed.set_image(url='attachment://gas_etherscan_plot.png')

    return (embed, file)