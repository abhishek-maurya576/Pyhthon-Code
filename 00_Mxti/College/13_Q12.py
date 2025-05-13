'''
Problem 12: NumPy Indexing and Slicing
Task:
Create a 2D NumPy array, for example:
np_array = np.array([[10, 11, 12],
                     [13, 14, 15],
                     [16, 17, 18]])
Use code with caution.
Python
Access and print the element at row 1, column 2.
Access and print the element at the last row, last column using negative indexing.
Print the first row of the array using slicing.
Print the last column of the array using slicing.
Print the sub-array consisting of the first two rows and the last two columns using slicing.
Use boolean indexing to select and print all elements in the array that are greater than 14.
Use integer array indexing to select and print the elements at positions (0,0), (1,1), and (2,2).
'''
import numpy as np
np_array = np.array([[10, 11, 12],
                     [13, 14, 15],
                     [16, 17, 18]])
print(f"the element at row 1, column 2: {np_array[0,1]}")
print(f"the last row, last column using negative indexing {np_array[-1,-1]}")
print(f"the first row of the array using slicing {np_array[0:1]}")
print(f"the last column of the array using slicing: ")
print(f"the elements at positions (0,0): {np_array[0,0]}, (1,1): {np_array[1,1]}, and (2,2): {np_array[2,2]}")