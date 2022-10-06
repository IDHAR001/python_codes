def change(x):
    for c in range(1,len(x)):
        for r in range(c,len(x)):
            x[r][c-1],x[c-1][r] =  x[c-1][r],x[r][c-1]

list01 = [
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12],
    [13,14,15,16]
]
change(list01)
print(list01)