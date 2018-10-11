# -*- coding: utf-8 -*-
"""
Created on Thu Sep 27 17:14:24 2018

@author: zhe

E-mail：1194585271@qq.com
"""

#当我们需要定义常量时，一个办法是用大写变量通过整数来定义，例如月份;

#更好的方法是为这样的枚举类型定义一个class类型，然后，每个常量都是class的一个唯一实例。
#Python提供了Enum类来实现这个功能.
from enum import Enum

Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))

print (Month.Jan)

for name, member in Month.__members__.items():
    print(name, '=>', member, ',', member.value)
	
#	如果需要更精确地控制枚举类型，可以从Enum派生出自定义类：
from enum import Enum, unique

@unique
class Weekday(Enum):
    Sun = 0 # Sun的value被设定为0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6
	
#@unique装饰器可以帮助我们检查保证没有重复值。
#访问这些枚举类型可以有若干种方法
day1 = Weekday.Mon
day2 = Weekday['Tue']

#可见，既可以用成员名称引用枚举常量，又可以直接根据value的值获得枚举常量。



#小结
#Enum可以把一组相关常量定义在一个class中，且class不可变，而且成员可以直接比较