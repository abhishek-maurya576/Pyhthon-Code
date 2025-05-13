'''
Problem 13: Reshaping NumPy Arrays
Task:
Create a 1D NumPy array using arange with 12 elements (e.g., from 0 to 11).
Print the initial array and its shape.
Use the reshape() method to reshape this 1D array into a 2D array with 3 rows and 4 columns. Print the reshaped array and its shape.
Reshape the original 1D array into a 2D array with 4 rows and 3 columns. Print this new reshaped array and its shape.
Reshape the original 1D array into a 3D array with shape (2, 2, 3). Print this array and its shape.
Attempt to reshape the original 1D array into a shape that doesn't match the total number of elements (e.g., (3, 5)). Explain the error you get.
'''
import numpy as np
arr = np.arange(12)
print(f"array: {arr}\nshape: {arr.shape}")
d2 = arr.reshape(3,4)
print(f"array: {d2}\nshape: {d2.shape}")
arr2 = arr.reshape(4,3)
print(f"array: {arr2}\nshape: {arr2.shape}")
arr3 = arr.reshape(2,2,3)
print(f"array: {arr3}\nshape: {arr3.shape}")
try:
    arr3 = arr.reshape(3,5)
    print(f"array: {arr3}\nshape: {arr3.shape}")
except (ValueError):
    print(ValueError)