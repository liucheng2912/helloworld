#!/usr/bin/env python
#-*- coding:utf-8 -*-
import sys

i = int(len(sys.argv))

dict1 = {}
for i in sys.argv[1:]:
     a,b= i.split(':')
     dict1[a] = b

for key,value in dict1.items():
   print('ID:{} Name:{}'.format(key,value))

