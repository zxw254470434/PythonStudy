n, L, r, t = map(int, input().split())
# 矩阵
A = [[0 for j in range(0, n + 1)] for i in range(0, n + 1)]
S = [[0 for j in range(0, n + 1)] for i in range(0, n + 1)]
# 记录矩阵的二维前缀和
for i in range(0, n):
    row = input().split()
    for j in range(0, n):
        A[i + 1][j + 1] = int(row[j])
        S[i + 1][j + 1] = S[i][j + 1] + S[i + 1][j] - S[i][j] + A[i + 1][j + 1]


def average(x1, y1, x2, y2):
    sum = S[x2 + 1][y2 + 1] - S[x1][y2 + 1] - S[x2 + 1][y1] + S[x1][y1]
    num = (x2 - x1 + 1) * (y2 - y1 + 1)
    return sum / num


count = 0
for i in range(0, n):
    for j in range(0, n):
        x1 = max(0, i - r)
        y1 = max(0, j - r)
        x2 = min(n - 1, i + r)
        y2 = min(n - 1, j + r)
        if average(x1, y1, x2, y2) <= t:
            count += 1

print(count, end='')
