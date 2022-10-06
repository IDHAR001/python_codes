list01 = [54,25,12,42,35,17]
max = list01[0]
for item in list01:
    if max < item:
        max = item
print(max)