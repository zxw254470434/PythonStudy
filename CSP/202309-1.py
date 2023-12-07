n, m = map(int, input().split())
Dx = 0
Dy = 0
for i in range(0, n):
    dx, dy = map(int, input().split())
    Dx += dx
    Dy += dy

results = []
for i in range(0, m):
    x, y = map(int, input().split())
    x += Dx
    y += Dy
    results.append([x, y])

for i in range(0, m):
    if i == m - 1:
        print(results[i][0], results[i][1], end='')
    else:
        print(results[i][0], results[i][1])
