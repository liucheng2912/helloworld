#!/usr/bin/env python
#-*- coding:utf-8 -*-

import sys

output_dict = {}

def handle_data(a):
   b,c =  a.split(":")
   output_dict[b] = c
   

def print_data(a,b):
   print('ID:{}Name:{}'.format(a,b))
    
if __name__ == '__main__':
   
  for arg in sys.argv[1:]:
      handle_data(arg)
  
  for key in output_dict:
      print_data(key,output_dict[key])


 
