import numpy as np
def mult_arr(m1,m2):
    return np.array((m1*m2)[-1,:])//np.sum((m1*m2)[-1,:])



#print(mult_arr([1,2,3],[4,5,6]))
 
