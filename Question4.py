import numpy as np

arr = np.arange(1, 25)

print("Original Array:")
print(arr)

arr1 = arr.reshape(4, 6)
arr2 = arr.reshape(3, 8)
arr3 = arr.reshape(2, 3, 4)

print("\n4 x 6")
print(arr1)
print("Shape:", arr1.shape)

print("\n3 x 8")
print(arr2)
print("Shape:", arr2.shape)

print("\n2 x 3 x 4")
print(arr3)
print("Shape:", arr3.shape)