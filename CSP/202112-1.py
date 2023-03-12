n, N = map(int, input().split())

A = input().split()
for i in range(0, n):
    A[i] = int(A[i])

sum = 0
for i in range(0, n):
    if i != n - 1:
        sum += (A[i + 1] - A[i]) * (i + 1)
    else:
        sum += (N - A[i]) * (i + 1)

print(sum, end='')
