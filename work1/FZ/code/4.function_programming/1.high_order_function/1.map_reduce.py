# -*- coding: utf-8 -*-
"""
Created on Tue Apr 10 15:35:25 2018

@author: FZ
"""

# =============================================================================
#map 
# =============================================================================


def square(x):
    return x*x

L1 = [1,2,3,4,5,6,7,8,9]

L1 = list(map(square,L1))

print (L1)

L2 = []
for x in range(1,10):
    L2.append(x*x)
    
print (L2)

L3 = list(map(str,range(1,10)))

print (L3)


# =============================================================================
#reduce 
# =============================================================================
from functools import reduce

def add(x,y):
    return x+y

N1 = reduce(add,range(10))
print (N1) 

print (sum(range(10)))

L4 = [1,3,5,7,9]

def f(x,y):
    return x*10+y

N2 = reduce(f,L4)  #1,3,5,7,9  变成13579
print (N2)     


#将str转换为int函数

def char2int(s):
    digits = {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}
    return digits[s]

s = '1597864312'
N3 = reduce(f,map(char2int,s))
print (N3)


#整理成一个str2int函数

def str2int(s):
    def char2int(s):
        digits = {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}
        return digits[s]
    def f(x,y):
        return x*10+y
    return reduce(f,map(char2int,s))

s = '35978641325434616'

print (str2int(s))


# =============================================================================
# exercise
# =============================================================================
#利用map()函数，把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字。
#输入：['adam', 'LISA', 'barT']，输出：['Adam', 'Lisa', 'Bart']：

L5 = ['adam', 'LISA', 'barT','Frala']

def specify(x):
    x = x[0].upper()+x[1:].lower()
    return x

print (list(map(specify,L5)))

#Python提供的sum()函数可以接受一个list并求和，请编写一个prod()函数，
#可以接受一个list并利用reduce()求积：

print (sum(range(10)))

def product(x,y):
    return x*y

print (reduce(product,[3,5,7,9]))
    
#利用map和reduce编写一个str2float函数，把字符串'123.456'转换成浮点数123.456：




def str2float(s):
    def char2floatnumber(s):
        digits = {'0': 0,'1': 1,'2': 2,'3': 3,'4': 4,'5': 5,
                  '6': 6,'7': 7,'8': 8,'9': 9,'.': -1}
        return digits[s]
    point = 0
    def to_float(f, n):
        nonlocal point
        if n == -1:
            point = 1
            return f
        if point == 0:
            return f * 10 + n
        else:
            point = point * 10
            return f + n / point
    return reduce(to_float,map(char2floatnumber,s), 0.00000000)

print(str2float('0'))
print(str2float('123.456'))
print(str2float('123.45600'))
print(str2float('0.1234'))
print(str2float('.1234'))
print(str2float('120.0034'))
    
    
    
    
