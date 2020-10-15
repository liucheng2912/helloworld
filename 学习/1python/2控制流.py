#   分支结构：某个判断条件后，选择一条分支去执行
#   顺序结构：一条一条语句顺序执行
# 多重分支
a=1
if a==0:
    print("a=0")
elif a==1:
    print("a=1")
elif a==2:
    print("a=2")
else:
    print("not")
# 嵌套分支
x=3
if x>1:
    sum=3*x-5
else:
    if x>-1:
        sum=x+2
    else:
        sum=5*x+3
print(sum)
# 扁平化更好
if x>1:
    sum=3*x-5
elif -1<x<=1:
    sum=x+2
elif x<-1:
    sum=5*x+3
print(sum)

# 循环
# for-in循环
sum=0
for i in range(101):
    sum+=i
print(sum)

sum=0
for i in range(101):
    if i %2 ==0:
        sum+=i
print(sum)

#range(1,100,2) 1到99的奇数  步长为2
sum=0
for i in range(0,101,2):
    sum+=i

print(sum)

# while循环
a=1
while a==1:
    print("a==1")
    a=a+1
else:
    print("a!=1")
    print(a)

# 写成一行
a=0
while a==0:a+=1
print(a)

# break、continue
for i in range(1,10):
    if i==5:
        break
    print(i)

for i in range(1,10):
    if i==5:
        continue
    print(i)

