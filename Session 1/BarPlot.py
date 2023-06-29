import matplotlib.pyplot as plt

Years = [2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020, 2021]

Temperatures = [25.3,27.1,24.8,26.5,22.9,23.7,25.2,26.8,24.5,23.9,26.1,28.3]


plt.bar(Years,Temperatures,color = 'red')

plt.xlabel("Temperatures")

plt.ylabel("Years")

plt.title("iiii")

plt.legend(Years)

plt.show()





Sum = int(0)

for i in Temperatures:
    Sum += i

mid = int(Sum / 20)

print (mid)

Temperatures.sort()
print(Temperatures[0], Temperatures[-1])

print(Years[0], Years[-1])




