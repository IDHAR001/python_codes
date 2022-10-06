# 2048游戏核心算法

# 零元素移至末尾

list_merge = []

def zero_to_end():
    '''
        零元素移动到末尾
    '''
    # 从后向前，如果发现零元素，删除并追加
    for i in range(-1,-len(list_merge)-1,-1):
        if list_merge[i] == 0:
            del list_merge[i]
            list_merge.append(0)

def merge():
    '''
        相同数字合并
    '''
    # [2,0,0,2] -> [2,2,0,0]
    zero_to_end() 

    # [2,2,0,0] -> [4,0,0,0]
    for i in range(1,len(list_merge)):
        if list_merge[i-1] == list_merge[i]:
            list_merge[i-1] += list_merge[i]
            del list_merge[i]
            list_merge.append(0)

map = [
    [2,0,2,2],
    [4,0,2,2],
    [2,4,0,2],
    [0,0,2,2],
]
# 地图向左移动

def move_left(x):
    for line in x:
        global list_merge
        list_merge = line
        merge()

# 地图向右移动
def move_right(x):
    for line in x:
        global list_merge
        list_merge = line
        merge()
        list_merge.reverse()

# 地图向上移动，向下移动
def change(x):
    for c in range(1,len(x)):
        for r in range(c,len(x)):
            x[r][c-1],x[c-1][r] =  x[c-1][r],x[r][c-1]
def move_up(x):
    global list_merge
    change(x)
    move_left(x)
    change(x)

def move_down(x):
    global list_merge
    change(x)
    move_right(x)
    change(x)

