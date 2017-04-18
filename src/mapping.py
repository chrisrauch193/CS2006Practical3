"""This module contains a function to plot data on a map."""

import matplotlib.cm
from mpl_toolkits.basemap import Basemap
from matplotlib.patches import Polygon
from matplotlib.collections import PatchCollection
from matplotlib.colors import Normalize


def plot_population_map(df, region_path, figsize=(10, 20)):
    """Plot a map of population, broken down by region."""

    # Create axes and figure, with the map centred on England.
    fig, axes = plt.subplots(figsize=size)
    data_map = Basemap(
        resolution='i',  # c, l, i, h, f or None.
        projection='merc',
        lat_0=54.5,
        lon_0=-4.36,
        llcrnrlon=-6.0,
        llcrnrlat=49.5,
        urcrnrlon=2.0,
        urcrnrlat=55.2
    )

    # Draw general geography.
    data_map.drawmapboundary(fill_color='#46bcec')
    data_map.fillcontinents(color='#f2f2f2', lake_color='#46bcec')
    data_map.drawcoastlines()

    # Read in the shape file and record it in a more useful format.
    data_map.readshapefile(region_path, 'regions', color='none')
    regions = dict([(info['NAME'], shape) for info, shape in zip(data_map.regions_info, data_map.regions)])

    # Get populations in each region.
    region_counts = df.groupby('Region').size()

    # Create Polygon objects from shape file.
    shapes = [Polygon(np.array(regions[index]), True) for index in region_counts.index]

    # Define colour map and attach data to each region the appropriate colour.
    cmap = plt.get_cmap('Oranges')
    pc = PatchCollection(shapes, zorder=2)
    norm = Normalize()
    pc.set_facecolor(cmap(norm(region_counts)))
    axes.add_collection(pc)

    # Create mapper object to apply colour to shapes.
    mapper = matplotlib.cm.ScalarMappable(cmap=cmap)
    mapper.set_array(region_counts)
    plt.colorbar(mapper, shrink=0.4)

    # Set title and show.
    plt.title('Population by Region')
    plt.show()
