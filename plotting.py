import matplotlib
#matplotlib.use('qt5agg')
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import pandas as pd
import textwrap


def plot_bar_group_count(
        data, field, title, title_pad=1.05, label_pad=15, wrap_chars=10
):

    sizes = data.groupby(field).size()

    axes = sizes.plot.barh()
    axes.set_title(title, y=title_pad)
    axes.set_xlabel("Frequency", labelpad=label_pad)
    axes.set_ylabel(field, labelpad=label_pad)

    labels = ['\n'.join(textwrap.wrap(str(label), wrap_chars, break_long_words=False)) for label in sizes.keys()]
    axes.set_yticklabels(labels)

    return axes


def plot_pie_group_count(
        data, field, title, percent_format="%1.1f%%", title_pad=1.05
):

    sizes = data.groupby(field).size()

    axes = sizes.plot.pie(autopct=percent_format)
    axes.set_title(title, y=title_pad)
    axes.set_ylabel('')
    axes.axis("equal")

    return axes


def plot_3d_table_count(
        data, field_1, field_2, title, xlabel, ylabel, title_pad=1.05,
        label_pad=10, alpha=0.8, wrap_chars=15
):

    freq = pd.crosstab(data[field_1], data[field_2])
    x_grid, y_grid = np.meshgrid(range(len(freq.index)), range(len(freq.columns)))

    axes = plt.axes(projection="3d")

    for x, y, z in zip(x_grid, y_grid, np.array(freq).T):
        axes.bar(x, z, zs=y, zdir='y', alpha=alpha)

    axes.set_title(title, y=title_pad)
    axes.set_xlabel(xlabel, labelpad=label_pad)
    axes.set_ylabel(ylabel, labelpad=label_pad)
    axes.set_zlabel("Frequency", labelpad=label_pad)
    axes.set_xticks(range(len(freq.index)), minor=True)
    axes.set_yticks(range(len(freq.columns)), minor=True)

    x_labels = ['\n'.join(textwrap.wrap(str(label), wrap_chars, break_long_words=False)) for label in freq.index]
    y_labels = ['\n'.join(textwrap.wrap(str(label), wrap_chars, break_long_words=False)) for label in freq.columns]

    axes.set_xticklabels(x_labels)
    axes.set_yticklabels(y_labels)

    return axes


if __name__ == "__main__":

    from utils import read_data
    with open("./translated.csv", 'r') as f:
        data = read_data(f)

    plt.style.use('ggplot')

    # plt.figure(figsize=(10, 10))
    # plot_3d_table_count(
    #     data,
    #     'Region',
    #     'Industry',
    #     'Frequencies Residents by Region and Industry in 2011 Census',
    #     'Region',
    #     'Industry',
    # )
    # plt.show()
    #
    # plt.figure(figsize=(12, 9))
    # plot_bar_group_count(
    #     data,
    #     'Region',
    #     'Frequencies of Resident Regions in 2011 Census',
    # )
    # plt.show()
    #
    # plt.figure(figsize=(15, 9))
    # plot_bar_group_count(
    #     data,
    #     'Occupation',
    #     'Frequencies of Resident Occupations in 2011 Census',
    # )
    # plt.show()
    #
    # plt.figure(figsize=(12, 9))
    # plot_pie_group_count(
    #     data,
    #     'Age',
    #     'Proportions of Resident Ages in 2011 Census',
    # )
    # plt.show()
    #
    # plt.figure(figsize=(12, 9))
    # plot_pie_group_count(
    #     data,
    #     'Economic Activity',
    #     'Proportions of Resident Economic Activity in 2011 Census',
    # )
    # plt.show()

    import matplotlib.cm

    from mpl_toolkits.basemap import Basemap
    from matplotlib.patches import Polygon
    # from shapely.geometry import Point, Polygon, MultiPoint, MultiPolygon
    # from shapely.prepared import prep
    from matplotlib.collections import PatchCollection
    from matplotlib.colors import Normalize

    fig, axes = plt.subplots(figsize=(10, 20))

    map = Basemap(
        resolution='i',     # c, l, i, h, f or None.
        projection='merc',  # Mercator projection.
        lat_0=54.5,
        lon_0=-4.36,
        llcrnrlon=-6.0,
        llcrnrlat=49.5,
        urcrnrlon=2.0,
        urcrnrlat=55.2
    )

    map.drawmapboundary(fill_color='#46bcec')
    map.fillcontinents(color='#f2f2f2', lake_color='#46bcec')
    map.drawcoastlines()

    map.readshapefile('regions/regions', 'regions', color='none')

    import pysal
    shp = pysal.open('regions/regions.shp')
    polys = list(shp)


    regions = dict([(info['NAME'], shape) for info, shape in zip(map.regions_info, map.regions)])

    region_counts = data.groupby('Region').size()

    shapes = [Polygon(np.array(regions[index]), True) for index in region_counts.index]

    cmap = plt.get_cmap('Oranges')
    pc = PatchCollection(shapes, zorder=2)
    norm = Normalize()

    pc.set_facecolor(cmap(norm(region_counts)))
    axes.add_collection(pc)

    mapper = matplotlib.cm.ScalarMappable(cmap=cmap)

    mapper.set_array(region_counts)
    plt.colorbar(mapper, shrink=0.4)

    plt.title('Population by Region')

    plt.show()

    # England: http://129.215.55.209/handle/10672/50
    # Wales: http://datashare.is.ed.ac.uk/handle/10283/2410

    # Try: http://www.geophysique.be/2013/02/12/matplotlib-basemap-tutorial-10-shapefiles-unleached-continued/
    # https://github.com/brandomr/pythonmap/blob/master/SL%20Map.ipynb
