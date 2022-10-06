class Person:
    def __init__(self,name) -> None:
        self.name = name

    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self,value):
        self.__name = value

    def get_money(self,str_position,type):
        type.return_money(str_position)

class Bank:
    def return_money(self,str_position):
        print("吐钱给"+str_position)

xiaoming = Person("xiaoming")
zhaohang = Bank()
xiaoming.get_money(xiaoming.name,zhaohang)