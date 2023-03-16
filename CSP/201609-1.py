n = int(input())
prices = input().split()

max_diff = 0
prices[0] = int(prices[0])
for i in range(1, n):
    prices[i] = int(prices[i])
    if abs(prices[i] - prices[i - 1]) > max_diff:
        max_diff = abs(prices[i] - prices[i - 1])

print(max_diff, end='')
