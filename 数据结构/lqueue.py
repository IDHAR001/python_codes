class QueueError(Exception):
    pass


class Node:
    def __init__(self, val, next=None) -> None:
        self.val = val
        self.next = next
        
# 队列操作
class LQueue:
    def __init__(self) -> None:
        # 定义对头和队尾变量
        self.front = self.rear = Node(None)
        
    def is_empty(self):
        return self.front == self.rear
    
    def enqueue(self, val):
        self.rear = self.rear.next = Node(val)
        
    def dequeue(self):
        if self.front == self.rear:
            raise QueueError("Queue is empty")
        self.front = self.front.next
        return self.front