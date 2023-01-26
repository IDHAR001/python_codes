from link_list import *
import time
# l = range(999999)

list = LinkList()
# list.init_list(l)
tm = time.time()

# 访问列表
# 5.5s
# for i in l:
#     print(i)
# print("time: ", time.time() - tm) 

# 访问链表
# 5.5s
# list.show_value()

list.append(86)
list.append(33)

print("time: ", time.time() - tm)

# 理论上来说，顺序表遍历应该是要比链表遍历快的

list.insert(0,3)
# list.show_value()
# list.delete(3)
# list.show_value()
# list.delete(100)
print(list.get_index(0))
