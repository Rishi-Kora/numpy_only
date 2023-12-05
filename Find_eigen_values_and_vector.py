import numpy as np
from numpy.linalg import eig
a = np.array([[0, 4], 
              [4, 3]])
n,k = eig(a)
print("E-value: ", n)
print("E-vector: ", k)
