n, X, Y = map(int, input().split())

i_d = []
for i in range(1, n + 1):
    x, y = map(int, input().split())
    d = (X - x) ** 2 + (Y - y) ** 2
    temp = [i, d]
