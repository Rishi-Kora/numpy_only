import numpy as np
m1 = np.array([3,5,7,9,11,13])
m2 = np.array([1,2,1,1,2,3])
print(m2==1)
print(m1[m2==1])


m3 = np.array([[1,2],[3,4],[5,6]])
m4 = np.array(["True","False","True"])
print(m3[m4,:])
