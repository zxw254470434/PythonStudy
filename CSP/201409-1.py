n = int(input())
a = input().split()
counter = 0
for i in range(0, n):
    a[i] = int(a[i])
a.sort()

for i in range(1, n):
    if a[i] - a[i - 1] == 1:
        counter += 1
print(counter, end='')
