import numpy as np
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import glob
import os


def plotimage(lats, lons, values, range, pngout):
    llcrnrlon_indo = 94
    llcrnrlat_indo = -11
    urcrnrlon_indo = 141
    urcrnrlat_indo = 11
    m = Basemap(projection='merc', llcrnrlon=llcrnrlon_indo, llcrnrlat=llcrnrlat_indo, urcrnrlon=urcrnrlon_indo,
                urcrnrlat=urcrnrlat_indo, resolution='c')
    x, y = m(lons, lats)
    sc = m.scatter(x, y,marker=',', c=values, s=8, cmap='jet', vmin=range[0], vmax=range[1])
    for spine in plt.gca().spines.values():
        spine.set_visible(False)
    plt.savefig(pngout, bbox_inches='tight', dpi=250, pad_inches=0, frameon=False, transparent=True)
    plt.clf()
    plt.cla()
    plt.close()


def loadimage():
    files = glob.glob('../data/nucaps/nucaps.*.txt')
    for file in files:
        print('converting ' + file)
        infoname = file.split('.')
        time = infoname[3]
        yyyy = time[0:4]
        mm = time[4:6]
        dd = time[6:8]
        folder = '{}/{}'.format(yyyy, mm)
        type = infoname[3]
        lats = []
        lons = []
        co = []
        so2 = []
        o3 = []
        with open(file, 'r') as text:
            strfile = text.read()
            rows = strfile.split('\n')
            for row in rows:
                datas = row.split('\t')
                if len(datas) > 2:
                    lats.append(float(datas[0]))
                    lons.append(float(datas[1]))
                    co.append(float(datas[2]))
                    so2.append(float(datas[3]))
                    o3.append(float(datas[4]))
        lats = np.asarray(lats, float)
        lons = np.asarray(lons, float)
        co = np.asarray(co, float)
        so2 = np.asarray(so2, float)
        o3 = np.asarray(o3, float)
        plotimage(lats, lons, co, (50, 150), '../static/img/cris/co.' + yyyy + '' + mm + '' + dd + '.png')
        plotimage(lats, lons, so2, (15, 20), '../static/img/cris/o3.' + yyyy + '' + mm + '' + dd + '.png')
        plotimage(lats, lons, o3, (0.1, 0.4), '../static/img/cris/so2.' + yyyy + '' + mm + '' + dd + '.png')


if __name__ == '__main__':
    loadimage()
