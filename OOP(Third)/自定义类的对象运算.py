class Vector:
    def __init__(self,x) -> None:
        self.x = x
    
    def __str__(self) -> str:
        return str(self.x)
    
    def __add__(self,other):
        return Vector(self.x + other)

    def __sub__(self,other):
        return Vector(self.x - other)
    
    # 数值与对象的运算，r开头
    def __radd__(self,other):
        return Vector(other + self.x)

    # += 
    # 算术运算符会返回新的对象，符合运算符在自身操作
    # 如果这时候调用 += ，在没有写__iadd__方法的情况下，会去调用__add__方法，生成一个新的对象
    def __iadd__(self,other):
        self.x += other
        return self
    
v01 = Vector(10)
print(v01 + 2)
print(v01 - 3)
print(10 + v01)
v01 += 2
print(v01)
