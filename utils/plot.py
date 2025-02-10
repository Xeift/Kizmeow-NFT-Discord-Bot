import matplotlib.pyplot as plt
import numpy as np
from matplotlib.collections import LineCollection


def gas_etherscan_plot(block_numbers, gas_usage_rates):
    line_color = '#FFA46E'
    points = np.array([list(range(len(gas_usage_rates))), gas_usage_rates]).T.reshape(-1, 1, 2)
    segments = np.concatenate([points[:-1], points[1:]], axis=1)
    fig, ax = plt.subplots(figsize=(5, 3))
    fig.patch.set_facecolor('#2E2E2E')
    ax.set_facecolor('#2E2E2E')

    line_collection = LineCollection(segments, color=line_color, linewidth=2)
    ax.add_collection(line_collection)

    ax.scatter(range(len(gas_usage_rates)), gas_usage_rates, facecolor='none', edgecolor='white', s=50, linewidth=1.5, alpha=1, zorder=5)

    for i, txt in enumerate(gas_usage_rates):
        ax.annotate(f'{txt:.2f}', 
                    (i, gas_usage_rates[i]), 
                    textcoords="offset points", 
                    xytext=(0, 10), 
                    ha='center', 
                    color='white', 
                    fontsize=10)

    ax.set_xlim(-0.5, len(block_numbers) - 0.5)
    ax.set_ylim(min(gas_usage_rates) - 5, max(gas_usage_rates) + 5)

    plt.xlabel('Block Number', fontsize=12, labelpad=10, color='#EDEDED')
    plt.ylabel('Gas Usage Rate (%)', fontsize=12, labelpad=10, color='#EDEDED')
    plt.title('Gas Usage Rate (Last 5 Blocks)', fontsize=14, pad=15, color='#EDEDED')
    plt.xticks(np.arange(len(block_numbers)), block_numbers, fontsize=10, color='#EDEDED')
    plt.yticks(fontsize=10, color='#EDEDED')
    plt.grid(axis='y', linestyle='--', alpha=0.3, color='#A6A6A6')

    plt.savefig('tmp/gas_etherscan_plot.png', dpi=300, bbox_inches='tight')
