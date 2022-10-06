from re import I


dict02 = {"zzc":"100"}
print(dict02["zzc"])


dict01 = dict([("a","b"),("c","d")])
print(dict01)

# 修改元素（之前存在key）
dict01["a"] = "B"
# 添加元素
dict01["e"] = "E"

# 删除元素
del dict01["a"]
print(dict01)

# 遍历
for item in dict01:
    print(item)
    print(dict01[item])

for value in dict01.values():
    print(value)

for k,v in dict01.items():
    print(k)
    print(v)