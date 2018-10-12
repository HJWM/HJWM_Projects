# -*- coding: utf-8 -*-
"""
Created on Sat Apr 28 11:22:28 2018

@author: FZ
"""

def fact(n):
      if n == 1:
            return 1
      else:
            return n*fact(n-1)
      
def fact_iter(number,product):
      if number == 1:
            return product
      else:
            return fact_iter(number-1,number * product)
      
      