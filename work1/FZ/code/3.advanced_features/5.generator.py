# -*- coding: utf-8 -*-
"""
Created on Tue Jan 23 21:16:30 2018

@author: FZ
"""

#generator 生成器 一边循环一边计算的机制

#list comprehension
L1 = [x*x for x in range(10)]
print (L1)

#generator
L2 = (y*y for y in range(10))
print (next(L2))#complex

for x in L2:
    print (x) #easy

#function fib
print ('function>>>>>>>') 
def fib(max):      #have generator
    n,a,b=0,0,1
    while n < max: 
        a, b = b, a + b            #t = (b, a + b) # t是一个tuple
        yield a    #generator      #a = t[0]
        n = n + 1                  #b = t[1]       
    return 'done'

for i in fib(10):
    print (i)

g = fib(6)
while True:
    try:
        x = next(g)
        print('g:', x)
    except StopIteration as e:
        print('Generator return value:', e.value)#catch return 'done'
        break
    
def odd():
    print('step 1')
    yield 1
    print('step 2')
    yield 3
    print('step 3')
    yield 5

#exercise
#杨辉三角
def triangles():
    L = [1]
    while True:
        yield L
        L = [x+y for x,y in zip( [0]+L, L+[0] )]
        
        
#测试        
n = 0
results = []
for t in triangles():
    print(t)
    results.append(t)
    n = n + 1
    if n == 10:
        break
if results == [
    [1],
    [1, 1],
    [1, 2, 1],
    [1, 3, 3, 1],
    [1, 4, 6, 4, 1],
    [1, 5, 10, 10, 5, 1],
    [1, 6, 15, 20, 15, 6, 1],
    [1, 7, 21, 35, 35, 21, 7, 1],
    [1, 8, 28, 56, 70, 56, 28, 8, 1],
    [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]
]:
    print('测试通过!')
else:
    print('测试失败!')
    
    
    
#小结
#
#generator是非常强大的工具，在Python中，可以简单地把列表生成式改成generator，也可以通过函数实现复杂逻辑的generator。
#
#要理解generator的工作原理，它是在for循环的过程中不断计算出下一个元素，并在适当的条件结束for循环。对于函数改成的generator来说，遇到return语句或者执行到函数体最后一行语句，就是结束generator的指令，for循环随之结束。
#
#请注意区分普通函数和generator函数，普通函数调用直接返回结果
#
#generator函数的“调用”实际返回一个generator对象


