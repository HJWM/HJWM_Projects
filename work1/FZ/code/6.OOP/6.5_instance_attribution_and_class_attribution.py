# -*- coding: utf-8 -*-
"""
Created on Sat May  5 14:04:48 2018

@author: FZ
"""

class Student():
      name = 'student'  #belongs to class
      def __init__(self,name):
            self.name = name
            
s = Student('fz')  #via self
s.score = 100   #via instance variable

print (Student.name) #student






class Student(object):
      name = 'Student'
      
      
s = Student()
print (s.name)   #Student
s.name = 'fz'   #绑定变量，优先级高于类变量
print (s.name)   #fz
del s.name   #删除后 重现类变量
print (s.name)   #Student



# =============================================================================
#exercise 
# =============================================================================
#为了统计学生人数，可以给Student类增加一个类属性，每创建一个实例，该属性自动增加

class Student(object):
      count = 0
      def __init__(self,name):
            self.name = name
            Student.count += 1
            
            
for i in range(10):
      i = Student(i)
      
      
print (Student.count)