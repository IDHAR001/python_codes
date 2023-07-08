# 算法训练

# 冒泡
def bubble(list):
    for i in range(len(list)):
        for j in range(1,len(list) - i):
            if list[j-1] > list[j]:
                list[j-1], list[j] = list[j], list[j-1]
        # for j in range(1,len(list)):
        #             if list[j-1] > list[j]:
        #                 list[j-1], list[j] = list[j], list[j-1]

# 快排

# 完成一轮交换
def sub_sort(list, low, high):
    # 选定基准
    x = list[low]
    # low向后，high向前
    while low < high:
        # 后面的数往前放
        while list[high] >= x and low < high:
            high -= 1
        list[low] = list[high]
        # 前面的数往后放
        while list[low] < x and low < high:
            low +=1
        list[high] = list[low]
    list[low] = x
    return low
        
def quick(list, low, high):
    # low表示列表第一个元素索引，high表示列表最后一个元素索引
    if low < high:
        key = sub_sort(list, low, high)
        quick(list, low, key-1)
        quick(list, key+1, high)
            

l = [4,9,3,1,6,5,8,2]
# bubble(l)
# print(l)
# print(len(l))
quick(l, 0, len(l)-1)
print(l)