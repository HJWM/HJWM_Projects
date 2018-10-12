# -*- coding: utf-8 -*-
"""
Created on Thu Sep 27 15:17:59 2018

@author: zhe

E-mail：1194585271@qq.com
"""

class Student(object):
	pass

#实例化
s = Student()
#实例绑定属性
s.name = 'zhe'
print (s.name)#zhe
#实例绑定方法
def set_age(self,age):
	self.age=age
	
from types import MethodType
s.set_age = MethodType(set_age,s)#给实例绑定一个方法
s.set_age(25)
print (s.age)#25

#但是，给一个实例绑定的方法，对另一个实例是不起作用的
s2 = Student()
#s2.set_age(25)
#AttributeError: 'Student' object has no attribute 'set_age'

#但是给类绑定方法后，所有实例均可调用
def set_score(self, score):
	self.score = score
	
Student.set_score = set_score
s.set_score(95)
s2.set_score(100)
print (s.score,s2.score)#95,100

#使用__slots__,来限制该class实例能添加的属性
class Student(object):
    __slots__ = ('name', 'age') # 用tuple定义允许绑定的属性名称

s3 = Student()
s3.name = 'kui'
s3.age = '22'

print (s3.name,s3.age)

#s3.number = '001'   #it is wrong.
#print (s3.number)

#还要注意一点，__slots__定义的属性仅对当前类实例起作用，对继承的子类是不起作用的；
#除非在子类中也定义__slots__，这样，子类实例允许定义的属性就是自身的__slots__加上父类的__slots__