class Iterator:
    def __init__(self,target) -> None:
        self.__target = target
        self.__index = 0

    def __next__(self):
        if self.__index > len(self.__target)-1:
            raise StopIteration
        temp = self.__target[self.__index]
        self.__index += 1
        return temp


class Skill:
    pass
class Manager:
    def __init__(self):
        self.__list = []

    def add_skill(self,skill):
        self.__list.append(skill)

    def __iter__(self):
        return Iterator(self.__list)

manager = Manager()
manager.add_skill(Skill())
manager.add_skill(Skill())



for item in manager:
    print(item)

iterator = manager.__iter__()
while True:
    try:
        item = iterator.__next__()
        print(item)
    except:
        break