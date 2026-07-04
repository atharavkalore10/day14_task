import numpy as np

# Create a 5x6 array with random integers between 10 and 100
arr = np.random.randint(10, 101, size=(5, 6))

print("Array:")
print(arr)

print("Shape:", arr.shape)
print("Size:", arr.size)
print("Data Type:", arr.dtype)