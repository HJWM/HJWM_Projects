# -*- coding: utf-8 -*-
"""
Created on Fri Apr 13 14:53:00 2018

@author: FZ
"""
import time
# =============================================================================
# 装饰器 decorator
# =============================================================================
def now():
      print ('2018/4/13')

n = now
print (n())

print (now.__name__)
print (n.__name__)

#定义一个打印日志的decorator

def log(func):
      def wrapper(*args,**kw):
            print ('call %s():'%func.__name__)
            return func(*args,**kw)
      return wrapper

@log
def now1():
      print ('2018/4/13')
      
print (now1())

#若decorator 本身需要参数，则需编写一个返回decorator的函数。

def log(text):
      def decorator(func):
            def wrapper(*args,**kw):
                  print ('%s %s():'%(text,func.__name__))
                  return func(*args,**kw)
            return wrapper
      return decorator

@log('excute')
def now2():
      print ('2018/4/13')

print (now2())

print (now2.__name__)
#产生问题，需要把原始函数的__name__等属性复制到wrapper()函数中，
#否则，有些依赖函数签名的代码执行就会出错。

#解决此类问题 引入python内置的functools.wraps

import functools

def log(func):
      @functools.wraps(func)
      def wrapper(*args,**kw):
            print ('call %s():'%func.__name__)
            return func(*args,**kw)
      return wrapper

#带参数的log decorator
def log(text):
      def decorator(func):
            @functools.wraps(func)
            def wrapper(*args,**kw):
                  print ('%s %s():'%(text,func.__name__))
                  return func(*args,**kw)
            return wrapper
      return decorator

@log('excute')
def now():
      print ('2018/4/13')
      
print (now(),'frala')
      
# =============================================================================
# excise
# =============================================================================
#请设计一个decorator，它可作用于任何函数上，并打印该函数的执行时间：

def excute_time(func):
      @functools.wraps(func)
      def wrapper(*args,**kw):
            print ('%s executed in %s ms' % (func.__name__, 10.24))
            return func(*args,**kw)
      return wrapper

@excute_time
def fast(x,y):
      time.sleep(0.0012)
      return x+y

print (fast(1,2))


#请编写一个decorator，能在函数调用的前后打印出'begin call'和'end call'的日志。

def log(func):
      @functools.wraps(func)
      def wrapper(*args,**kw):
            start=time.time()
            func(*args,*kw)
            time.sleep(0.1)
            end=time.time()
            print('%s is executed %s ms'%(func.__name__,(end-start)))
            
      return wrapper

@log
def test1():
      print ('LIU is a good girl')
      
print(test1())



#再思考一下能否写出一个@log的decorator，使它既支持：
#@log
#def f():
#    pass

#又支持：
#@log('execute')
#def f():
#    pass


def log(text=None):
      def decorator(func):
            @functools.wraps(func)
            def wrapper(*args,**kw):
                  if callable(text):
                        print ('call %s():'%func.__name__)
                  else:
                        print ('%s %s():'%(text,func.__name__))
                  return func(*args,**kw)
            return wrapper
      return decorator(text) if callable(text) else decorator

@log('excute')
def test4(i,j):
      return i*j

@log
def test5(m,n):
      return m+n

print (test4(3,4))

print (test5(3,4))










