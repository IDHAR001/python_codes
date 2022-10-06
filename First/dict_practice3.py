dict00 = {}
while True:
    name = input("输入学生名称")
    if name == "":
        break
    age = input("输入年龄")
    score = input("输入成绩")
    sex = input("输入性别")
    dict00[name] = {"age":age,"score":score,"sex":sex}
# print(list01)
for k,v in dict00.items():
    print("%s的属性是%s"%(k,v))