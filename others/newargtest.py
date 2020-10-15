#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import sys

il = len(sys.argv)
i = 1

while i < il:
  if len(sys.argv[i])>3:
     print(sys.argv[i])
  i = i+1


