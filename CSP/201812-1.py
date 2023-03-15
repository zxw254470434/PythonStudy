r, y, g = map(int, input().split())
n = int(input())
T = 0
for i in range(0, n):
    k, t = map(int, input().split())
    if k == 0:
        T += t
    elif k == 1:
        T += t
    elif k == 2:
        T += t + r
    else:
        continue
print(T, end='')
