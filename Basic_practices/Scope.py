# __coding: UTF-8 __
import numpy as np
import pandas as pd
from pandas import DataFrame, Series

a = 1
def func1():
    print(a)

func1()

def func2():
    b = 2
    print(b)

func2()

# print(b)

dframe = DataFrame({'k1':['X','X','Y','Y','Z'],
                    'k2':['alpha','beta','alpha','beta','alpha'],
                    'dataset1':np.random.randn(5),
                    'dataset2':np.random.randn(5)})
print(dframe)
