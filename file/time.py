import time
from func_timeout import FunctionTimedOut, func_timeout

f = open("./file/time.txt", "a")
a = 1
while True:
    s = "%d. %s"%(a, time.ctime())
    f.write(s)
    f.flush()
    # time.sleep(2)
    try:
        i = func_timeout(1, lambda: input(">>(continue or stop)") or "continue")
        a += 1

    except FunctionTimedOut:
        print("stop")
        break

        

    