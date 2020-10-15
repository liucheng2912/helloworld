"""
变量
    存储数据的载体
    计算机中的变量是实际存在的数据或者说是存储器中存储数据的一块内存空间，变量的值可以被读取和修改，这是所有计算和控制的基础
"""
a=1
print(a)
# 可以打印变量的存储地址
print(id(a))

# 数字
a=1
b=0.2
c=0.2j

print(type(a))
print(type(b))
print(type(c))

# 字符串
# \转义符
# r 忽略转义符的作用
# + 以及空格  多个字符串连接
# 切片

str_a="aaaaaa"
str_b="bbbbbb"
print(str_a)

print("bbbbb\n")
print("bbbbb\\n")
print(r"bbbbb\n")

print("bbbbb")

print(str_a+str_b)
print("aaaa" "bbbb")

str_c="1234567"
# [开始 ： 结束 ：步长]
print(str_c[0])
print(str_c[0:5:2])

# 列表
list1 = [1,2,3]
print(list1[0])
# 切片
print(list1[0:2:2])
# 复制
print(list1[:])

