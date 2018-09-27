# -*- coding: utf-8 -*-
"""
Created on Thu Sep 27 16:24:40 2018

@author: zhe

E-mail：1194585271@qq.com
"""

#继承是面向对象编程的一个重要的方式，因为通过继承，子类就可以扩展父类的功能。

#类层次仍按照哺乳类和鸟类设计
class Animal(object):
    pass

# 大类:
class Mammal(Animal):
    pass

class Bird(Animal):
    pass


#我们要给动物再加上Runnable和Flyable的功能，只需要先定义好Runnable和Flyable的类
class RunnableMixin(object):
    def run(self):
        print('Running...')

class FlyableMixin(object):
    def fly(self):
        print('Flying...')
		
#对于需要Runnable功能的动物，就多继承一个Runnable，例如Dog
#对于需要Flyable功能的动物，就多继承一个Flyable，例如Bat
		
# 各种动物:
class Dog(Mammal,RunnableMixin):
    pass

class Bat(Mammal,FlyableMixin):
    pass

class Parrot(Bird,FlyableMixin):
    pass

class Ostrich(Bird,RunnableMixin):
    pass

#通过多重继承，一个子类就可以同时获得多个父类的所有功能。


		
#Mixin  混入   确定继承关系的主线
#在设计类的继承关系时，通常，主线都是单一继承下来的，例如，Ostrich继承自Bird。但是，如果需要“混入”额外的功能，通过多重继承就可以实现，比如，让Ostrich除了继承自Bird外，再同时继承Runnable。这种设计通常称之为MixIn。

#比如，编写一个多进程模式的TCP服务
#class MyTCPServer(TCPServer, ForkingMixIn):
#    pass
#
#class MyUDPServer(UDPServer, ThreadingMixIn):
#    pass
#
#class MyTCPServer(TCPServer, CoroutineMixIn):
#    pass

#这样一来，我们不需要复杂而庞大的继承链，只要选择组合不同的类的功能，就可以快速构造出所需的子类。


#小结
#由于Python允许使用多重继承，因此，MixIn就是一种常见的设计。
#
#只允许单一继承的语言（如Java）不能使用MixIn的设计。






