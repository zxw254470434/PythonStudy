n, k = map(int, input().split())
A = input().split()
weight = 0
counter = 0
for i in range(0, n):
    A[i] = int(A[i])
    weight += A[i]
    if weight >= k:
        counter += 1
        weight = 0
    else:
        if i == n - 1:
            counter += 1

print(counter, end='')
