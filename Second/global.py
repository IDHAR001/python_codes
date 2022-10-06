i = 0
def func():
    global i
    i+=1 
    return 1
func()
func()
func()
print(i)
