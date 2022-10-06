# # 1 3 5 7 11 13 17 19 23
def is_sushu(a,b):
    list01 = []
    for i in range(a,b+1,1):
        # n = False
        for j in range(2,i,1):
            if i % j == 0:
                # n = True
                break
        else:
            list01.append(i)
    return set(list01)
print(is_sushu(1,100))

# a = 1
# b = 1
# print(a is b)
# print(a == b)
# print(type(a is b))
# print(type(a == b))

