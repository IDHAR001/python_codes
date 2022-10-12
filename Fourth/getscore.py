# def get_score():
#     score = int(input("输入成绩:"))
#     print(score)
#     return score

# while True:
#     try:
#         score = get_score()
#         if 0 <= score <= 100:
#             print(score)            
#             break
#         else:
#             print("成绩超出范围")
#             continue
#     except ValueError:
#         print("值有问题")

# print("做完了")

def get_score():
    while True:
        str_result = input("输入成绩:")
        try:
            score = int(str_result)
        except ValueError:
            print("值有问题")
            continue
        if 0 <= score <= 100:
            print(score)            
            break
        else:
            print("成绩超出范围")
            continue
get_score()