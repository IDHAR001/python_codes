dict01 = {}
# list01 = []
while True:
    name = input("输入学生名称")
    if name == "":
        break
    age = input("输入年龄")
    score = input("输入成绩")
    sex = input("输入性别")
    # list01.append(age)
    # list01.append(score)
    # list01.append(sex)
    dict01[name] = [age,score,sex]
# print(list01)
for k,v in dict01.items():
    print("%s的属性是%s"%(k,v))