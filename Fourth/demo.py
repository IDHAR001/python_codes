import time

print(time.time())
print(time.localtime())
print(time.struct_time)

time_tuple = time.localtime()
print(time.strftime("%y,%m,%d",time_tuple))