from operator import le


str01 = "How are you"
list01 = str01.split(" ")
# list02 = []
print(list01)
# for i in range(len(list01)-1,-1,-1):
#     list02.append(list01[i])
# print(" ".join(list02))
list02 = " ".join(list01[::-1])
print(list02)