r, y, g = map(int, input().split())
# 红：1，绿：3，黄2，依次循环
lights = [1, 3, 2]

n = int(input())
T = 0
for i in range(0, n):
    k, t = map(int, input().split())
    if k == 0:
        T += t
        continue
    # 计算这个红绿灯在T时刻的状态
    temp_t = T
    while temp_t > 0:
        t -= 1
        if t == 0:
            if k == 1:
                k = 3
                t = g
            elif k == 2:
                k = 1
                t = r
            else:
                k = 2
                t = y
        temp_t -= 1
    # 计算完之后再进行判断
    if k == 1:
        T += t
    elif k == 2:
        T += t + r
    else:
        continue

print(T, end='')
