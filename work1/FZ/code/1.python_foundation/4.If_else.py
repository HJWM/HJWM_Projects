# -*- coding: utf-8 -*-
"""
Created on Sun Jan 14 15:29:19 2018

@author: FZ
"""

#条件判断
#缩进规则     4个空格或1个Tab

tage = input('please input your age :')
age = int (tage)
print ('your age is %d' % age)
if age>=18:                          #比较时不能是str
    print ('adult')
elif age>=6:
    print ('teenager')
else:
    print ('kid')


#exercise
h = input ('please input your height :')
w = input ('please input your weight :')
hei = float (h)
wei = float (w)

BMI = wei/(hei*hei)
if BMI<=18.5:
    print ('过轻')
elif BMI<=25:
    print ('正常')
elif BMI<=28:
    print ('过重')
elif BMI<=32:
    print ('肥胖')
else:
    print ('严重肥胖')
    
#小结
#条件判断可以让计算机自己做选择，Python的if...elif...else很灵活。
#条件判断从上向下匹配，当满足条件时执行对应的块内语句，后续的elif和else都不再执行。