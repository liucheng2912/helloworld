#!/usr/bin/env python3
#-*- coding:utf-8 -*-

start =1
end =100
result = 0

def compute():   
    global start,result
    while start<=end:
        result+=start
        start+=1
    print(result)

if __name__ == '__main__':

    compute()
