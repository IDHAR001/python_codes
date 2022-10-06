from logging.config import valid_ident
from multiprocessing.sharedctypes import Value


class Player:
    __slots__ = ("__atk","__blood")

    def __init__(self,atk,blood) -> None:
        self.atk = atk
        self.blood = blood

    @property
    def atk(self):
        return self.__atk

    @atk.setter
    def atk(self,value):
        self.__atk = value

    @property
    def blood(self):
        return self.__blood

    @blood.setter
    def blood(self,value):
        self.__blood = value    

    def attack(self,target):
        target.damage(self.atk)

class Enemy:
    def __init__(self,atk,blood) -> None:
        self.atk = atk
        self.blood = blood

    @property
    def atk(self):
        return self.__atk

    @atk.setter
    def atk(self,value):
        self.__atk = value

    @property
    def blood(self):
        return self.__blood

    @blood.setter
    def blood(self,value):
        self.__blood = value  

    def damage(self,value):
        self.blood -= value
        print("扣了%d血"%(value))
        if self.blood <= 0:
            self.__death()
    
    def __death(self):
        print("敌人 死了")

    def attack(self,target):
        target.blood -= self.atk  
        print("player掉了"+str(target.blood)+"血")
        if target.blood == 0:
            print("player被打败了")

idhar = Player(10,100)
spider = Enemy(10,100)
idhar.atk = 100
idhar.attack(spider)
spider.atk = 100
spider.attack(idhar)

# spider._Enemy__death()
