import random as rd
import numpy as np

# 出现正面的概率为 p, 每次出现正面的概率为 x
# 假设投掷次数为n, 正面出现的次数期望值为 E(X) = np,  X表示出现正面的次数
# 每次出现正面的概率x与出现正面的次数X之间的关系是： x = X/n
# 出现正面的概率与每次出现正面的概率之差的绝对值为： |p - x| = |p - X/n|
# |p - X/n| <= 0.01的概率 >= 0.99

prob_front = 0.5
diff_abs = 0.01
target_prob = 0.99

def calculate_min_n(p, diff, target):
    total = 0
    for j in range(10000):
        for i in range(1000):
            X = rd.randint(0,1)
            total += X
        diff = np.abs(X/16641 - p)
        print(diff)
        total = 0
        if diff > diff_abs:
            print(diff)
            total += 1
    
    result = 1 - (total/1000)
    print(result)


calculate_min_n(prob_front, diff_abs, target_prob)