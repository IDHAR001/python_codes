str01 = "  校  训：、。  "
list01 = []
for item in str01:
    list01.append(item)
for item in str01:
    if item == " ":
        list01.remove(item)
    elif item != " ":
        break
for i in range(len(list01)-1,-1,-1):
        if list01[i] == " ":
            list01.remove(list01[i])
        else:
            break
print(list01)
print(str01.count(" "))