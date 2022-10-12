import time

'''
根据生日(年月日)，计算活了多少天
'''

def life_days(year,month,day):
    time_tuple = time.strptime("%d,%d,%d"%(year,month,day),"%Y,%m,%d")
    time_chuo = int(time.mktime(time_tuple))
    now = int(time.time())
    life_time = now - time_chuo 
    print(life_time / 60 / 60 // 24)
    
life_days(1999,12,19)