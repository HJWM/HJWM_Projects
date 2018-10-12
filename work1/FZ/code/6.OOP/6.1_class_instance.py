# -*- coding: utf-8 -*-
"""
Created on Sat Apr 28 09:37:31 2018

@author: FZ
"""

# =============================================================================
#OOP object oriented programming 
# =============================================================================

class Student(object):  #自定义类
      pass

frala = Student() #创建实例

#可以自由的给实例绑定一些属性
frala.name = 'FZ'

#创建类时可以绑定属性
#定义方法 与普通函数没有什么区别 
#仍然可用可变参数，默认参数，关键字参数，命名关键字参数
class Student(object):
      def __init__(self,name,score):  #与普通函数相比 
            self.name = name          #第一个参数永远是实例变量 且调用时不用传入 
            self.score = score        #解释器自动传入
            
      def print_score(self):
            print ('%s : %d' % (self.name,self.score))
            
      def get_grade(self):
            if self.score > 90:
                  return 'A'
            elif self.score > 80:
                  return 'B'
            elif self.score > 60:
                  return 'C'
            elif self.score < 60:
                  return 'D'
            
frala = Student('FZ',97)

frala.print_score()
frala.get_grade()  #返回值 为 ‘A’



