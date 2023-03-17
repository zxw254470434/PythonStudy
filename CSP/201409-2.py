n = int(input())
boxs = {}
for i in range(0, n):
    x_1, y_1, x_2, y_2 = map(int, input().split())
    for x in range(x_2, x_1, -1):
        for y in range(y_2, y_1, -1):
            boxs[(x, y)] = 1

print(len(boxs), end='')
