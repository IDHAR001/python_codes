f = open('./file/test','w+')

f.write("hello world")
f.flush()

# 读不出来，文件偏移量的问题，因为写“hello world”已经写到“d”后面了，所以读的时候会从“d”后面开始读
data = f.read()
print(data)

f.close()