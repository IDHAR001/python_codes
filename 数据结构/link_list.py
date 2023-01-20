class Node():
    def __init__(self,value,next=None):
        self.value = value
        self.next = next
        
class LinkList:
    def __init__(self):
        self.head = Node(None)

    def init_list(self,list_):
        p = self.head
        for i in list_:
            p.next = Node(list_[i-1])
            p = p.next
    
    # 遍历链表
    def show_value(self):
        p = self.head.next
        while p is not None:
            print(p.value)
            p = p.next
            
    # 判断链表为空
    def is_empty(self):
       if self.head.next is None:
           print("链表为空")
           return True
       else:
            return False

    # 清空链表
    def clear(self):
        self.head.next = None
    
    # 尾部插入
    def append(self,value):
        p = self.head
        while p.next is not None:
            p = p.next
        p.next = Node(value)
        
    # 头部插入
    def head_insert(self,value):
        p = self.head
        node = Node(value)
        node.next = p.next
        p.next = node
        
    # 指定插入位置
    def insert(self, index, value):
        p = self.head
        for i in range(index):
            if p.next is None: #超出位置最大范围，跳出循环
                break
            p = p.next
        node = Node(value)
        node.next = p.next
        p.next = node
        












# list = LinkList()
# list.init_list([1,2,3,4,5])
# print(list.head.next.next.value)
# list.show_value()
# print(list.head.next.next.next.value)
# 一个一个创建节点添加
# node01 = Node(1)
# node02 = Node(2)
# node03 = Node(3)
# list01.head.next = node01
# print(list01.head.next)
# node01.next = node02
# print(node01.next.value)
# print(list01.head.next.next.value)

# 加一个函数添加节点 p = p.next 
