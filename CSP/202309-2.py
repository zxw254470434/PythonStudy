from math import cos, sin

n, m = map(int, input().split())
operations = []
K = [0]
Theta = [0]
for i in range(0, n):
    k, theta = map(float, input().split())
    operations.append([k, theta])
    K.append(K[-1] + k)

    Theta.append(Theta[-1] + theta)

results = []
for l in range(0, m):
    i, j, x, y = map(int, input().split())
    k = K[j] - K[i - 1]
    theta = Theta[j] - Theta[i - 1]

    print(k)
    print(theta)
    x = x * k
    y = y * k
    new_x = x * cos(theta) - y * sin(theta)
    new_y = x * sin(theta) + y * cos(theta)

    results.append([new_x, new_y])

print(K)
print(Theta)
for i in range(0, m):
    if i != m - 1:
        print(results[i][0], results[i][1])
    else:
        print(results[i][0], results[i][1], end='')
