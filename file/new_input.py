from func_timeout import FunctionTimedOut, func_timeout

def new_input():
    arg = input(">>(continue or stop)")
    try:
        if arg != "continue" and arg != "stop":
            raise ValueError("input error")
        return arg
    except ValueError as e:
        print(e)

# print(new_input())

def default_input(default = "continue"):
    try:
        func_timeout(1, lambda: input(">>(continue or stop)"))
    
    except FunctionTimedOut as e:
        print(e)
        return default