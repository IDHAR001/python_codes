# 列表容器可变，但是字符串容器不可变，把字符串放进列表里就可变了
list01 = ["idhar"]
list02 = list("abc")
print(list01)
print(list02)

print(list01[0])
print(list02[:3:1])

list02.append("123")
print(list02)
list02.insert(1,"baba")
print(list02)

list02.remove("a")
print(list02)

del list02[0]
print(list02)

del list02[0:]
print(list02)