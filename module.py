# -*- coding: utf-8 -*-
import config
import random

"""def Randoms(x):
    total = []
    test = 0
    for i in range(x):
        test = random.random()
        total.append(test)
    return total"""


def Randoms_Uniform(x, Start, Finish):
    total = []
    test = 0
    for i in range(x):
        test = random.uniform(Start, Finish)
        total.append(test)
    return total

def Randoms_Gauss(Num,x,y):
    total = []
    test = 0
    for i in range(Num):
        test = random.gauss(x,y)
        if test<0:
            test=0
        elif test>config.DATA_OF_2017['Upper_Limit']:
            test=config.DATA_OF_2017['Upper_Limit']
        total.append(test)
    return total

def Randoms_Price(Num,x,y):
    total=[]
    test=0
    for i in range(Num):
        test=random.gauss(x,y)
        total.append(test)
    return total
             