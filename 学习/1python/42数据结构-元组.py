#   使用()定义
#   tuple list range 都是序列数据类型
#   元祖是不可变的，可以通过解包、索引来访问
tuple1=(1,2,3)
tuple2=1,2,3
print(tuple1)
print(type(tuple1))
print(tuple2)
print(type(tuple2))
# 直接修改会报错
# tuple1[0]="a"

# 可在元组中放置一个列表 可变元素 然后可修改元组中的列表
a=[1,2,3]
tuple4=(1,2,a)
tuple4[2].append(4)
tuple4[2][0]="a"
print(tuple4)

# count函数
b=(1,2,3)
print(b.count(1))

# index 对应元素的索引
print(b.index(2))