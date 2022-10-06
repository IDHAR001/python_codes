list04 = [
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12],
    [13,14,15,16],
]

# for item in list04[2]:
#     print(item)

# for i in range(len(list04)):
#     for k in range(1):
#         print(list04[i][k])

# for r in range(len(list04)):
#     print(list04[r][0])
# for r in range(len(list04)):
#     print(list04[r][1])
# for r in range(len(list04)):
#     print(list04[r][2]) 
# for r in range(len(list04)):
#     print(list04[r][3])
# 矩阵倒置

# list04 = [
#     [1,2,3,4],
#     [5,6,7,8],
#     [9,10,11,12],
#     [13,14,15,16],
# ]
# list04[0][0] -> list05[0][0]
#       i,k    =       (0,0)
# list04[1][0] -> list05[0][1]
#       i,k    =        (0,1)
#       [2][0]          [0][2]
#       [3][0]          [0][3]

# for i in range(len(list04)):
#     for k in range(i+1,len(list04[i])):
#         list04[i][k],list04[k][i] = list04[k][i],list04[i][k]
# print(list04)

result = []
for i in range(len(list04[0])):
    result.append([])
    for k in range(len(list04)):
        result[i].append(list04[k][i])
print(result)