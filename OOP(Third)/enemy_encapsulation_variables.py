class Enemy:
    def __init__(self,name,atk,blood) -> None:
        self.__name = name
        self.atk = atk
        self.blood = blood

    def get_atk(self):
        return self.__atk
    
    def set_atk(self,atk):
        if 10 <= atk <= 50:
            self.__atk = atk
        else:
            raise ValueError("不对！")

    atk = property(get_atk,set_atk)

    def get_blood(self):
        return self.__blood
    
    def set_blood(self,blood):
        if 100 <= blood <= 200:
            self.__blood = blood
        else:
            raise ValueError("不对！")

    blood = property(get_blood,set_blood)

spider = Enemy("spider",10,200)
print(spider.__dict__)
# spider.atk = 40
# print(spider.atk)
# spider.blood = 150
# print(spider.blood)