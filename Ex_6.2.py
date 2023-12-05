#Write a function that receives two numpy arrays (vectors) and one integer (p) and returns the Minkowski distance between these.
#Hint: you can use abs(a) to get the absolute or a ndarray a.
import numpy as np
def minkowski_dist(x,y,p):
    return np.sum(abs(x-y)**p)**(1/p)
