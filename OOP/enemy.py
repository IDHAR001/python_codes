class Enemy:
    def __init__(self,name,blood,attack_power,defense_power):
        self.name = name
        self.blood = blood
        self.attack_power = attack_power
        self.defense_power = defense_power
    
    @staticmethod
    def search_mieba(list):
        for item in list:
            if item.name == "灭霸":
                print(list.index(item))
    
    @staticmethod
    def search_death(list):
        list_death = []
        for item in list:
            if item.blood == 0:
                list_death.append(item)
        return list_death
    
    @staticmethod
    def cal_ave_attack_power(list):
        total_attack_power = 0
        for i in range(len(list)):
            total_attack_power += list[i].attack_power
        ave_attack_power = total_attack_power/len(list)
        return ave_attack_power
    
    @staticmethod
    def del_low_power(list):
        for i in range(len(list)-1,-1,-1):
            if list[i].attack_power < 10:
                list.remove(list[i])

    @staticmethod
    def add_attack_power(list):
        for item in list:
            item.attack_power += 50
        
bat = Enemy("bat",10,1,100)
mieba = Enemy("灭霸",100,10,10)
idhar = Enemy("idhar",100,80,8)
spider = Enemy("spider",0,10,7)
enemy_list = [bat,mieba,idhar,spider]

# Enemy.search_mieba(enemy_list)
# listDeath = Enemy.search_death(enemy_list)
# for item in listDeath:
#     print(item.name)

# ave_attack_power = Enemy.cal_ave_attack_power(enemy_list)
# print(ave_attack_power)

Enemy.del_low_power(enemy_list)
for item in enemy_list:
    print(item.name)

Enemy.add_attack_power(enemy_list)
for item in enemy_list:
    print(item.attack_power)
