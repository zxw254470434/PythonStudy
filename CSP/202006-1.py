n, m = map(int, input().split())

points = []
for i in range(0, n):
    point = input().split()
    point[0] = int(point[0])
    point[1] = int(point[1])
    points.append(point)

lines = []
for i in range(0, m):
    line = input().split()
    line[0] = int(line[0])
    line[1] = int(line[1])
    line[2] = int(line[2])
    lines.append(line)

is_perfect = ['Yes'] * m
for i in range(0, m):
    line = lines[i]
    theta_0, theta_1, theta_2 = line[0], line[1], line[2]
    bigger = []
    less = []

    for j in range(0, n):
        point = points[j]
        x, y, point_type = point[0], point[1], point[2]
        if theta_0 + theta_1 * x + theta_2 * y > 0:
            bigger.append(point_type)
        else:
            less.append(point_type)

    num_b = len(bigger)
    num_l = len(less)
    for b in range(0, num_b - 1):
        if bigger[b] != bigger[b + 1]:
            is_perfect[i] = 'No'
            break
    for l in range(0, num_l - 1):
        if less[l] != less[l + 1]:
            is_perfect[i] = 'No'
            break

for i in range(0, m):
    if i != m - 1:
        print(is_perfect[i])
    else:
        print(is_perfect[i], end='')
