# -*- coding: utf-8 -*-
"""
Created on Wed Mar  8 16:15:59 2022

@author: shyam
"""
'''
sum of two arrays
'''
import numpy as np

p = np.array([9,8,7])
q = np.array([6,5,4])

print ("array n.o 1 : ", p)
print ("array n.o 2 : ", q)

a = np.add(p,q)
print ("sum of arrays 1 & 2 is : ", a)

'''
dot product of matrix
'''
r = np.array([[7,8,9],[4,5,6],[1,2,3]])
s = np.array([[1,2,3],[6,5,4],[7,8,9]])

print ("matrix n.o 1 : ", r)
print ("matrix n.o 2 : ", s)

b=np.dot(r,s)
print('')
print ("product of matrix 1 & 2 is : ", b)

