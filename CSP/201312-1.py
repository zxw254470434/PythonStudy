n = int(input())
a = input().split()
counter = {}
max = 0
min = 10000
for i in range(0, n):
    a[i] = int(a[i])
    if a[i] not in counter.keys():
        counter[a[i]] = 1
        if 1 > max:
            max = 1
    else:
        temp = counter[a[i]]
        counter[a[i]] = temp + 1
        if temp + 1 > max:
            max = temp + 1

for k, v in counter.items():
    if v == max:
        if k < min:
            min = k

print(min, end='')
