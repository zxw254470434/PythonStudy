n, L, t = map(int, input().split())
# 记录n个小球的原始位置
origin_location = [int(a) for a in input().split()]
# 对小球的位置进行排序
location = [a for a in origin_location]
location.sort()
# 记录排好序的小球的原始位置
index = [origin_location.index(a) for a in location]

# 记录小球运动的方向，左-1右1
direction = [1] * n

for i in range(0, t):
    for j in range(0, n):
        location[j] += direction[j]
    for j in range(0, n - 1):
        if location[j] == 0:
            direction[j] = -direction[j]
        elif location[j] == location[j + 1]:
            direction[j] = -direction[j]
            direction[j + 1] = -direction[j + 1]
    if location[n - 1] == L:
        direction[n - 1] = -direction[n - 1]

result = [0] * n
for i in range(0, n):
    result[index[i]] = location[i]
for i in range(0, n - 1):
    print(result[i], end=' ')
print(result[n - 1], end=' ')
