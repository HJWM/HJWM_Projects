# -*- coding: utf-8 -*-
"""
Created on Tue Jan 23 20:15:43 2018

@author: FZ
"""

#list comprehensions 列表生成式

L1 = list (range(1,11))
print (L1)

#generate [1x1, 2x2, 3x3, ..., 10x10]
L2 = list()
for i in range(1,11):
    L2.append(i*i)
print (L2)
#too complex
print ([x*x for x in range(1,11)]) #one line
#add if
print ([x*x for x in range(1,11) if x % 2 == 0]) #one line
#two variables
print ([m+n for m in 'ABC' for n in 'abc'])

#show pwd and all files
import os
print ([d for d in os.listdir('.') ])


#interation key and value in the dict at the same time
d = {'A':'a','B':'b','C':'c'}
for key,value in d.items():
    print (key,':',value)

print ([k+':'+v for k,v in d.items()])   

#for lower
L3 = ['Hello', 'World', 'IBM', 'Apple']
print ([s.lower() for s in L3])

#exercise
L4 = ['Hello', 'World', 18, 'Apple', None]
print ([s.lower() for s in L4 if isinstance(s,str)])







