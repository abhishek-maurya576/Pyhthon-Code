import numpy as np
arr = np.array([[5,5,4,7,8,2],[4,7,8,7,4,7]])
dim4 = arr.reshape(1,2,3,2)
print(dim4)
print(dim4.reshape(6,2))