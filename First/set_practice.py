list01 = []
while True:
    str01 = input("输入字符串：")
    if str01 == "":
        break
    list01.append(str01)
set01 = set(list01)
print(set01)