# -*- coding: utf-8 -*-
"""
Created on Sun Apr 29 13:33:39 2018

@author: FZ
"""

class Student(object):
      
      def __init__(self,name,score):
            self.__name = name   #私有变量
            self.__score = score
      def print_score(self):
            print ('%s : %d' % (self.__name,self.__score))
            
            
frala = Student('FZ',99)   #解释器si私有变量改名  
frala.__name = 'Zl'      #frala.__name  =>  frala._Student__name

print (frala.__name)
print (frala._Student__name)


# =============================================================================
#exercise 
# =============================================================================
#练习
#请把下面的Student对象的gender字段对外隐藏起来，用get_gender()和set_gender()代替，并检查参数有效性：

class Student(object):
      def __init__(self, name, gender):
            self.name = name
            self.__gender = gender
            
      def get_gender(self):
            return self.__gender
      
      def set_gender(self,gender):
            self.__gender = gender
            
fra = Student('FZ','man')

print (fra.get_gender())

fra.set_gender('woman')

print (fra.get_gender())


