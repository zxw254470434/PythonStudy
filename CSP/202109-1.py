n = int(input())

B = input().split()
for i in range(0, n):
    B[i] = int(B[i])

B_max = sum(B)


for i in range(n - 1, 0, -1):
    if B[i] == B[i - 1]:
        B[i] = 0

B_min = sum(B)

print(B_max)
print(B_min, end='')