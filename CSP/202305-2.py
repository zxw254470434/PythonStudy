n, d = map(int, input().split())
Q = [[int(a) for a in input().split()] for i in range(0, n)]
K = [[int(a) for a in input().split()] for i in range(0, n)]
V = [[int(a) for a in input().split()] for i in range(0, n)]
W = [int(a) for a in input().split()]

K_T = [[K[i][j] for i in range(0, n)] for j in range(0, d)]

Q_K_T = [[sum(map(lambda a: a[0]*a[1], zip(l, s))) for l in zip(*Q)] for s in K_T]
W_Q_K_T = [W[i] * Q_K_T[i] for i in range(0, n)]
result = [[sum(map(lambda a: a[0]*a[1], zip(l, s))) for l in zip(*W_Q_K_T)] for s in V]
print(result)
for i in range(0, n - 1):
    for j in range(0, d - 1):
        print(result[i][j], end=' ')
    print(result[i][d - 1])

for j in range(0, d - 1):
    print(result[n - 1][j], end=' ')
print(result[n - 1][d - 1])
