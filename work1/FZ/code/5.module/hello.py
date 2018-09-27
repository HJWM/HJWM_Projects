# -*- coding: utf-8 -*-

' a test module ' #文档注释 可通过 __doc__ 访问

__author__ = 'frala' #作者注释

import sys

def test():
      args = sys.argv
      if len(args)==1:
            print ('Hello world!')
      elif len(args)==2:
            print ('Hello,%s' % args[1])
      else:
            print ('Too many arguments!')
            
if __name__ == '__main__':
      test()