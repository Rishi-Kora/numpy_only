import numpy as np
m = np.array([1,2,3,4])
n=m
n[0]=10
print(n)


s = m.copy()
print(s is m)
