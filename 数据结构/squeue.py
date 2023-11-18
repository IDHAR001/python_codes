class QueueError(Exception ):
    pass

class SQueue:
    def __init__(self) -> None:
        self._elems = []
        
    
    # 判断队列是否为空
    def is_empty(self):
        return self._elems == []
    
    # 入队
    def enqueue(self,val):
        self._elems.append(val)
    
    # 出队
    def dequeue(self):
        if not self._elems:
            raise QueueError("Queue is empty")
        return self._elems.pop(0)
    
    def lsqueue(self):
        print(sq._elems)
if __name__ == "__main__":
    sq = SQueue()
    for i in range(10):
        sq.enqueue(i)
    
    print(sq.lsqueue())
    list = []
    
    while not sq.is_empty():
        list.append(sq.dequeue())
        # print(list)
    
    for i in range(len(list)):
        for j in range(len(list)-1):
            if list[j] < list[j+1]:
                list[j],list[j+1] = list[j+1],list[j]
    
    for i in range(len(list)):
        sq.enqueue(list[i])

    print(sq.lsqueue())