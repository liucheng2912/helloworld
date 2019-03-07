#!/usr/bin/env python
#-*- coding:utf-8 -*-

class UserData(object):
   def __init__(self,id,name):
       self.id = id
       self.name = name

class NewUser(UserData):
   
   def __call__(self):
     print("{}'s id is {}".format(self.name,self.id))    



if __name__ == '__main__':
    user = NewUser(101,'Jack')
    user()

