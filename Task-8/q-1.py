# -*- coding: utf-8 -*-
"""
Created on Wed Mar  8 15:25:04 2022

@author: shyam
"""
"""
Consider the vector [10, 11, 12, 13, 14], how to build a new vector with 5 
consecutive zeros interleaved between each value?
"""
import numpy as np
x =10
y =14
z = y + 1
nums = np.arange(x,z)
print("Original array: ",nums)
a = 5
new_nums = np.zeros(len(nums) + (len(nums)-1)*(a))
new_nums[::a+1] = nums
print("\nNew array:")
print(new_nums)