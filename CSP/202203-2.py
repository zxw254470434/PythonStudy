n, m, k = map(int, input().split())
t_c = [[int(a) for a in input().split()] for i in range(0, n)]

result = []
for i in range(0, m):
    count = 0
    q = int(input())
    start = q + k
    for j in range(0, n):
        t, c = t_c[j][0], t_c[j][1]
        if start <= t <= start + c - 1:
            count += 1

    result.append(count)

for i in range(0, m - 1):
    print(result[i])
print(result[- 1], end='')
