import numpy as np

arr = np.array([
    [10, 20, 30, 40],
    [50, 60, 70, 80],
    [90, 100, 110, 120]
])

print("Array:")
print(arr)

print("\nFirst Row:")
print(arr[0])

print("\nLast Column:")
print(arr[:, -1])

print("\nCenter 2x2 Submatrix:")
print(arr[1:3, 1:3])

print("\nEven Numbers:")
print(arr[arr % 2 == 0])