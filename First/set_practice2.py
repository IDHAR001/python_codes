from ssl import OPENSSL_VERSION_INFO


dict01 = {"经理":["caocao","liubei","sunquan"]}
dict02 = {"技术":["caocao","liubei","zhangfei","guanyu"]}
set01 = set(dict01["经理"])
print(set01)
set02 = set(dict02["技术"])
print(set01 & set02)
set03 = set01 ^ set02
for item in set03:
    if item in set01:
        print(item)
print(set03)
print(type(set03))

if "zhangfei" in set01:
    print("shijingli")
print("bushi")

