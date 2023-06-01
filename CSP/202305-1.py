n = int(input())
chesses = {}

results = []
for i in range(0, n):
    chess = [input() for j in range(0, 8)]
    chess = tuple(chess)

    result = 0
    if chess not in chesses.keys():
        result = 1
        chesses[chess] = 1
    else:
        result = chesses[chess] + 1
        chesses[chess] = result

    results.append(result)

for i in range(0, n):
    if i != n - 1:
        print(results[i])
    else:
        print(results[i], end='')
