import numpy as np

# NumPy’s array class is called "ndarray".
test_1 = [[0, 1, 2, 3, 4], [5, 6, 7, 8, 9], [10, 11, 12, 13, 14]]
test_2 = np.arange(0, 15, 1).reshape(3, 5)
print("test_1: ", test_1)
print("test_2: ", test_2)

# ndarray.shape
# the dimensions of the array. This is a tuple of integers indicating the
# size of the array in each dimension. For a matrix with n rows and m columns,
# shape will be (n,m). The length of the shape tuple is therefore the rank, or
#  number of dimensions, ndim.

print("test_2.shape :", test_2.shape)
