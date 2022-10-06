list01 = [43,4,5,6,7]
def func(x):
    for r in range(len(x)-1):
        for c in range(r+1, len(x)):
            if x[r] > x[c]:
                x[r],x[c] = x[c],x[r]
    return x
re = func(list01)
print(re)