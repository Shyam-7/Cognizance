# -*- coding: utf-8 -*-
"""
Created on Wed Mar  8 15:36:43 2022

@author: shyam
Consider two random array A anb B, check if they are equal
"""

import array as arr

a = arr.array('i', [])

k = int(input("Enter size of array:"))
for i in range(0, k):
    num = int(input("Enter %d array element:" % (i + 1)))
    a.append(num)
b=arr.array('i', [])
l = int(input("Enter size of array:"))
for i in range(0, l):
    num = int(input("Enter %d array element:" % (i + 1)))
    b.append(num)
print()

if a==b:
    print("a is equal to b")
else:
    print("a is not equal to b")
    
        