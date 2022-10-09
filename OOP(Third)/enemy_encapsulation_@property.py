class Enemy:
    def __init__(self,name,atk,blood) -> None:
        self.__name = name
        self.atk = atk
        self.blood = blood

    @property
    def atk(self):
        return self.__atk
    
    @atk.setter
    def atk(self,atk):
        if 10 <= atk <= 50:
            self.__atk = atk
        else:
            raise ValueError("不对！")

    @property
    def blood(self):
        return self.__blood
    
    @blood.setter
    def blood(self,blood):
        if 100 <= blood <= 200:
            self.__blood = blood
        else:
            raise ValueError("不对！")

spider = Enemy("spider",10,200)
print(spider.__dict__)
spider.atk = 40
print(spider.atk)
spider.blood = 150
print(spider.blood)