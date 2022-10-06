import copy

list01 = [800,[1000,1200]]
# 浅拷贝
list02 = list01[:]

# 浅拷贝
list02 = list01.copy()
print(list02)

list02 = list01

print(list02)

# 深拷贝
list02 = copy.deepcopy(list01)

print(list02)

# 所有的编程语言默认的copy都是浅拷贝