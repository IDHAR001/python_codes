list01 = list(["a","b"])
print(list01)
tuple01 = tuple(list01)
print(tuple01)
print(type(tuple01))

a = list01[0]
print(type(a))

q,w = list01
print(q,w)
# 切片得到的还是原来的类型