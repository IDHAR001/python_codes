class Student:
    def __init__(self,name,age,score,sex) -> None:
        self.name = name
        self.age = age
        self.score = score
        self.sex = sex

    def print(self):
        print(self.name,self.age,self.score,self.sex)

student_info = []
# dict_info = {}
while True:
    name = input("输入学生姓名:")
    if name == "":
        break
    age = input("请输入学生年龄:")
    score = input("请输入学生成绩:")
    sex = input("请输入学生性别:")
    stu = Student(name,age,score,sex)
    # dict_info = {"name":name,"age":age,"score":score,"sex":sex}
    student_info.append(stu)

print(student_info)
print(type(student_info[0]))
for stu in student_info:
    stu.print()
# for dict_info in student_info:
#     student1 = Student(**dict_info)
#     student1.print()
