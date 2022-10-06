list01 = []
while True:
    str01 = input("输入一个字符串")
    if str01 == "":
        break
    list01.append(str01)
print("".join(list01))