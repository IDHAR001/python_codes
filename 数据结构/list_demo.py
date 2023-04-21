class Node():
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

class NodeList():
    def __init__(self):
        self.head = Node(None)
    
    def bubbleSort(arr):
        for i in range(1, len(arr)):
            for j in range(0, len(arr)-i):
                if arr[j] > arr[j+1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
        return arr

    def init_list(self,list_):
        p = self.head
        for i in range(1, len(list_)+1):
            p.next = Node(list_[i-1])
            p = p.next
                
                
    def show_value(self):
        p = self.head.next
        list = []
        while p is not None:
            list.append(p.value)
            p = p.next
        NodeList.bubbleSort(list)
        print(list)

    def insert(self, index, value):
        p = self.head
        for i in range(index):
            if p.next is None: #超出位置最大范围，跳出循环
                break
            p = p.next
        node = Node(value)
        node.next = p.next
        p.next = node
           
    def merge(self, list):
        count = 0
        p = self.head.next
        while p is not None:
            for i in range(0, len(list)):
                while True:
                    count += 1
                    if p.value <= list[i]:
                        p = p.next
                    else:
                        # i += 1
                        NodeList.insert(count, list[i])
                        break
                p = p.next
        
list = [6,1,3,2]
l = NodeList()
l.init_list(list)
l.show_value() # 1,2,3,6
list2 = [4,5]
l.merge(list2)
l.show_value()



    # 失败冒泡
    # def init_list(self,list_):
    #     p = self.head
    #     for i in range(1, len(list_)):
    #         for j in range(0, len(list_)-i):
    #             p.next = Node(list_[j-1])
    #             if j >= 1:
    #                 if list_[j] > list_[j+1]:
    #                     list_[j], list_[j+1] = list_[j+1], list_[j]
    #             p = p.next
