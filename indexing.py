import numpy as np
m = np.arange(30).reshape(3,10)
print(m)
print(m[0,:])
print(m[0,:4])
print(m[1,:4])
print(m[1,:5])
print(m[1,::2])
print(m[1,::3])
print(m[1,:6:2])
print(m[1,[0,2,5]])
print(m[-1,-1])
print(m[-1,-2])
