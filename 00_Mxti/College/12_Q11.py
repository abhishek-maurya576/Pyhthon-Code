'''
Problem 11: NumPy Array Creation and Attributes
Task:
Import NumPy.
Create a 1D NumPy array from the Python list [1, 2, 3, 4, 5].
Create a 2x3 NumPy array filled with zeros.
Create a 3x2 NumPy array filled with ones, specifying the data type as float64.
Create a 1D NumPy array using arange that goes from 0 to 10 (exclusive) with a step of 2.
Create a 1D NumPy array using linspace that has 5 points between 0 and 1 (inclusive).
For each created array, print its ndim, shape, size, and dtype.
Briefly comment on why NumPy arrays are generally more efficient than Python lists for numerical operations (relating to homogeneity and underlying implementation).
'''
import numpy as np
lst =[1, 2, 3, 4, 5]
d1 = np.array(lst)
zeros = np.zeros((2,3),dtype = int)
print(f"array: {d1}, \ndimension of the array: {d1.ndim},\nsize of the array: {d1.size},\nshape of the array: {d1.shape},\ndtype of the array: {d1.dtype},\nType of the array: {type(d1)}")
print(f"\narray: {zeros}, \ndimension of the array: {zeros.ndim},\nsize of the array: {zeros.size},\nshape of the array: {zeros.shape},\ndtype of the array: {zeros.dtype},\nType of the array: {type(zeros)}")
ones = np.ones((3,2),dtype = np.float64)
print(f"\narray: {ones}, \ndimension of the array: {ones.ndim},\nsize of the array: {ones.size},\nshape of the array: {ones.shape},\ndtype of the array: {ones.dtype},\nType of the array: {type(ones)}")
one_d = np.arange(0,11,2)
print(f"\narray: {one_d}, \ndimension of the array: {one_d.ndim},\nsize of the array: {one_d.size},\nshape of the array: {one_d.shape},\ndtype of the array: {one_d.dtype},\nType of the array: {type(one_d)}")
one_d_lin = np.linspace(1,0,5)
print(f"\narray: {one_d_lin}, \ndimension of the array: {one_d_lin.ndim},\nsize of the array: {one_d_lin.size},\nshape of the array: {one_d_lin.shape},\ndtype of the array: {one_d_lin.dtype},\nType of the array: {type(one_d_lin)}")
