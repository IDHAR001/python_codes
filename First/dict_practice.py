dict01 = {}
while True:
    name = input("输入商品名称")
    if name == "":
        break
    price = input("输入商品单价")
    dict01[name] = price

for k,v in dict01.items():
    print("商品名：%s"%k)
    print("单价：%s"%v)
    print("-------------")
