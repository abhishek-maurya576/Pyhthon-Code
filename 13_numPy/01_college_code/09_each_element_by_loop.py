import numpy as n
arr = n.array([[[1,5,4],[7,8,9]],[[4,8,5],[5,8,7]]])
for i in arr:
    for j in i:
        for k in j:
            print(k)
        print("")
    