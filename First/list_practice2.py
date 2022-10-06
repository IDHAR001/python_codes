# 在控制台中录入，所有学生姓名
# 如果姓名重复，则提示“姓名已存在”，不添加到列表中
# 如果录入空字符串，则倒序打印所有学生

namelist = list()
while True:
    name = input("输入学生姓名")
    if name == "":
        break
    elif name in namelist:
        print("姓名已存在")
        continue
    else:
        namelist.append(name)
for i in range(-1,-len(namelist)-1,-1):
    print(namelist[i])