import copy
list01 = [54,25,12,42,35,17]
list02 = []
i = 0
for i in range(0,len(list01),1):
    if list01[i] > 30:
        list02.append(list01[i])
    # else:
    #     continue
    i +=1
print(list02)

# import copy
# list01 = [54,25,12,42,35,17]
# list02 = []
# i = 0
# for i in range(0,len(list01),1):
#     if list01[i] > 30:
#         list02 = list01.copy()
#     else:
#         continue
#     i +=1
# print(list02)