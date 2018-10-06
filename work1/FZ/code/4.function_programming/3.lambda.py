# -*- coding: utf-8 -*-
"""
Created on Fri Apr 13 14:21:35 2018

@author: FZ
"""

# =============================================================================
#lambda 
# =============================================================================

print (list(map(lambda x:x*x,range(1,10))))

square = lambda x:x*x
print (square)
print (square(6))

def f(i):
      return lambda x:x*i
func = f(3)
print (func)
print (func(9))

def fx(x,y):
      return lambda :x*x+y*y

print (fx(3,4))
print (fx(3,4)())

# =============================================================================
#excise 
# =============================================================================
print (list (filter(lambda x:x%2==1,range(1,20))))