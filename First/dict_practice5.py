list01 = []
while True:
    name = input("输入学生名称")
    if name == "":
        break
    age = input("输入年龄")
    score = input("输入成绩")
    sex = input("输入性别")
    list01.append({"name":name,"age":age,"score":score,"sex":sex})
for item in list01:
    print(item)
print(list01[len(list01)-1])