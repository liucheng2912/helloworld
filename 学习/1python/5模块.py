"""
程序结构：
    组成
        package 包
        module  模块
        function  方法
模块
    定义
        包含python定义和语句的文件
        .py文件
        作为脚本运行
    分类
        系统内置模块  自带模块
        第三方的开源模块    pip install
        自定义模块
"""
# 内置模块
import sys
import os
import re
import json
import time
print(sys.path)
time.sleep(1) #强制等待1s

#第三方开源模块
import  pytest

# 自定义库
# from 学习.python1.模块zdy import func1
# from 学习.python1.模块zdy import a
from 学习.python1.模块zdy import *
func1()
print(a)

import 学习.python1.模块zdy
学习.python1.模块zdy.func1()
print(学习.python1.模块zdy.a)

# dir() 找出当前模块定义的对象
# dir(sys) 找出参数模块定义的对象

name="lc"
def func2():
    return
print(dir())

print(dir(sys))

print(sys.path)
