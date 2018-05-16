import numpy as np
import matplotlib.pyplot as plt
import glob
from mpl_toolkits.basemap import Basemap, cm

h = 720
w = 1440
llcrnrlat = -89.875
llcrnrlon = -179.875
urcrnrlat = 89.875
urcrnrlon = 179.875
llcrnrlon_indo = 94
llcrnrlat_indo = -11
urcrnrlon_indo = 141
urcrnrlat_indo = 11
for spine in plt.gca().spines.values():
    spine.set_visible(False)

files = glob.glob('../data/npp/npp_aot550_edr_gridded_0.25_*.high.bin')
for file in files:
    Record = np.dtype(('float32', 1036800))
    aot = (np.fromfile(file, dtype=Record, count=2).astype('float')[
        0].reshape((h, w))*14.21)+6.088
    xstart = int(270 * 0.25)
    xend = int(321 * 0.25)
    ystart = int(78 * 0.25)
    yend = int(97 * 0.25)
    width = xend - xstart
    height = yend - ystart
    m = Basemap(projection='merc', llcrnrlon=llcrnrlon_indo, llcrnrlat=llcrnrlat_indo, urcrnrlon=urcrnrlon_indo, urcrnrlat=urcrnrlat_indo,
                resolution='l')
    lons = np.arange(llcrnrlon, urcrnrlon+0.25, 0.25)
    lats = np.arange(llcrnrlat, urcrnrlat+0.25, 0.25)
    lons, lats = np.meshgrid(lons,lats)
    x, y = m(lons, lats)
    aot = np.ma.masked_array(aot, aot < 0)
    cs = m.pcolormesh(x, y, aot,vmin=2, vmax=25,cmap=plt.get_cmap('jet'))
    date = file.split('_')[5].split('.')[0]
    pngout = '../static/img/viirs/pm25.'+date+'.png'
    plt.savefig(pngout, bbox_inches='tight', dpi=250, pad_inches=0,frameon=False,transparent=True)
    plt.clf()
    plt.cla()
    plt.close()
