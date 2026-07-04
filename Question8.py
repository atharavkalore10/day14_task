import numpy as np

A = np.array([
    [1,2,3],
    [4,5,6],
    [7,8,9]
])

B = np.array([
    [9,8,7],
    [6,5,4],
    [3,2,1]
])

# Element-wise multiplication
element = A * B

# Matrix multiplication
matrix = A @ B

print("Element-wise Multiplication:")
print(element)

print("\nMatrix Multiplication:")
print(matrix)

# Difference:
# * performs multiplication of corresponding elements.
# @ performs actual matrix multiplication.