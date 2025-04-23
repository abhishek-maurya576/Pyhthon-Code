"""Array Attributes
ndim: Number of dimensions

shape: Shape of the array

size: Total number of elements

dtype: Data type

itemsize: Size of each item in bytes"""

import numpy as np
arr = np.array([[4,5,6,7,8],[1,2,3,4,5]])
print("Number of dimensions: ",arr.ndim)
print("Shape of the array",arr.shape)
print("Total number of elements: ",arr.size)
print("Data type: ",arr.dtype)
print("Size of each item in bytes: ",arr.itemsize)