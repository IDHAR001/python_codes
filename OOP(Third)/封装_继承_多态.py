from cmath import pi

class ImageController:
    def __init__(self) -> None:
        self.__images = []
    
    def add_images(self,image):
        if not isinstance(image, Image):
            raise ValueError("不是图形")
        self.__images.append(image)
        
    def getArea(self,image_target):
        if not isinstance(image_target, Image):
            raise ValueError("没多态啊")
        print(image_target.area())
        
class Image:
    def area(self):
        raise NotImplementedError("没继承啊")

class Circle(Image):
    def __init__(self,r) -> None:
        super().__init__()
        self.__r = r
    
    @property
    def r(self):
        return self.__r 
    
    @r.setter
    def r(self,value):
        self.__r = value
        
    def area(self):
        return pi*self.r**2

class Rectange(Image):
    def __init__(self,long,wide) -> None:
        super().__init__()
        self.__long = long
        self.__wide = wide
    
    @property
    def long(self):
        return self.__long
    
    @long.setter
    def long(self,value):
        self.__long = value
    
    @property
    def wide(self):
        return self.__wide
    
    @wide.setter
    def wide(self,value):
        self.__wide = value
        
    def area(self):
        return self.long * self.wide
    
c01 = Circle(10)
r01 = Rectange(10,20)
i01 = Image()
controller1 = ImageController()
controller1.add_images(c01)
controller1.add_images(r01)
controller1.add_images(i01)
controller1.getArea(c01)
controller1.getArea(r01)
controller1.getArea(i01)