N, M = map(int, input().split())

max_sub = 0
index = 1
T = 0
for i in range(1, N + 1):
    operation = input().split()
    operation[0] = int(operation[0])

    all_sub = 0
    for j in range(1, M + 1):
        operation[j] = int(operation[j])
        all_sub += operation[j]

    if all_sub < max_sub:
        max_sub = all_sub
        index = i

    T += operation[0] + all_sub

print(T, index, -max_sub, end='')
