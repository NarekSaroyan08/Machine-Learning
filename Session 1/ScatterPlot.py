import matplotlib.pyplot as plt

import random 

x = [random.random() for _ in range(50)]
y = [random.random() for _ in range(50)]

colors = [random.random() for _ in range(50)]

SIZES = [random.randint(10,100) for _ in range(50)]

plt.scatter(x,y, c = colors, s = SIZES,marker = 'o')

plt.xlable("X")
plt.ylable("Y")
plt.title(" " )

plt.grid(True)

plt.show()

