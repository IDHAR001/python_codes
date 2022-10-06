# numList = []
# i = 0
# while True:
#     num = int(input("输入一个数字"))
#     numList.append(num)
#     i += 1
#     if i == 5:
#         break
# print(numList)

# 假设的最大值
max_value = 0
for item in range(5):
    number = int(input("请输入第%d个数字"%(item+1)))
    if max_value < number:
        max_value = number
print(max_value)
        

