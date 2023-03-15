N = int(input())

T = 0
D = 0
E = [1] * N
e = 0
for i in range(0, N):
    appletree = input().split()
    appletree[0]=int(appletree[0])
    n = appletree[0]
    for j in range(0, n + 1):
        appletree[j] = int(appletree[j])

    # 计算这棵树还剩下多少苹果
    k = n
    sub = 0
    while appletree[k] <= 0:
        sub += appletree[k]
        k -= 1
    T += appletree[k] + sub

    # 判断这棵树的苹果是否掉落，并将结果存储在E中
    # 初始苹果个数
    is_jump = 0
    num_apples = appletree[1]
    for l in range(2, n + 1):
        if appletree[l] <= 0:
            num_apples += appletree[l]
        else:
            if num_apples != appletree[l]:
                is_jump = 1
                E[i] = 0
            num_apples = appletree[l]
    D += is_jump

# 检查是否有3课连续的苹果树发生掉落
if E[N - 1] == 0 and E[0] == 0 and E[1] == 0:
    e += 1
if E[N - 2] == 0 and E[N - 1] == 0 and E[0] == 0:
    e += 1

for i in range(1, N - 1):
    if E[i - 1] == 0 and E[i] == 0 and E[i + 1] == 0:
        e += 1

print(T, D, e, end='')
