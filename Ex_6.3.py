#Write a function that receives two 2d numpy arrays. Your function should (element-wise) multiply the two arrays and then return the last row of the result, normalised.
import numpy as np
def create_arr_2(m1,m2):
    return np.array((m1*m2)[-1,::]/sum(m1*m2)[-1,::])
