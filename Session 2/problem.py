import numpy as np

Array = np.array()

a = random.rand(1,20)
b = random.rand(50,70)
c = random.rand(5,15)

for _ in range(c) :
    np.append(Array,random.rand(a,b),axis = None)

print(Array)
