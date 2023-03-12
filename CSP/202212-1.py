para_n_i = input().split()
n = int(para_n_i[0])
i = float(para_n_i[1])

income = input().split()
for k in range(0, n + 1):
    income[k] = int(income[k])
    income[k] = income[k] * ((1 + i) ** (-k))

print(sum(income))
