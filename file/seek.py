f = open('./file/test','rb+')
# 只有二进制可以实现文件偏移量写入成功

f.read(5)
# f.flush()
print("文件偏移量:",f.tell())
f.seek(0,2)
# 0当前位置，1头，2尾
f.write(b"****78887")
f.close()