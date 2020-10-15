#   提供了一个更简单的创建列表的方法
#       常见用法是把某种操作应用于序列或可迭代对象的每个元素上，然后使用其结果来创建列表，或者通过满足某些特定条件元素来创建子序列
list=[]
for  i in range(1,4):
    list.append(i**2)

print(list)

list1=[i**2 for i in range(1,4)]
print(list1)

list2=[]
for i in range(1,4):
    if i!=1:
        list2.append(i**2)
print(list2)

list3=[i**2 for i in range(1,4) if i!=1]
print(list3)

list4=[]
for i in range(1,4):
    for j in range(1,4):
        list4.append(i*j)
print(list4)

list5=[i*j for i in range(1,4) for j in range(1,4)]
print(list5)
