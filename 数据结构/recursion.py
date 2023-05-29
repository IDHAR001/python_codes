def jiecheng(arg):
    a=1
    for i in range(1,arg+1):
        a = a*i
    return a

print(jiecheng(5))

def recursion(num):
    if num <= 1:
        return num * recursion(num - 1)