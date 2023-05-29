# day 西西艾弗岛上树的棵数, L 绿化图的大小, S 藏宝图的大小
n, L, S = map(int, input().split())

# 输入绿化图中 n 棵树的坐标 x,y
A_trees = [[int(a) for a in input().split()] for i in range(0, n)]

# 输入完整的藏宝图S（逆序）
B = [[int(a) for a in input().split()] for i in range(0, S + 1)]
B.reverse()

