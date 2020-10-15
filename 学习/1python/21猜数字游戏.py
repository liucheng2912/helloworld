import random
# 1-100的数字
x=random.randint(1,100)

while True:
    y = int(input("请输入数字"))
    if y<x:
        print("大一点")
    elif y>x:
        print("小一点")
    elif y==x:
        print("猜对了")
        break