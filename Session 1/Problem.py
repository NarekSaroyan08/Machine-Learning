import matplotlib.pyplot as plt

plt.style.use('_mpl-gallery')

xs = [2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020,2021]
ys = [25.3,27.1,24.8,26.5,22.9,23.7,25.2,26.8,24.5,23.9,26.1,28.3]
zs = [33.1,29.6,30.2,29.9,31.9,31.8,27.8,32.6,33.2,31.8,20.6,25.4]

fig, ax = plt.subplots(subplot_kw={"projection": "3d"})

ax.scatter(xs, ys, zs)

ax.set(xticklabels=[],yticklabels=[],zticklabels=[])


plt.show()


















