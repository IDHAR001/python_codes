# 二叉树节点
class Node:
    def __init__(self, val, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = right
    
# 二叉树遍历类
class Bitree:
    def __init__(self, root=None) -> None:
        self.root = root

    def preOrder(self, node):
        if node is None:
            return
        print(node.val)
        self.preOrder(node.left)
        self.preOrder(node.right)
        
if __name__ == "__main__":
    # b f g d i h d e c a
    # 根据后续遍历构建二叉树
    b = Node('b')
    f = Node('f')
    g = Node('g')
    d = Node('d', f, g)
    i = Node('i')
    h = Node('h')
    e = Node('e', i, h)
    c = Node('c', d, e)
    a = Node('a', b ,c) #树根
    
    # 将a作为遍历的起始位置
    bt = Bitree(a)
    bt.preOrder(a)