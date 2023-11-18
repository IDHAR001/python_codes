# 自定义异常
class StackError(Exception):
    pass


# 栈模型的顺序存储

# 列表即顺序存储，但功能太多，需要进行封装，提供接口

class SStack:
    def __init__(self):
        # 空列表是栈的存储空间，列表最后一个元素作为栈顶
        self._elems = []
        
    def is_empty(self):
        return self._elems == []

    def push(self, value):
        self._elems.append(value)
    
    def pop(self):
        if self.is_empty():
            raise StackError("stack is empty")
        else:    
            return self._elems.pop()
    
    # 查看栈顶元素
    def top(self):
        if self.is_empty():
            raise StackError("stack is empty")
        else:   
            return self._elems[-1]
        
        
if __name__ == '__main__':
    st = SStack()
    st.push(10)
    st.push(20)
    while not st.is_empty():
        print(st.pop())