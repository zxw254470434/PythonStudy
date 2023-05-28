n = int(input())
locations = set()
for i in range(0, n):
    x, y = input().split()
    locations.add((int(x), int(y)))

scores = [0, 0, 0, 0, 0]
for point in locations:
    x, y = point[0], point[1]
    if (x, y + 1) not in locations:
        continue
    if (x, y - 1) not in locations:
        continue
    if (x + 1, y) not in locations:
        continue
    if (x - 1, y) not in locations:
        continue

    score = 0
    if (x - 1, y - 1) in locations:
        score += 1
    if (x - 1, y + 1) in locations:
        score += 1
    if (x + 1, y - 1) in locations:
        score += 1
    if (x + 1, y + 1) in locations:
        score += 1

    scores[score] += 1

for i in range(0, 4):
    print(scores[i])
print(scores[4], end='')
