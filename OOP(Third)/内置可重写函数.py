from re import S
from unicodedata import name


class Student:
    def __init__(self,name="",age=0) -> None:
        self.name = name
        self.age = age 
    
    # 对象 -> 字符串（随意格式）
    def __str__(self) -> str:
        return "名字“叫”%s,年龄是%d"%(self.name,self.age)
    
    # 对象 -> 字符串（解释器可识别，有格式，有语法）
    def __repr__(self) -> str:
        return "Student('%s',%d)"%(self.name,self.age)

s01 = Student("idhar",10)
str01 = repr(s01)
print(str01)
# 说明每个类都内置了一个str repr ...函数，之前print的时候都调用了str函数

# repr返回python格式字符串
# eval根据字符串执行代码
s02 = eval(repr(s01))
# 克隆了一个对象
print(s02.name)
print(type(s02))
