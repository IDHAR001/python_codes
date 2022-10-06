# 失败


import random

list01 = []
list02 = []
list03 = []
totalList = []
while True:
    redBall = random.randint(1,33)
    if redBall in list01:
        continue
    list01.append(redBall)
    if len(list01) == 33:
        break
print(list01)
while True:
    blueBall = random.randint(1,16)
    if blueBall in list02:
        continue
    list02.append(blueBall)
    if len(list02) == 16:
        break   
print(list02)

for item in list01:
    list03.append(item)
    if len(list03) == 6:
        for j in range(len(list02)-1,-1,-1):
            list03.append(list02[j])
            list02.remove(list02[j])
            totalList.append(list03[:])
            for k in range(len(list03)-1,-1,-1):
                list03.remove(list03[k])
                if list03 == [""]:
                    break
            break
    if list03 in totalList:
        break
print(totalList)


