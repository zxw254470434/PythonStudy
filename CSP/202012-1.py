n = int(input())

y = 0
for i in range(0, n):
    w_i, score_i = map(int, input().split())
    y += w_i * score_i

print(max(0, y), end='')
