#!/usr/bin/env python
#-*- coding:utf-8 -*_

class UserData:

 def __init__(self,ID,name):    
    self.ID = ID
    self.name = name

 def __repr__(self):
   return 'ID:{} Name:{}'.format(self.ID,self.name)
   
class NewUser(UserData):
    group = 'shiyanlou-louplus'
    def get_name(self):
        return self.name
    def set_name(self,value):
        self.name = value
    @classmethod
    def get_group(cls):
        return cls.group

    @staticmethod
    def format_userdata(id,name):
        return "{}'s id is{}".format(name,id)
    

if __name__=='__main__':
    #user1 = NewUser(101,'Jack')
    #user1.set_name('Jackie')
    #user2 = UserData(102,'Louplus')
    #print(user1)
    #print(user2)
    print(NewUser.get_group())
    print(NewUser.format_userdata(109,'Lucy'))

