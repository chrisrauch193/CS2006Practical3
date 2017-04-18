import matplotlib.cm
from mpl_toolkits.basemap import Basemap
from matplotlib.patches import Polygon
from matplotlib.collections import PatchCollection
from matplotlib.colors import Normalize


def plot_map(df):

    fig, axes = plt.subplots(figsize=(10, 20))
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

    data_map.drawmapboundary(fill_color='#46bcec')
    data_map.fillcontinents(color='#f2f2f2', lake_color='#46bcec')
    data_map.drawcoastlines()

    data_map.readshapefile('regions/regions', 'regions', color='none')

    regions = dict([(info['NAME'], shape) for info, shape in zip(data_map.regions_info, data_map.regions)])

    region_counts = df.groupby('Region').size()

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
