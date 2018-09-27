# -*- coding: utf-8 -*-
"""
Created on Thu Sep 27 15:50:15 2018

@author: zhe

E-mail：1194585271@qq.com
"""

#在绑定属性时，如果我们直接把属性暴露出去，虽然写起来很简单，但是，没办法检查参数；

#检查参数合理性(复杂)
class Student(object):

    def get_score(self):
         return self._score

    def set_score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value
		
s = Student()
s.set_score(60)  #ok!

print (s.get_score())

#s.set_score(9999)
#print (s.get_score())  #wrong


#利用内置的装饰器@property 检查参数
#Python内置的@property装饰器就是负责把一个方法变成属性调用的

class Student(object):

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value
		
s = Student()
s.score = 60
print (s.score)
#s.score = 110
#print (s.score) #wrong

#我们在对实例属性操作的时候，就知道该属性很可能不是直接暴露的，而是通过getter和setter方法来实现的.


# =============================================================================
#exercise 
# =============================================================================
#请利用@property给一个Screen对象加上width和height属性，以及一个只读属性resolution：
class Screen(object):
	@property
	def width(self):
		return self._width
	
	@width.setter
	def width(self,value):
		self._width = value
		
	@property
	def height(self):
		return self._height
	
	@height.setter
	def height(self,value):
		self._height = value
		
	@property
	def resolution(self):
		return self.height * self.width

# 测试:
s = Screen()
s.width = 1024
s.height = 768
print('resolution =', s.resolution)
if s.resolution == 786432:
    print('测试通过!')
else:
    print('测试失败!')










