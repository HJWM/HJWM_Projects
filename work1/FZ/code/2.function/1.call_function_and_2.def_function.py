# -*- coding: utf-8 -*-
"""
Created on Mon Jan 15 14:23:49 2018

@author: FZ
"""
import math
# =============================================================================
# # function 函数
print ('1.call cfunction:')
#函数是一种代码抽象方式 

#函数调用 abs()  max()等

#数据类型转换函数 

#函数名其实就是指向一个函数对象的引用，完全可以把函数名赋给一个变量，相当于给这个函数起了一个“别名”：

a = abs #函数别名
print (a(-123))

s =  ([1,2,3,4,5])

#exercise
n1 = 255
n2 = 1000
s1 = str(hex(n1))
print (s1,str(hex(n2)))


#小结
#调用Python的函数，需要根据函数定义，传入正确的参数。如果函数调用出错，一定要学会看错误信息，所以英文很重要！
# =============================================================================

# =============================================================================
# 定义函数
print ('2.define function:')
def my_abs (x):
    if not isinstance(x,(int,float)):
        raise TypeError('bad operand type')  #抛出错误
    if x>0:
        return x
    else:
        return -x

#空函数
def nop(x):
    pass      #没想好可以用pass 否则会报错
    if x==1:
        pass  #返回None
    
#参数检查
print (my_abs(12.468))    

#返回多值
def mov(x,y,step,angle=0):
    nx = x + step *math.cos(angle)
    ny = y - step *math.sin(angle)
    return nx,ny
t = mov(100,100,60,math.pi/6)  #返回值实际是tuple 即单返回值
print (t)

#小结
#定义函数时，需要确定函数名和参数个数；
#如果有必要，可以先对参数的数据类型做检查；
#函数体内部可以用return随时返回函数结果；
#函数执行完毕也没有return语句时，自动return None。
#函数可以同时返回多个值，但其实就是一个tuple。

#exercise
def quadratic (a,b,c):
    if b*b-4*a*c<0:
        return 'No answer'
    else:
        x1 = (-b+math.sqrt(b*b-4*a*c))/(2*a)
        x2 = (-b-math.sqrt(b*b-4*a*c))/(2*a)
        return x1,x2
print (quadratic(2,3,1))
print (quadratic(1,3,-4))
# =============================================================================
