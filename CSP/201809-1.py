n = int(input())
yesterday = input().split()
for i in range(0, n):
    yesterday[i] = int(yesterday[i])

today = [0] * n

today[0] = (yesterday[0] + yesterday[1]) // 2
today[n - 1] = (yesterday[n - 2] + yesterday[n - 1]) // 2

for i in range(1, n - 1):
    today[i] = (yesterday[i - 1] + yesterday[i] + yesterday[i + 1]) // 3

for i in range(0, n):
    if i != n - 1:
        print(today[i], end=' ')
    else:
        print(today[i], end='')
