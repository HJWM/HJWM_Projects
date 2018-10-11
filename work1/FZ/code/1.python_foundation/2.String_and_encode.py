# -*- coding: utf-8 -*-
"""
Created on Sat Jan 13 15:25:06 2018

@author: FZ
"""

#string and unicode
#ASCII Unicode 可变长 UTF-8

print ('包含中的string')
print (ord('中'))
print (chr(20013))

#转码
print ('ABC'.encode('ascii'))
print ('中文'.encode('UTF-8'))

#字节流编码
print (b'\xe4\xb8\xad\xe6\x96\x87'.decode('UTF-8'))
print (len('youareabetterman'))

#通配符 excerse
s1 = 72
s2 = 85
rate = (85-72)/72*100

print ('%.1f%%'% rate)


#小结：python使用的是 unicode编码，直接支持多语言
#string 与 byte转换时需要指定编码最常用的是 UTF-8