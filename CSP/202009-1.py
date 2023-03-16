n, X, Y = map(int, input().split())
dist_index_type = []
for i in range(1, n + 1):
    x, y = map(int, input().split())
    d = (X - x) ** 2 + (Y - y) ** 2
    dist_index_type.append([d, i, 0])

for i in range(0, 3):
    min = 10000000
    min_index = 0
    for j in range(0, n):
        if dist_index_type[j][0] < min and dist_index_type[j][2] == 0:
            min = dist_index_type[j][0]
            min_index = j
    dist_index_type[min_index][2] = 1

    if i != 2:
        print(dist_index_type[min_index][1])
    else:
        print(dist_index_type[min_index][1], end='')
