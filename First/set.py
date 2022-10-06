from typing import Set


set01 = set("abc")
print(set01)

# 大多数情况用列表存储，然后用set去重
list01 = list(set01)
print(list01)
str01 = "".join(list01)
print(str01)

set02 = {"a","b","a"}
print(set02)

set02.add("ax")
print(set02)

for item in set02:
    print(item)

# 数学运算
# 交集
set11 = {1,2,3}
set12 = {2,3,4}
print(set11 & set12)

# 并集
print(set11 | set12)
# 补集
print(set11 ^ set12)
print(set11 - set12) # set11的补集
# 子集
set13 = {1,2}
print(set13 < set11)
# 超集
print(set11 > set13)

# 固定集合
set21 = frozenset([1,2,2,2,2,2])
print(set21)
print(type(set21))