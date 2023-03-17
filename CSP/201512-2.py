n, m = map(int, input().split())
martix = []
for i in range(0, n):
    row = input().split()
    for j in range(0, m):
        row[j] = int(row[j])
    martix.append(row)

# 解法1，一行一行、一列一列地查找可以删除的元素，将下表记录下来，再统一删除
clear = []
for i in range(0, n):
    counter = 1
    for j in range(0, m - 1):
        if martix[i][j] == martix[i][j + 1]:
            counter += 1
            if counter == 3:
                clear.append([i, j - 1])
                clear.append([i, j])
                clear.append([i, j + 1])
            elif counter > 3:
                clear.append([i, j + 1])
        else:
            counter = 1

for j in range(0, m):
    counter = 1
    for i in range(0, n - 1):
        if martix[i][j] == martix[i + 1][j]:
            counter += 1
            if counter == 3:
                clear.append([i - 1, j])
                clear.append([i, j])
                clear.append([i + 1, j])
            elif counter > 3:
                clear.append([i + 1, j])
        else:
            counter = 1

for i in range(0, len(clear)):
    martix[clear[i][0]][clear[i][1]] = 0

for i in range(0, n):
    if i != n - 1:
        for j in range(0, m):
            if j != m - 1:
                print(martix[i][j], end=' ')
            else:
                print(martix[i][j])
    else:
        for j in range(0, m):
            if j != m - 1:
                print(martix[i][j], end=' ')
            else:
                print(martix[i][j], end='')

# 解法2，边检测边生成新的矩阵
martix_2 = []
for i in range(0, n):
    counter = 1
    temp = martix[i]
    for j in range(0, m - 1):
        if martix[i][j] == martix[i][j + 1]:
            counter += 1
            if counter == 3:
                temp[j - 1] = 0
                temp[j] = 0
                temp[j + 1] = 0
            elif counter > 3:
                temp[j + 1] = 0
        else:
            counter = 1
    martix_2.append(temp)

for j in range(0, m):
    counter = 1
    for i in range(0, n - 1):
        if martix[i][j] == martix[i + 1][j]:
            counter += 1
            if counter == 3:
                martix_2[i - 1][j] = 0
                martix_2[i][j] = 0
                martix_2[i + 1][j] = 0
            elif counter > 3:
                martix_2[i + 1][j] = 0
        else:
            counter = 1

for i in range(0, n):
    if i != n - 1:
        for j in range(0, m):
            if j != m - 1:
                print(martix[i][j], end=' ')
            else:
                print(martix[i][j])
    else:
        for j in range(0, m):
            if j != m - 1:
                print(martix[i][j], end=' ')
            else:
                print(martix[i][j], end='')