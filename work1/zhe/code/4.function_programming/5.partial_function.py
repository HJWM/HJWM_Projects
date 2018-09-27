# -*- coding: utf-8 -*-
"""
Created on Sat Apr 14 09:47:24 2018

@author: FZ
"""

# =============================================================================
#partial_function 
# =============================================================================


print (int('123456',base=8))

#假设要经过大量基于2进制转换成10进制，为了省去调用时的麻烦利用偏函数。

def int2(x,base=2):
      return int(x,base)

print (int2('101'))     

#functools.partial就是帮助我们创建一个偏函数的，不需要我们自己定义int2()，
#可以直接使用下面的代码创建一个新的函数int2：
import functools
int2 = functools.partial(int ,base=2)
print (int2('10101010001010111001010'))

max10 = functools.partial(max,10)#传入*args = 10    #max(*args) 
print (max10(5,7,2))