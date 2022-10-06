class Teacher:
    def __init__(self,name,skill) -> None:
        self.name = name
        self.skill = skill

    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self,name):
        self.__name = name

    @property
    def skill(self):
        return self.__skill
    
    @skill.setter
    def skill(self,skill):
        self.__skill = skill

    # def teach(self):
    #     return self.__skill

class Student:
    def __init__(self,name,skill) -> None:
        self.name = name
        self.skill = skill

    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self,name):
        self.__name = name

    @property
    def skill(self):
        return self.__skill
    
    @skill.setter
    def skill(self,skill):
        self.__skill = skill

    def learn(self,teacher):
        self.__skill.append(teacher.skill)

zhangwuji = Teacher("张无忌","排山倒海")
xiaolongnv = Student("小龙女",["九阴白骨爪","乾坤大挪移"])
print(zhangwuji.skill)
xiaolongnv.learn(zhangwuji)
print(xiaolongnv.skill)