'''
父类：动物（行为：叫）

子类：
    狗（行为：咬）
    鸟（行为：飞）
'''

'''
子类若没有构造函数，使用父类的
子类若具有构造函数，则必须先调用父类构造函数
'''

class Animal:
    def shout(self):
        print("叫！")

class Dog(Animal):
    def bite(self):
        print("咬")

class Bird(Animal):
    def fly(self):
        print("飞")

animal = Animal()
dog = Dog()
bird = Bird()

animal.shout()
dog.shout()
bird.shout()

print(isinstance(dog,Animal))
print(issubclass(Dog,Animal))
print(isinstance(animal,Dog))

class Person:
    def __init__(self,name):
        self.name = name

class Children(Person):
    def __init__(self, name):
        super().__init__(name)

c01 = Children("idhar")