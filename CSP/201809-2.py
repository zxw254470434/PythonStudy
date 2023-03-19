n = int(input())
times = set()
t = 0
for i in range(0, n):
    a, b = map(int, input().split())
    for j in range(a, b):
        times.add(j + 0.5)

for i in range(0, n):
    c, d = map(int, input().split())
    for j in range(c, d):
        if j + 0.5 in times:
            t += 1

print(t, end='')
