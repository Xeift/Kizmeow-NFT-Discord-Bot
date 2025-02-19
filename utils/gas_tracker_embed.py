from discord import Embed, File

from utils.plot import gas_etherscan_plot


embed = Embed(color=0xFFA46E)
embed.title = f'Gas Tracker'

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
    block_prices = gas_data['blockPrices'][0]
    unit = gas_data['unit']
    max_price = gas_data['maxPrice']
    current_block = gas_data['currentBlockNumber']
    pending_block = block_prices['blockNumber']

    txn_count = block_prices['estimatedTransactionCount']
    base_fee = block_prices['baseFeePerGas']
    blob_fee = block_prices['blobBaseFeePerGas']

    estimated_prices = block_prices['estimatedPrices']
    print(estimated_prices)

    
    return (embed, None)
