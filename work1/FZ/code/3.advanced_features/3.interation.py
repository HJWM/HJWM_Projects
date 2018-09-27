# -*- coding: utf-8 -*-
"""
Created on Mon Jan 22 21:29:19 2018

@author: FZ
"""

#interation(迭代)
#如果给定一个list或tuple，我们可以通过for循环来遍历这个list或tuple，这种遍历我们称为
#迭代（Iteration）

#not only list,tuple but dict as well

d = {'fz':98,'zhanglu':100,'huasheng':99,'liuyouze':100}
print (d)

for key in d:
    print (key)   #dict default interate key

for value in d.values(): #interate value
    print (value)

#interation string
    
for a in 'frala':
    print (a)
    
#how to judge interation?
from collections import Iterable
print (isinstance('asdfghjkl',Iterable))    #interation
print (isinstance(123,Iterable))            #no interation


#enumerate 枚举
L = [9,8,7,6,5]        #list number
for i,value in enumerate(L):
    print (i,':',value)
    
L1 = [(1,2),(3,4),(5,6)]  
for x,y in L1:         #two variables at the same time 
    print (x,y)


#ecercise
def findMinAndMax(L):   
    if L == []:      #is and ==  different
        return (None,None)
    min =  99999999
    max = -99999999
    for i in L:
        if min > i:
            min = i
        if max < i:
            max = i
    return (min,max)   

if findMinAndMax([]) != (None, None):
    print('测试失败!')
elif findMinAndMax([7]) != (7, 7):
    print('测试失败!')
elif findMinAndMax([7, 1]) != (1, 7):
    print('测试失败!')
elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
    print('测试失败!')
else:
    print('测试成功!')
    
#is and ==
#is compare value
#== compare id point


x = y = [4,5,6]
z = [4,5,6]
print (x == y)     #true
print (x == z)     #true
print (x is y)     #ture
print (x is z)     #ture

#小结
#任何可迭代对象都可以作用于for循环，包括我们自定义的数据类型，
#只要符合迭代条件，就可以使用for循环。





    
    