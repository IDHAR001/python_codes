import random

list01 = []
list02 = []
list03 = []
while len(list01) < 6:
    random_number = random.randrange(1,33)
    if random_number not in list01:
        list01.append(random_number)
print(list01)

while len(list02) < 1:
    random_number = random.randrange(1,16)
    if random_number not in list02:
        list02.append(random_number)
print(list02)

i = 1
k = 1
while i < 3:
    num01 = int(input("请输入第%d个红球号码:"%(i)))
    if num01 not in list01:
        print("号码不在范围内")
        continue
    elif num01 in list03:
        print("号码已经重复")
        continue
    else:
        list03.append(num01)
        i += 1
        if i == 3:
            while k < 2:
                num02 = int(input("请输入蓝球号码:"))
                if num02 not in list02:
                    print("号码不在范围内")
                    continue
                elif num02 in list03:
                    print("号码已经重复")
                    continue
                else:
                    list03.append(num02)
                    k += 1
        continue
print(list03)
    

