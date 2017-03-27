import matplotlib
matplotlib.use('qt5agg')
import matplotlib.pyplot as plt
import pandas as pd


def read_data(file):

    data = pd.read_csv(file)

    return data


def plot_bar_group(data, group, title, xlabel, ylabel):

    sizes = data.groupby(group).size()

    axes = sizes.plot.bar()
    axes.set_title(title)
    axes.set_xlabel(xlabel)
    axes.set_ylabel(ylabel)

    return axes


def plot_pie_group(data, group, title):

    sizes = data.groupby(group).size()

    axes = sizes.plot.pie(autopct='%1.1f%%')
    axes.set_title(title)
    axes.axis('equal')

    return axes


if __name__ == "__main__":

    with open("./census2011.csv", 'r') as f:
        data = read_data(f)

    plot_bar_group(
        data,
        'Region',
        'Frequencies of Resident Regions in 2011 Census',
        'Region',
        'Frequency',
    )

    plt.tight_layout()
    plt.show()

    plot_bar_group(
        data,
        'Occupation',
        'Frequencies of Resident Occupations in 2011 Census',
        'Occupation',
        'Frequency',
    )

    plt.tight_layout()
    plt.show()

    plot_pie_group(
        data,
        'Age',
        'Proportions of Resident Ages in 2011 Census',
    )

    plt.tight_layout()
    plt.show()

    plot_pie_group(
        data,
        'Economic Activity',
        'Proportions of Resident Economic Activity in 2011 Census',
    )

    plt.tight_layout()
    plt.show()
