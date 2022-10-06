list01 = [9,25,12,8]
a = 0
for i in range(0,len(list01)-1,1):
    a += 1
    if list01[a-1] > 10:
        del list01[a-1]
        # list01.remove(a-1)
        a -= 1
    else:
        print(a-1)
        print(list01[a-1])
print(list01)

# list02 = [1,2,3]
# list02.remove(list02[2])
# print(list02[2])

# list03 = [4,5,6]
# del list03[2]
# print(list03[2])

# list04 = [1,2,3]
# a = list04[0]
# del a
# print(list04)

for i in range(len(list01)-1,-1,-1):
    if list01[i] > 10:
        list01.remove[list01[i]]
        # del list01[i]
print(list01)