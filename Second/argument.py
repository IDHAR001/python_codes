def func(a,b,c,d):
    print(a)
    print(b)
    print(c)
    print(d)

# 序列实参：星号将序列拆分后按位置与形参进行对应
list01 = ["a","b","c","d"]
func(*list01)
# 字典实参：拆分后按名称与形参进行对应
dict01 = {"a":1,"b":2,"c":3,"d":4}
func(**dict01)