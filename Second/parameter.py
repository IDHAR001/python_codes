# 缺省（默认）参数
def func(a=0,b=0,c=0,d=0):
    print(a)
    print(b)
    print(c)
    print(d)

# 关键字实参 + 缺省形参：
# 调用者可以随意传递参数
func(b=2,c=3)

# 星号元组形参： * 将所有实参合成一个元组
# 让实参个数无限
def func01(*args):
    print(args)
func01()

def add(*args):
    return sum(args)
print(add(1,2,3,4,5))

# 命名关键字形参
def func02(a,*args,b):
    print(a)
    print(args)
    print(b)
func02(1,b=2)
func02(1,1,2,3,b=2)

# 双星号字典形参：实参可以传递数量无限的关键字实参
def func03(**a):
    print(a)
func03(a=1,b=2,c=3)
