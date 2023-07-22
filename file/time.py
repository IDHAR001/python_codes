# 这里有问题
import time
from func_timeout import FunctionTimedOut, func_timeout
from new_input import default_input

f = open("./file/time.txt", "a")
a = 1
while True:
    s = "%d. %s"%(a, time.ctime())
    f.write(s)
    f.flush()
    time.sleep(2)
    anwser = default_input()
    if anwser == "continue":
        print("continue")
    a += 1
    