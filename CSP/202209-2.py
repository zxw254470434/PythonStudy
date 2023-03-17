# day 图书数量，x 包邮条件
n, x = map(int, input().split())

# 第 b 本书的价格为 a[b-1]
a = list(range(n))
for i in range(0, n):
    a[i] = int(input())

print(a)
