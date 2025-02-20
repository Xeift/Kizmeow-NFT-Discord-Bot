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

    line_collection = LineCollection(
        segments,
        color=line_color,
        linewidth=2
    )
    ax.add_collection(line_collection)

    ax.scatter(
        range(len(gas_usage_rates)),
        gas_usage_rates,
        facecolor='none',
        edgecolor='white',
        s=50,
        linewidth=1.5,
        alpha=1,
        zorder=5
    )

    for i, txt in enumerate(gas_usage_rates):
        ax.annotate(
            f'{txt:.2f}', 
            (i, gas_usage_rates[i]), 
            textcoords='offset points', 
            xytext=(0, 10), 
            ha='center', 
            color='white', 
            fontsize=10
        )

    ax.set_xlim(-0.5, len(block_numbers) - 0.5)
    ax.set_ylim(min(gas_usage_rates) - 5, max(gas_usage_rates) + 5)

    plt.xlabel(
        'Block Number',
        fontsize=12,
        labelpad=10,
        color='#EDEDED'
    )
    plt.ylabel(
        'Gas Usage Rate (%)',
        fontsize=12,
        labelpad=10,
        color='#EDEDED'
    )
    plt.title(
        'Gas Usage Rate (Last 5 Blocks)',
        fontsize=14,
        pad=15,
        color='#EDEDED'
    )
    plt.xticks(
        np.arange(len(block_numbers)),
        block_numbers,
        fontsize=10,
        color='#EDEDED'
    )
    plt.yticks(
        fontsize=10,
        color='#EDEDED'
    )
    plt.grid(
        axis='y',
        linestyle='--',
        alpha=0.3,
        color='#A6A6A6'
    )

    plt.savefig(
        'tmp/gas_etherscan_plot.png',
        dpi=300,
        bbox_inches='tight'
    )


def gas_blocknative_plot(gas_data):
    confidences = [item["confidence"] for item in gas_data]
    maxFeePerGas = [item["maxFeePerGas"] for item in gas_data]
    maxPriorityFeePerGas = [item["maxPriorityFeePerGas"] for item in gas_data]

    color_maxFeePerGas = "#FFA46E"
    color_maxPriorityFeePerGas = "#FFFFFF"
    background_color = "#2E2E2E"

    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(5, 4))

    bar_width = 0.4
    index = np.arange(len(confidences))

    bars1 = ax1.bar(index, maxFeePerGas, bar_width, color=color_maxFeePerGas)

    fig.patch.set_facecolor(background_color)
    ax1.set_facecolor(background_color)

    ax1.set_title('Max Fee by Confidence', color='white')
    ax1.set_xlabel('Confidence', color='white')
    ax1.set_ylabel('Max Fee (Gwei)', color='white')

    ax1.set_xticks(index)
    ax1.set_xticklabels(confidences, color='white')

    y_min = min(maxFeePerGas) * 0.98
    y_max = max(maxFeePerGas) * 1.02
    ax1.set_ylim([y_min, y_max])

    ax1.tick_params(axis='y', colors='white')

    for i, v in enumerate(maxFeePerGas):
        ax1.text(i, v + 0.02, f'{v:.2f}', ha='center', color='white', fontsize=8)

    bars2 = ax2.bar(index, maxPriorityFeePerGas, bar_width, color=color_maxPriorityFeePerGas, alpha=0.5)

    ax2.set_facecolor(background_color)

    ax2.set_title('Max Priority Fee by Confidence', color='white')
    ax2.set_xlabel('Confidence', color='white')
    ax2.set_ylabel('Max Priority Fee (Gwei)', color='white')

    ax2.set_xticks(index)
    ax2.set_xticklabels(confidences, color='white')

    y_min2 = min(maxPriorityFeePerGas) * 0.98
    y_max2 = max(maxPriorityFeePerGas) * 1.02
    ax2.set_ylim([y_min2, y_max2])

    ax2.tick_params(axis='y', colors='white')

    for i, v in enumerate(maxPriorityFeePerGas):
        ax2.text(i, v + 0.001, f'{v:.3f}', ha='center', color='white', fontsize=8)

    plt.tight_layout(pad=3.0)
    plt.savefig('tmp/gas_blocknative_plot.png', dpi=300, bbox_inches='tight')
