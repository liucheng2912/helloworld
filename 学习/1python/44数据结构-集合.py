#   不重复元素组成的无序的集
#   基本用法包括成员检测和消除重复元素
#   使用{}或set()函数创建集合
#   要创建一个空集合只能用set() 不能用{}
a={1}
b=set()
c={}
print(type(a))
print(type(b))
print(type(c))

a1={1,2,3}
b1={1,4,5}
# 并集
print(a1.union(b1))
# 交集
print(a1.intersection(b1))
# 差集 a1有 b1没有
print(a1.difference(b1))
# add
a1.add("a")
print(a1)
# 去重

print([i for i in "bdfdwfewfwe"])
c="bdfdwfewfwe"
print(set(c))