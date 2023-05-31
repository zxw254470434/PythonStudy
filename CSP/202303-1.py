n, a, b = map(int, input().split())
s = 0
for i in range(0, n):
    x_1, y_1, x_2, y_2 = map(int, input().split())
    x = [0, a, x_1, x_2]
    y = [0, b, y_1, y_2]
    x.sort()
    y.sort()
    if 0 <= x[1] and x[2] <= a and 0 <= y[1] and y[2] <= b:
        s += (x[2] - x[1]) * (y[2] - y[1])

print(s, end='')
