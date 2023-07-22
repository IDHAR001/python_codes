import time
from new_input import default_input

f = open("./file/time.txt", "a")
a = 1
while True:
    s = "%d. %s \n"%(a, time.ctime())
    a += 1
    f.write(s)
    f.flush()
    time.sleep(1)
    
    