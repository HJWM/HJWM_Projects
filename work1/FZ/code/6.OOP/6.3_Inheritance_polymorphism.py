# -*- coding: utf-8 -*-
"""
Created on Wed May  2 10:55:43 2018

@author: FZ
"""


# =============================================================================
# inhenritance
# =============================================================================
class Animal(object):
      def run(self):
            print ('Animal is running.')
            
class Dog(Animal):
      def run(self):
            print ('dog is running.')

class Cat(Animal):
      pass


hua = Dog()  #重写父类方法
zl = Cat()   #继承父类方法

hua.run()
zl.run()      
      
# =============================================================================
# polymophism      
# =============================================================================
a = list()
b = Animal()
c = Dog()

isinstance(a,list)    #true
isinstance(b,Animal)  #true
isinstance(c,Dog)     #true
isinstance(c, Animal) #true

def run_twice(Animal):
      Animal.run()
      Animal.run()

run_twice(b)  #Animal is running.
run_twice(c)  #dog is running.

class Tortoise(Animal):
      def run(self):
            print ('tortoise is running slowly.')
                      
run_twice(Tortoise())  #tortoise is running slowly.


class Timer(object):
      def run(self):
            print ('start...')

run_twice(Timer())

