str01 = "  校  训：、。  "
# list01 = str01.split(None)
# print(list01)
i = 0
for item in str01:
    if item == " ":
        i += 1
print(i)
list01 = str01.split(None)
print(list01)


for i in range(0,len(list01)+1,1):
    for i in range(len(list01)-1,-1,-1):
        if list01[i] == " ":
            list01.remove(list01[i])
        else:
            break
print(list01)
str02 = "".join(list01)
print(str02)

