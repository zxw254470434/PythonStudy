import math
S = 0
T = int(input())

S_range = [3500, 5000, 8000, 12500, 38500, 58500, 83500]
T_range = [3500, 4955, 7655, 11255, 30755, 44755, 61005]
tax_rate = [0, 0.03, 0.1, 0.2, 0.25, 0.3, 0.35, 0.45]
tax = [0, 45, 300, 900, 6500, 6000, 8750]

i = 0
for i in range(0, 7):
    if T_range[i] >= T:
        break

sum = 0
for j in range(1, i):
    sum += tax[j]

S = math.ceil((T + sum - S_range[i - 1] * tax_rate[i]) / (1 - tax_rate[i]))

print(S, end='')
