# 猜数字
import random


randomNum01 = random.randint(1,10)
i = 0

# while True:
#     num01 = int(input("猜一个数,1~10 \n"))
#     i += 1
#     if i < 3:
#         if num01 == randomNum01:
#             print("猜对了，猜了%d次"%(i))
#             break
#         elif num01 < randomNum01:
#             print("猜小了")
#             continue
#         elif num01 > randomNum01:
#             print("猜大了")
#             continue
#     else:
#         print("三次已满，游戏结束")
#         break

while i < 3:
    num01 = int(input("猜一个数,1~10 \n"))
    i += 1
    if num01 == randomNum01:
        print("猜对了，猜了%d次"%(i))
        break
    elif num01 < randomNum01:
        print("猜小了")
        continue
    elif num01 > randomNum01:
        print("猜大了")
        continue
else:
    print("三次已满，游戏结束")
