class Enemy:
    def __init__(self,name,atk,blood) -> None:
        self.__name = name
        self.set_atk(atk)
        self.set_blood(blood)

    def get_name(self):
        return self.__name

    def get_atk(self):
        return self.__atk
    
    def set_atk(self,atk):
        if 10 <= atk <= 50:
            self.__atk = atk
        else:
            raise ValueError("不对！")
        
    def get_blood(self):
        return self.__blood
    
    def set_blood(self,blood):
        if 100 <= blood <= 200:
            self.__blood = blood
        else:
            raise ValueError("不对！")

spider = Enemy("spider",10,200)
spider.set_blood(150)
spiderAtk = spider.get_atk()
print(spiderAtk)
spiderName = spider.get_name()
print(spiderName)
spiderBlood = spider.get_blood()
print(spiderBlood)
print(spider.__dict__)