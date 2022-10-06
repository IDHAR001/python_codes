import random
from turtle import numinput


list01 = [1,2,3,4,5,6]
# list02 = []
# for item in lis01:
#     list02.append(item+1)
list02 = [item+1 for item in list01]
print(list02)

list02 = [item+1 for item in list01 if item > 10]

listRand = []
# list03 = []
while True:
    num01 = random.randrange(1,11)
    print(num01)
    if num01 not in listRand:
        listRand.append(num01)
    elif len(listRand) == 10:
        break
    else:
        continue
# for item in listRand:
#     list03.append(pow(item,2))
list03 = [pow(item,2) for item in listRand]
print(listRand)
print(list03)

# list04 = []
# list05 = []
# for item in list03:
#     if item%2 == 0:
#         list04.append(item)
#     elif item%2 == 1:
#         list05.append(item)

list04 = [item for item in list03 if item%2 == 0]
list05 = [item for item in list03 if item%2 == 1]

print(list04)
print(list05)


# list06 = []
# for item in list04:
#     if item > 5:
#         list06.append(item + 1)
list06 = [item + 1 for item in list04 if item > 5]
print(list06)

