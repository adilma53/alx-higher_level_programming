#!/usr/bin/python3

def weight_average(my_list=[]):
    if len(my_list) == 0:
        return 0
    
    s = 0
    t = 0
    
    for i, j in my_list:
        s += i * j
        t += j
    
    return s / t
