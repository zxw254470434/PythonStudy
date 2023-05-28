n, k, t, xl, yd, xr, yu = map(int, input().split())

num_pass = 0  # 经过的人数
num_stay = 0  # 逗留的人数

for i in range(0, n):
    locations = input().split()
    count = 0  # 记录有几个坐标连续处在高危区域
    is_pass = False  # 是否经过高危区域
    for j in range(0, 2 * t - 1, 2):
        x, y = int(locations[j]), int(locations[j + 1])
        if xl <= x <= xr and yd <= y <= yu:
            is_pass = True
            count += 1
            if count == k:
                break
        else:
            count = 0

    if is_pass:
        num_pass += 1

    if count == k:
        num_stay += 1

print(num_pass)
print(num_stay, end='')
