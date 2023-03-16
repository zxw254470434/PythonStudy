n, m = map(int, input().split())
martix = []
for i in range(0, n):
    row = input().split()
    for j in range(0, m):
        row[j] = int(row[j])
    martix.append(row)

for i in range(m - 1, -1, -1):
    for j in range(0, n):
        if j != n - 1:
            print(martix[j][i], end=' ')
        else:
            if i != 0:
                print(martix[j][i])
            else:
                print(martix[j][i], end='')
