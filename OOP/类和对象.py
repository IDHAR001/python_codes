class Person:
    def __init__(self,name,age) -> None:
        self.name = name
        self.age = age
    def walk(self):
        print("walking")

p1 = Person("idhar",18)
p1.walk()