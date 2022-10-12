import time


def get_week(year,month,day):
    # time_tuple = time.localtime()
    time_tuple = time.strptime("%d-%d-%d"%(year,month,day),"%Y-%m-%d")
    # print(time_tuple)
    week = int(time.strftime("%w",time_tuple))
    dict01 = {0:"星期日",1:"星期一",2:"星期二",3:"星期三",4:"星期四",5:"星期五",6:"星期六"}
    return dict01[week]

print(get_week(2022,10,16))

# print(time.localtime())