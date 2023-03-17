N, M = map(int, input().split())
windows = []
for i in range(0, N):
    x_1, y_1, x_2, y_2 = map(int, input().split())
    window = [i + 1, x_1, y_1, x_2, y_2]
    windows.append(window)
windows.reverse()

windows_number = []
for i in range(0, M):
    x, y = map(int, input().split())
    clicked = False
    for j in range(0, N):
        x_1, y_1, x_2, y_2 = windows[j][1], windows[j][2], windows[j][3], windows[j][4]
        if x_1 <= x <= x_2 and y_1 <= y <= y_2:
            temp = windows[j]
            windows.pop(j)
            windows.insert(0, temp)
            clicked = True
            windows_number.append(temp[0])
            break
    if not clicked:
        windows_number.append('IGNORED')

for i in range(0, M):
    if i != M - 1:
        print(windows_number[i])
    else:
        print(windows_number[i], end='')
