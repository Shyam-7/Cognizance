# -*- coding: utf-8 -*-
"""
Created on Wed Mar  8 15:52:31 2022

@author: shyam
"""

import pandas as pd
arr = pd.Series(['amrita', 'school', 'of', 'engineering', 'chennai' , 'campus'])
p = ""
q = arr.str.title()
i =0
while i < len(arr):    
    p = p + q[i]
    i = i + 1
    p = p + " "

print(p)