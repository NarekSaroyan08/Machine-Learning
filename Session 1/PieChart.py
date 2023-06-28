import matplotlib.pyplot as plt

categories = ["Categoria A", "Categoria B", "Categoria C", "Categoria D", "Categories E"]


percentages = [25,15,15,35,10]
explode = [0,0.1,0,0,0]

colors = ["red", "blue", "green", "orange", "aqua"]

plt.pie(percentages,explode = explode, labels = categories,colors = colors, shadow = True)

plt.legend(categories)

plt.show()
