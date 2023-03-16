n = int(input())
a = input().split()
for i in range(0, n):
    a[i] = int(a[i])
a.sort()

index_first_positive = 0
for i in range(0, n):
    if a[i] > 0:
        index_first_positive = i
        break

counter = 0
for i in range(0, index_first_positive):
    for j in range(index_first_positive, n):
        if a[i] == -a[j]:
            counter += 1
            break

print(counter, end='')
