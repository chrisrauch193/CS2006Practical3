"""Module for plotting two-way frequency tables as a 3D plot."""

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import pandas as pd
import textwrap


def plot_3d_table_count(
        data, field_1, field_2, title, xlabel, ylabel, title_pad=1.05,
        label_pad=20, alpha=0.8, wrap_chars=15, rotation=(30, 150)
):

    # Get frequency table.
    freq = pd.crosstab(data[field_1], data[field_2])

    # Create the grids giving the x and y values for each datapoint.
    x_grid, y_grid = np.meshgrid(range(len(freq.index)), range(len(freq.columns)))

    # Plot on 3D axes.
    axes = plt.axes(projection="3d")
    for x, y, z in zip(x_grid, y_grid, np.array(freq).T):
        axes.bar(x, z, zs=y, zdir='y', alpha=alpha)

    # Set relevant annotations.
    axes.set_title(title, y=title_pad)
    axes.set_xlabel(xlabel, labelpad=label_pad)
    axes.set_ylabel(ylabel, labelpad=label_pad)
    axes.set_zlabel("Frequency", labelpad=label_pad)
    axes.set_xticks(range(len(freq.index)))
    axes.set_yticks(range(len(freq.columns)))

    # Choose the labels.
    x_labels = ['\n'.join(textwrap.wrap(str(label), wrap_chars, break_long_words=False)) for label in freq.index]
    y_labels = ['\n'.join(textwrap.wrap(str(label), wrap_chars, break_long_words=False)) for label in freq.columns]

    # Set labels and viewing angle.
    axes.set_xticklabels(x_labels)
    axes.set_yticklabels(y_labels)
    axes.view_init(*rotation)

    return axes
