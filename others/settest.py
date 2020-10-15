#!/usr/bin/env python3
#-*- coding:utf-8 -*-
import sys
s=set()
i = int(len(sys.argv))
n = 1
while n<i:
  s.add(sys.argv[n])
  n = n+1

print(s)


