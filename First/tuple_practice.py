from curses import mouseinterval


day28Month = 2
day30Month = (4,6,9,11)
totalMonth = (1,2,3,4,5,6,7,8,9,10,11,12)
month = int(input("输入月份："))

if month not in totalMonth:
    print("wrong month")
elif month == day28Month:
    print("28天")
elif month in day30Month:
    print("30天")
else:
    print("31天")