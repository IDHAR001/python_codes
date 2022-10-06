# list01 = []
# for i in range(1970,2051,1):
#     if i % 4 == 0:
#         list01.append(i)


# list02 = [i for i in range(1970,2051,1) if i%4 == 0]
# print(list02)


# dictJingqu_beijing = {"景区":["故宫","天安门","天坛"]}
# dictMeishi_beijing = {"美食":["烤鸭","炸酱面","豆汁"]}
# dictJingqu_sichuan = {"景区":["九寨沟","峨眉山","春熙路"]}
# dictMeishi_sichuan = {"美食":["火锅","串串香","兔头"]}
# dictBeijing = {"北京":[dictJingqu_beijing,dictMeishi_beijing]}
# dictSichuan = {"四川":[dictJingqu_sichuan,dictMeishi_sichuan]}
# list01 = [dictBeijing,dictSichuan]
# for item in list01:
#     print(item)
# print(list01[0]["北京"][0]["景区"])

from time import strftime


str01 = "abcdefce"
dict01 = {}
for item in str01:
    if item not in dict01:
        dict01[item] = 1
    elif item in dict01:
        dict01[item] += 1
print(dict01)