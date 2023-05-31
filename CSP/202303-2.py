n, m, k = map(int, input().split())
l_c = [[int(a) for a in input().split()] for i in range(0, n)]

l_c.sort(key=lambda x: x[0])

max_day = l_c[n - 1][0]
min = l_c[n - 1][0]

for i in range(k, max_day):
    source = 0
    temp = [item[0] for item in l_c]
    for j in range(n - 1, -1, -1):
        source += l_c[j][1] * (l_c[j][0] - i)
        if source > m:
            break
        temp[j] = i

    is_find = True
    for j in range(0, n):
        if temp[j] > i:
            is_find = False
            break
    if is_find:
        min = i
        break
print(min, end='')