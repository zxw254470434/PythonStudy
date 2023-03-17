n = input()
sum = 0
index = [0, 2, 3, 4, 6, 7, 8, 9, 10]
for i in range(0, 9):
    sum += int(n[index[i]]) * (i + 1)

last = sum % 11
if last == 10:
    last = 'X'
last = str(last)

if last == n[12]:
    print('Right', end='')
else:
    print(n[0:12] + last, end='')
