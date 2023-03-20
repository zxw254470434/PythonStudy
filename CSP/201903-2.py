n = int(input())

result = []
for i in range(0, n):
    origin_re = input()
    re = [0]
    for j in range(0, 7):
        re.append(origin_re[j])

    if re[0] == 24:
        result.append('Yes')
    else:
        result.append('No')

for i in range(0, n):
    if i != n - 1:
        print(result[i])
    else:
        print(result[i], end='')
