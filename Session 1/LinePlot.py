import matplotlib.pyplot as plt


years = [2010,2012,2014,2016,2018,2020,2022]

population = [8.5, 10.4, 9.8, 10.9, 9.5, 5.8, 10.6]

plt.plot(years,population, marker = "o", linestyle = "--", color = "green")

plt.xlabel("Years")

plt.ylabel("Population (in billions)")

plt.title("Production Growth Iver Yeras")

plt.show()
