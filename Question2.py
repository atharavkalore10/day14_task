import numpy as np

arr = np.random.randint(1, 51, 20)

print("Array:")
print(arr)

print("Minimum Value:", np.min(arr))
print("Index of Minimum:", np.argmin(arr))

print("Maximum Value:", np.max(arr))
print("Index of Maximum:", np.argmax(arr))

print("Sum:", np.sum(arr))
print("Mean:", np.mean(arr))
print("Standard Deviation:", np.std(arr))