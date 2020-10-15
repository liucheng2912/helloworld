# 列表
list=[2]
# 在列表的末尾添加一个元素 相当于a[len(a):]=[x]
print("append")
list.append(1)
list.append(2)
list.append(4)
print(list)

# 在给定的位置插入一个元素，要插入元素的索引 a.insert(len(a),x)==a.append(x)
print("\ninsert")
list.insert(1,3)
list.insert(0,9)
print(list)

#移除列表中第一个值为x的元素 如果没有这个元素 抛出ValueError异常
print("\nremove")
list.remove(1)
print(list)

# 删除列表中给定位置的元素并返回它，如果没有给定位置，a.pop()将会删除并返回列表中的最后一个元素
print("\npop")
print(list.pop(0))
print(list)
print(list.pop())
print(list)

# 对列表中的元素进行排序（参数可用于自定义排序）
print("\nsort")
list.sort(key=None,reverse=False)
print(list)

# 反转列表中的元素
print("\nreverse")
print(list.reverse())
print(list)