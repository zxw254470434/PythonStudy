n, m, L = map(int, input().split())

# 灰度直方图
h = [0] * L

for i in range(0, n):
    row = input().split()
    for j in range(0, m):
        row[j] = int(row[j])
        h[row[j]] += 1

for i in range(0, L):
    if i != L - 1:
        print(h[i], end=' ')
    else:
        print(h[i], end='')
