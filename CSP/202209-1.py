# n 题目数量，m 神秘数字
n, m = map(int, input().split())

# 用空格分隔的 n 个整数, 依次表示每道选择题的选项数目。
a = list(map(int, input().split()))
#print(a)

# b(i)表示题目a(i)的正确选项
b = list(range(n + 1))

# 辅助数组c(i)表示数组a(i)的前缀乘积
c = list(range(n + 1))
c[0] = 1
temp = 1
for i in range(1, n + 1):
    c[i] = a[i - 1] * temp
    temp = c[i]
#print(c)

# 求b(i)
presum = 0
for i in range(1, n + 1):
    temp = m % c[i]
    b[i] = (temp - presum) // c[i - 1]
    presum = temp

#print(b)

for i in range(1, n + 1):
    print(b[i], end='')
    if i != n:
        print(' ', end='')
