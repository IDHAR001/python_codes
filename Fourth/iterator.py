# tuple1 = ("idhar","lingjie","qwer")
# iterator = tuple1.__iter__()
# while True:
#     try:
#         item = iterator.__next__()
#         print(item)
#     except:
#         break

from email import iterators


dict1 = {0:"idhar",1:"lingjie",2:"qwer"}
iterator = dict1.__iter__()
while True:
    try:
        item = iterator.__next__()
        print(dict1[item])
    except:
        break
        