import numpy as np

# Creating two 3x3 matrices
matrix_a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
matrix_b = np.array([[9, 8, 7], [6, 5, 4], [3, 2, 1]])

print("Matrix A:")
print(matrix_a)

print("\nMatrix B:")
print(matrix_b)

# Matrix addition
matrix_sum = np.add(matrix_a, matrix_b)
print("\nSum of A and B:")
print(matrix_sum)

# Matrix multiplication (element-wise)
matrix_multiply = np.multiply(matrix_a, matrix_b)
print("\nElement-wise multiplication of A and B:")
print(matrix_multiply)

# Matrix dot product
matrix_dot_product = np.dot(matrix_a, matrix_b)
print("\nDot product of A and B:")
print(matrix_dot_product)

# Matrix transpose
matrix_transpose = np.transpose(matrix_a)
print("\nTranspose of Matrix A:")
print(matrix_transpose)
