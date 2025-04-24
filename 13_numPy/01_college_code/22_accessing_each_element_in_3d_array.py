import numpy as np
arr = np.array([[5,5,4,7,8,2],[4,7,8,7,4,7]])
dim3 = arr.reshape(2,2,3)

for x in dim3:
    for y in x:
        for z in y:
            print(z)
        print()