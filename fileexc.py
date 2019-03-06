#!/usr/bin/env python3
#-*- coding:utf-8 -*-

filename = '/etc/123'
f = open(filename)

try:
   f.write('123')
except:
   print("File with error")
finally:
   print("finally")
   f.close()

