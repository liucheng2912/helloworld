#定义
# 组织好的 可重复使用的 用来实现单一或相关联功能的代码段
# 函数能提高应用的模块性 和代码的重复利用率

# 不带表达式的return或者不写return函数 相当于返回None
def func1():
    print("这是一个函数")
    return
# 位置参数 a b c
def func2(a,b,c):
    return a

# 函数的调用
print(func2(1, 2, 3))
# 默认参数
#   定义函数的时候使用k=v的形式定义
#   调用函数的时候 如果没有传递参数 则使用默认参数,传递参数的话就会使用传递参数
def func3(a=1):
    print(a)

func3()
func3(2)

# 关键字参数
# 调用函数的时候 使用k=v的方式进行传参
# 在函数调用/定义中，关键字必须跟随在位置参数的后面
def func2(a,b,c):
    print(a)
    print(b)
    print(c)

func2(a=1,c=3,b=2)
# 位置参数必须在关键字参数前面
func2(10,c=3,b=2)

# 特殊参数
#   仅限关键字参数 在仅限关键字参数 形参前放置一个*
def func2(a,b,*,c):
    print(a)
    print(b)
    print(c)
# func2(1,2,3)
# func2(1,2,c=3)

# lambda表达式
#   创建一个小的匿名函数
#   主体是一个表达式 而不是一个代码块 仅能在lambda表达是中封装有限的逻辑进去
func11=lambda x:x*2

def func12(x):
    return x*2

print(func11(3))
print(func12(3))