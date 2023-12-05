#Do exercise 6.2, but taking into account only those numbers that are even.
#Check if there is any operator that can help you: https://docs.python.org/3/library/operator.html(Look under Mapping Operators to Functions)
import numpy as np
def even_num_arr(x,y,p):
    if x % y == 0:
        return np.sum(abs(x-y)**p)**(1/p)
    

