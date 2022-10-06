# practice 1
from audioop import avg, avgpp


# list01 = list()
# while True:
#     actor = input("输入你喜欢的明星")
#     if actor != "":
#         list01.append(actor)
#     else:
#         break
# for i in range(0,len(list01),1):
#     print(list01[i])

# practice 2
list02 = []
while True:
    score = input("输入学生成绩")
    if score != "":
        list02.append(int(score))
    else:
        break

for item in list02:
    print(item)

print(max(list02))
print(len(list02))
avg01 = sum(list02)/len(list02)
print(avg01)