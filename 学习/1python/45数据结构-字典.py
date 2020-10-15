#   以关键字为索引
#   关键字可以是任意不可变类型，通常是字符串 或数字
#       如果一个元组只包含字符串、数字、或元祖，那么这个元组也可以用作关键字
a={"a":1,"b":2}
b=dict(a=1,b=2)
print(a)
print(type(a))
print(b)
print(type(b))

# key值不可变
print(a.keys())
print(a.values())

# pop 删除对应键值对 并返回对应value
print(a.pop("a"))
print(a)

# popitem 随机删除键值对 并返回被删除的键值对
print(b.popitem())
print(b)

# fromkeys 将列表里的参数当做key值 建立新的列表
a1={}
b=a1.fromkeys([1,2,3])
# 对每一个key值赋值value为a
c=a1.fromkeys((1,2,3),"a")
print(b)
print(c)

# 字典推导式
print({i: i * 2 for i in range(1, 10)})






