class Student:
    def __init__(self,name,age,score,sex) -> None:
        self.name = name
        self.age = age
        self.score = score
        self.sex = sex

    def print(self):
        print(self.name,self.age,self.score,self.sex)

student_info = []
list01 = [
    Student("zhaoming",28,100,"女"),
    Student("zhangwuji",80,100,"男"),
    Student("idhar",100,100,"男"),
    Student("zhaoming1",38,100,"女"),
    Student("zhaoming2",48,100,"女"),
    Student("zhaoming3",58,100,"女"),

]

def search(list):
    for stu in list:
        if stu.name == "idhar":
            print(list.index(stu))
            return stu

stu1 = search(list01)
print(stu1.name,stu1.age)

def find_girl(list):
    list02 = []
    for stu in list:
        if stu.sex == "女":
            list02.append(stu)
    return list02
re = find_girl(list01)

for item in re:
    item.print()

def count_age(list):
    i = 0
    for item in list:
        if item.age >= 30:
            i += 1
    return i

number = count_age(list01)
print(number)

def turn_zero(list):
    for item in list:
        item.score = 0
    # return list

# listZero = turn_zero(list01)
turn_zero(list01)
for item in list01:
    item.print()

def get_name(list):
    nameList = []
    for item in list:
        nameList.append(item.name)
    return nameList

nameList = get_name(list01)
print(nameList)

def search_maxage(list):
    for i in range(len(list)-1):
        if list[i].age < list[i+1].age:
            list[i] = list[i+1]
    return list[i]

maxStu = search_maxage(list01)
print(maxStu.name)
