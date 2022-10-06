from re import I


list01 = ["无忌","赵","周"]
list02 = [101,102,103]
dict01 = {}
for i in range(0,len(list01),1):
    dict01[list01[i]] = list02[i]
print(dict01)

dict01 = {list01[i]:list02[i] for i in range(0,len(list01),1)}
print(dict01)

dict02 = {value:key for key,value in dict01.items()}
print(dict02)

# 字典如果key重复，互换会丢失数据
# 如果需要保存数据
# [(k,v)]
list03 = [(key,value) for key,value in dict01.items()]