import numpy as np

arr1D = np.array([1,2,3,4,5])

arr2D = np.array([[1,2,3],[4,5,6]])

print(arr1D)
print(arr2D)

arr = np.array([1,2,3,4,5,6])

print(arr[-1])
x = [1,2,3]
y = [4,5,6]
print(x + y)


sum1 = np.array([1,2,3,4])

sum2 = np.array([5,6,7,8])

print(sum1 + sum2)
print(sum1 * sum2)

resizeArr = np.array([1,2,3,4,5,6])
print(resizeArr.reshape((2,3)))

statArr = np.array([1,2,3,4,5,6])

mean = np.mean(statArr)
max_val = np.max(statArr)
total = np.sum(statArr)
print("Mean =",mean,"Max =",max_val,"Total =",total)








































