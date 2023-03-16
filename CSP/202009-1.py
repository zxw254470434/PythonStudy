n, X, Y = map(int, input().split())

nearest_3_points = [0] * 3
for i in range(1, n + 1):
    x, y = map(int, input().split())
    d = (X - x) ** 2 + (Y - y) ** 2
    index_dist = [i, d]

    if i > 3:
        for j in range(2, -1, -1):
            if d < nearest_3_points[j][1]:
                nearest_3_points.insert(j, index_dist)
            elif d == nearest_3_points[j][1]:
                if i < nearest_3_points[j][0]:
                    nearest_3_points.insert(j, index_dist)
                else:
                    nearest_3_points.insert(j + 1, index_dist)
    elif i == 1:
        nearest_3_points[0] = index_dist
    elif i == 2:
        if d < nearest_3_points[0][1]:
            nearest_3_points.insert(0, index_dist)
        elif d >= nearest_3_points[0][1]:
            nearest_3_points[1] = index_dist
    elif i == 3:
        if d < nearest_3_points[1][1]:
            nearest_3_points.insert(1, index_dist)
        elif d == nearest_3_points[1][1]:
            nearest_3_points[2] = index_dist
        elif d < nearest_3_points[0][1]:
            nearest_3_points.insert(0, index_dist)
        elif d == nearest_3_points[0][1]:
            nearest_3_points.insert(1, index_dist)
        else:
            nearest_3_points[2] = index_dist

for i in range(0, 3):
    if i != 2:
        print(nearest_3_points[i][0])
    else:
        print(nearest_3_points[i][0], end='')
