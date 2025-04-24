import numpy as np
arr = np.array([[1,2,3,4,5],[6,7,8,9,10]]) #2x5 matrix
arr1 = np.array([[1,2],[3,4],[5,6],[7,8],[9,10]]) #5x2 matrix
print(arr.ndim)
print(arr[0:2,0:3])
print("=====")
print(arr1[0:5,0:1])