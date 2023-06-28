import matplotlib.pyplot as plt

import random



random.seed(42)

data = [random.random() for _ in range (1000)]

plt.hist(data, bins = 30, color = "aqua", alpha = 0.5)

plt.xlabel("Value")
plt.ylabel("Frequency")
plt.title("Histogram")

plt.show()








