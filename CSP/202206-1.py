import math

# n个整数
n = int(input())
a = list(map(int, input().split()))

# 求 a 的均值
a_mean = sum(a) / n

# 求方差
variance_sum = 0
for i in range(0, n):
    variance_sum += (a[i] - a_mean) ** 2
d_a = variance_sum / n
sqrt_d_a = math.sqrt(d_a)

# 求 f(ai)
f = list(range(n))

for i in range(0, n):
    f[i] = (a[i] - a_mean) / sqrt_d_a
    if i != n - 1:
        print(f[i])
    else:
        print(f[i], end='')
