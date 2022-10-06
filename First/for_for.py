# 外层循环控制行，内存循环控制列

# for r in range(4):
#     for c in range(3):
#         print("*",end=("#"))
#     print()


from re import I


for r in range(4):
    for c in range(6):
        if c % 2 == 0:
            print("#",end=(""))
        else:
            print("*",end=(""))
    print()

list01 = ["*"]
for r in range(4):
    for c in range(0,4):
        str01 = "".join(list01)
        print(str01)
        list01.append("*")
        if len(list01) > c:
            break
    print()

for r in range(4):            # 0 1 2 3
    for c in range(r+1):      # 1 2 3 4
        print("*",end="")
    print()
    

list02 = [3,80,45,5,7,1]
for i in range(len(list02)-1):
    for k in range(i+1):
        if list02[k] < list02[k+1]:
            list02[k],list02[k+1] = (list02[k+1],list02[k])
print(list02)

list03 = [3,80,45,5,80,1]
for i in range(len(list03)-1):
    for k in range(i+1,len(list03)-1):
        if list03[i] == list03[k]:
            list03.remove(list03[k])
            # pass
print(list03)



