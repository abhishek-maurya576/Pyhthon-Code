import numpy as np
arr = np.array([[5,5,4,7,8,2],[4,7,8,7,4,7]])
dim5 = arr.reshape(1,1,2,3,2)
print("5D dim: ",dim5)
print("One dim: ",dim5.reshape(-1))