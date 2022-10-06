'''
实例方法：操作对象的变量
类方法：操作类的变量
静态方法：既不操作实例变量也不操作类变量
'''
class Vector:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    @staticmethod
    def left():
        return Vector(0,-1)

    @staticmethod
    def right():
        return Vector(0,1)

    @staticmethod
    def up():
        return Vector(-1,0)
    
    @staticmethod
    def down():
        return Vector(1,0)

class DoubleListHelper:
    @staticmethod
    def get_elements(target,vect_pos,vect_dir,count):
        list_result = []
        for i in range(count):
            vect_pos.x += vect_dir.x
            vect_pos.y += vect_dir.y
            element = target[vect_pos.x][vect_pos.y]
            list_result.append(element)
        return list_result  

list01 = [
    ["00","01","02","03"],
    ["10","11","12","13"],
    ["20","21","22","23"],
    ["30","31","32","33"],
]

post01 = Vector(0,1)
l01 = Vector.left()
post01.x += l01.x
post01.y += l01.y

post02 = Vector(3,3)
l02 = Vector.up()
post02.x += l02.x
post02.y += l02.y

re = DoubleListHelper.get_elements(list01,Vector(1,0),Vector.left(),3)
print(re)
re2 = DoubleListHelper.get_elements(list01,Vector(3,0),Vector.up(),2)
print(re2)

