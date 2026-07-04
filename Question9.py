import numpy as np

arr = np.random.randn(6, 6)

print("Matrix:")
print(arr)

print("Shape:", arr.shape)
print("Size:", arr.size)
print("Data Type:", arr.dtype)

print("Maximum Index:", np.argmax(arr))
print("Minimum Index:", np.argmin(arr))

print("\nTop Left 3x3 Matrix:")
print(arr[:3, :3])

arr[arr < 0] = np.abs(arr[arr < 0])

print("\nModified Matrix:")
print(arr)

print("Mean:", np.mean(arr))