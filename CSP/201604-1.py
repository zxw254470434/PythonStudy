n = int(input())
a = input().split()
for i in range(0, n):
    a[i] = int(a[i])

counter = 0
for i in range(1, n - 1):
    if a[i - 1] < a[i] and a[i] > a[i + 1]:
        counter += 1
    elif a[i - 1] > a[i] and a[i] < a[i + 1]:
        counter += 1

print(counter,end='')