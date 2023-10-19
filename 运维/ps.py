import psutil
import math
mem = psutil.virtual_memory()
print(mem)
print("total:",mem.total/1024/1024, "used:",mem.used/math.pow(1024,2))
print(psutil.cpu_times())
print(psutil.cpu_count())
print(psutil.disk_usage("/").total/math.pow(1024,3))
# print(type(psutil.disk_usage("/").total))


# print(psutil.pids())
print(psutil.Process(71586))
print(psutil.Process(71586).connections())

print(psutil.Process(72212))
print(psutil.Process(72212).connections())