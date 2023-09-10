# __coding: UTF-8 __

import numpy as np

a = 7
b = 3

def add1(c, d):
    e = c + d
    print(e)

add1(a, b)

def add2(c, d):
    e = c + d
    return e

f = add2(a, b)
print(f)



x = np.array([[ 0,  1,  2,  3,  4],
       [ 5,  6,  7,  8,  9],
       [10, 11, 12, 13, 14]])


a = np.array([[ 0,  1,  2,  3,  4], [ 5,  6,  7,  8,  9], [10, 11, 12, 13, 14]])
