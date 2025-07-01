#1.	Write a NumPy program to append values to the end of an array
import numpy as np
arr = np.array([4,5,6,7,8])
print(f"Original Arrya: {arr}")
arr1 = np.append(arr,5)
print(f"Single element append {arr1}")
arr2 = np.append(arr,[9,9,9,9,7])
print(f"multiple element append {arr2}")
print(f"Org array {arr}")
