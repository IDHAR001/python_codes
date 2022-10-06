list01 = list(["123","xzc"])
print(list01)

list01.append("asd")

list02 = ["qweqwe","q","qweqweqw","eqweq"]
print(list02)
list02.append(1231231)
print(list02)

list02[0:] = []
print(list02)

list02[0:] = ["woaini","zhendeaini"]
# 不推荐
# for item in list02[::-1]:
#     print(item)

for index in range(1,-1,-1):
    print(list02[index])
# i -> index
for i in range(1,-1,-1):
    print(list02[i])

# 倒序获取所有元素
for i in range(len(list02)-1,-1,-1):
    print(list02[i])

for i in range(-1,-len(list02),-1):
    print(list02[i])