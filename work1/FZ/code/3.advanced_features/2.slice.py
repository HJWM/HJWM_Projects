# -*- coding: utf-8 -*-
"""
Created on Mon Jan 22 09:32:49 2018

@author: FZ
"""

#slice 切片操作符

L = ['Michael','Sarah','Tracy','Bob','Jack']
print (L[0:3])   #catch 0,1,2
print (L[-3:-1] )#catch -3，-2


L1 = list(range(100))
print (L1[:10])  #catch  0,1......9
print (L1[10:20])
print (L1[:10:2])
print (L1[::5])
print (L1[:])

T = tuple(range(50))
print (T[::5])   #tuple slice still is tuple


print ('ABCDEFG'[:3])  #string slice still is string

#exercise
def trim(str):
    if str[0] is ' ':
        str = str[1:]
    if str[-1] is ' ':
        str = str[:-1]
    return str

print (trim(' hello'))
print (trim('hello '))
print (trim(' hello '))

#Summary
#we have slice,and somewhere do not need loop enough.
#and python's slice is every flexible and a row code can realize what the loop 
#realize