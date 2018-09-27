# -*- coding: utf-8 -*-
"""
Created on Wed Apr 11 09:53:02 2018

@author: FZ
"""

# =============================================================================
#return function 
# =============================================================================
#实现可变参数求和
def calc_sum(*args):
      ax = 0
      for x in args:
            ax = ax + x
      return ax

#如果不需要立刻求和，而是在后面的代码中，根据需要再计算怎么办？
#可以不返回求和的结果，而是返回求和的函数     
def lazy_sum(*args):
      def sum():
            ax = 0
            for x in args:
                  ax = ax + x
            return ax
      return sum

#当调用 lazy_sum() 时返回求和函数而非和值
f = lazy_sum(0,1,2,3,4,5,6,7,8,9)
print (f)

sum = f()
print (sum)

#两次调用 互不影响
f1 = lazy_sum(1,3,5,7,9)
f2 = lazy_sum(1,3,5,7,9)

print (f1 == f2) 


#返回的函数并没有立刻执行，而是直到调用了f()才执行,即惰性执行
def count():
      L = []
      for i in range(1,4):
            def f():
                  return i*i
            L.append(f)
      return L


[f1,f2,f3] = count()

print (f1)
print (f1())

#引用循环变量，则需引入绑定函数

def count():
      def f(j):#绑定函数
            def g():
                  return j*j
            return g
      L = []
      for i in range(1,4):
            L.append(f(i))  #f(i)被立即执行
      return L

f1, f2, f3 = count()
print (f1(),f2(),f3())

# =============================================================================
# excise
# =============================================================================
#利用闭包返回一个计数器函数，每次调用它返回递增整数：
def create_counter():
      k = [0]
      def  counter():
            k[0]=k[0]+1
            return k[0]
      return counter

counter = create_counter()
print (counter(),counter(),counter())

#注：
#1.内部函数一般无法修改外部函数的参数
#2.想要修改需要声明 nonlocal
#3.内部函数可以修改外部list中的元素

#因为counter= create_counter()这一句，
#counter指向了counter()函数，
#因此调用counter时，即是执行counter()，
#而不会对s进行再次赋值。


