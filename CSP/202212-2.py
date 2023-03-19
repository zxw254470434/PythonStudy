n, m = map(int, input().split())
depend_subject = [int(item) for item in input().split()]
days = [int(item) for item in input().split()]

# 记录每个项目被哪几个项目依赖 [被依赖的项目号，对别人有依赖的项目号]
be_depended = []
is_Finish = True
earliest_day = [0] * m
latest_day = [0] * m

# 从前向后计算每个项目的最早时间
for i in range(0, m):
    depend_s = depend_subject[i]
    if depend_s == 0:
        earliest_day[i] = 1
    else:
        earliest_day[i] = earliest_day[depend_s - 1] + days[depend_s - 1]
        be_depended.append([depend_s, i + 1])
        if earliest_day[i] + days[i] > n:
            is_Finish = False

# 从后向前计算每个项目的最晚时间
for i in range(m - 1, -1, -1):
    if i == m - 1:
        latest_day[i] = n - days[i] + 1
        continue
    # 记录本项目被哪几个项目依赖
    b_d = []
    for j in range(0, len(be_depended)):
        if be_depended[j][0] == i + 1:
            b_d.append(be_depended[j][1])

    if len(b_d) == 0:
        latest_day[i] = n - days[i] + 1
        continue
    latest = 365
    for j in range(0, len(b_d)):
        if latest_day[b_d[j] - 1] - days[i] < latest:
            latest = latest_day[b_d[j] - 1] - days[i]
    latest_day[i] = latest

if is_Finish:
    for i in range(0, m - 1):
        print(earliest_day[i], end=' ')
    print(earliest_day[m - 1])
    for i in range(0, m - 1):
        print(latest_day[i], end=' ')
    print(latest_day[m - 1], end='')
else:
    for i in range(0, m - 1):
        print(earliest_day[i], end=' ')
    print(earliest_day[m - 1], end='')
