# -*- coding: utf-8 -*-
"""
Created on Sat May  5 12:A:35 2018

@author: FZ
"""



print (type(123)==int)  #ture
print (type('123')==type('abc'))   #true
print (type('123'))   #<class 'str'>


import types

def fn():
      pass

print (type(fn)==types.FunctionType)   #true
print (type(abs)==types.BuiltinFunctionType)   #true
print (type(lambda x:x)==types.LambdaType)  #true
print  (type(x for x in range(10))==types.GeneratorType)   #ture




class Animal:
      pass

class Dog(Animal):
      pass

class Cat(Animal):
      pass

a = Animal()
b = Dog()
c = Cat()

print (isinstance(a,Animal))   #ture
print (isinstance(b,Dog))   #ture
print (isinstance(b,Animal))   #true
print (isinstance(c,Dog))   #false


print (isinstance([1,2,3],(list,tuple)))   #true
print (isinstance((1,2,3),(list,tuple)))   #ture



print (dir('123'))  #['__add__', '__class__', '__contains__',...]



print ('zhe'.__len__())   #3
print (len('zhe'))   #3


class MyObject():
      def __init__(self):
            self.x = 16
      def power(self):
            return self.x*self.x
      
obj = MyObject()

print (hasattr(obj,'x'))  #true   实例有属性x
print (obj.x)   #16

print (hasattr(obj,'y'))   #false
setattr(obj,'y',32)
print (hasattr(obj,'y'))   #true
print (getattr(obj,'y'))   #32
print (obj.y)

#print (getattr(obj,'z'))   #抛出error

print (hasattr(obj,'power'))   #true
print (getattr(obj,'power'))   #bound method MyObject.power

fn = getattr(obj, 'power') # 获取属性'power'并赋值到变量fn
print (fn)  #fn = obj.power

print (fn())   #16*16







