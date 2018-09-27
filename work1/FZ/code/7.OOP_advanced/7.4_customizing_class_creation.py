# -*- coding: utf-8 -*-
"""
Created on Thu Sep 27 16:42:57 2018

@author: zhe

E-mail：1194585271@qq.com
"""

#Python的class中还有许多这样有特殊用途的函数，可以帮助我们定制类。

#__str__

class Student(object):
	def __init__(self, name):
		self.name = name
		
print (Student('zhe'))

class Student(object):
	def __init__(self, name):
			self.name = name
	def __str__(self):
			return 'Student object (name: %s)' % self.name
	__repr__ = __str__ #命令行直接输出无print 调用__repr__而不是__str__.
	
		
print (Student('kui'))

s = Student('sheng')
print (s)

#__iter__
#如果一个类想被用于for ... in循环，类似list或tuple那样，就必须实现一个__iter__()方法
#，该方法返回一个迭代对象，然后，Python的for循环就会不断调用该迭代对象的__next__()方法
#拿到循环的下一个值，直到遇到StopIteration错误时退出循环。

class Fib(object):
    def __init__(self):
        self.a, self.b = 0, 1 # 初始化两个计数器a，b

    def __iter__(self):
        return self # 实例本身就是迭代对象，故返回自己

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b # 计算下一个值
        if self.a > 100000: # 退出循环的条件
            raise StopIteration()
        return self.a # 返回下一个值

    def __getitem__(self, n):#像list一样取值 以及slice
        if isinstance(n, int): # n是索引
            a, b = 1, 1
            for x in range(n):
                a, b = b, a + b
            return a
        if isinstance(n, slice): # n是切片
            start = n.start
            stop = n.stop
            if start is None:
                start = 0
            a, b = 1, 1
            L = []
            for x in range(stop):
                if x >= start:
                    L.append(a)
                a, b = b, a + b
            return L
for n in Fib():
	print (n)
	

#__getitem__
#Fib实例虽然能作用于for循环，看起来和list有点像，但是，把它当成list来使用还是不行，
#比如，取第5个元素：
print (Fib()[100])

print (Fib()[0:10])

#但是没有对step参数以及负数做处理




#__getattr__
#只有在没有找到属性的情况下，才调用__getattr__，已有的属性，比如name，不会在__getattr__中查找。

#__call__
#一个对象实例可以有自己的属性和方法，当我们调用实例方法时，我们用instance.method()来调用。
class Student(object):
    def __init__(self, name):
        self.name = name

    def __call__(self):
        print('My name is %s.' % self.name)

s = Student('Michael')
print (s())


#小结
#Python的class允许定义许多定制方法，可以让我们非常方便地生成特定的类。
#
#本节介绍的是最常用的几个定制方法，还有很多可定制的方法，请参考Python的官方文档。




