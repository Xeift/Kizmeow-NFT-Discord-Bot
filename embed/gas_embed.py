import time

from discord import Embed, File

from utils.plot import gas_blocknative_plot, gas_etherscan_plot


def gas_etherscan_embed(gas_data):
    gas_data = gas_data['result']
    low = float(gas_data['SafeGasPrice'])
    medium = float(gas_data['ProposeGasPrice'])
    high = float(gas_data['FastGasPrice'])
    suggested = float(gas_data['suggestBaseFee'])
    last_block = int(gas_data['LastBlock'])
    last_five_blocks = [last_block - i for i in range(4, -1, -1)]

    gas_used_ratio = gas_data['gasUsedRatio'].split(',')
    gas_used_ratio = [round(float(gur) * 100, 2) for gur in gas_used_ratio]

    embed = Embed(color=0xFFA46E, title='Gas Tracker')
    embed.add_field(name='🐢', value=f'{low:.2f} gwei')
    embed.add_field(name='🚗', value=f'{medium:.2f} gwei')
    embed.add_field(name='🚀', value=f'{high:.2f} gwei')
    embed.add_field(name='Suggested base fee', value=f'{suggested:.2f} gwei')

    embed.set_footer(
        text='Source: Etherscan API',
        icon_url='https://raw.githubusercontent.com/Xeift/Kizmeow-NFT-Discord-Bot/refs/heads/main/img/etherscan_logo.png'
    )

    gas_etherscan_plot(last_five_blocks, gas_used_ratio)
    file = File('tmp/gas_etherscan_plot.png', filename='gas_etherscan_plot.png')
    embed.set_image(url='attachment://gas_etherscan_plot.png')


    return (embed, file)

def gas_blocknative_embed(gas_data):
    block_price = gas_data['blockPrices'][0]
    unit = gas_data['unit']
    max_price = gas_data['maxPrice']
    last_update = int(time.time() - (gas_data['msSinceLastBlock'] / 1000))
    current_block = gas_data['currentBlockNumber']
    pending_block = block_price['blockNumber']
    

    txn_count = block_price['estimatedTransactionCount']
    base_fee = block_price['baseFeePerGas']
    blob_fee = block_price.get('blobBaseFeePerGas')

    estimated_prices = block_price['estimatedPrices']
    priority_fee = estimated_prices[0]['maxPriorityFeePerGas']
    max_fee = estimated_prices[0]['maxFeePerGas']

    embed = Embed(color=0xFFA46E, title='Gas Tracker')

    embed.add_field(name='Base Fee', value=f'{base_fee:.2f} {unit}')
    embed.add_field(name='Priority Fee', value=f'{priority_fee:.2f} {unit}')
    embed.add_field(name='Max Fee', value=f'{max_fee:.2f} {unit}')

    if blob_fee:
        embed.add_field(name='Blob Fee', value=f'{blob_fee:.5f} {unit}')
    embed.add_field(name='Last Update', value=f'<t:{last_update}:R>')
    embed.add_field(name='Current Block → Pending Block', value=f'{current_block} → {pending_block}')
    
    embed.add_field(name='Max Price In Pending Block', value=f'{max_price} {unit}')
    embed.add_field(name='Transaction In Pending Block', value=f'{txn_count}')
    
    embed.set_footer(
        text='Source: Blocknative API',
        icon_url='https://raw.githubusercontent.com/Xeift/Kizmeow-NFT-Discord-Bot/refs/heads/main/img/blocknative_logo.png'
    )

    gas_blocknative_plot(estimated_prices)
    file = File('tmp/gas_blocknative_plot.png', filename='gas_blocknative_plot.png')
    embed.set_image(url='attachment://gas_blocknative_plot.png')

    return (embed, file)
