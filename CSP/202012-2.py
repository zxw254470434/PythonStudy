m = int(input())
y_result = []
theta_set = set()
for i in range(0, m):
    y, r = map(int, input().split())
    y_result.append([y, r])
    theta_set.add(y)

# 按y大小排序
y_result.sort(key=lambda x: x[0])

best_num_right = 0
best_theta = 0
for theta in theta_set:
    temp_num_right = 0
    for i in range(0, m):
        y, r = y_result[i][0], y_result[i][1]
        if y < theta and r == 0:
            temp_num_right += 1
        elif y >= theta and r == 1:
            temp_num_right += 1

    if temp_num_right > best_num_right:
        best_num_right = temp_num_right
        best_theta = theta
    elif temp_num_right == best_num_right:
        if theta > best_theta:
            best_theta = theta

print(best_theta, end='')
