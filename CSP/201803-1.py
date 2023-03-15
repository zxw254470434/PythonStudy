jump = input().split()
n = len(jump)

score = 0
last_score = 0
for i in range(0, n):
    jump[i] = int(jump[i])

    if jump[i] == 1:
        score += 1
        last_score = 1
    elif jump[i] == 2:
        if last_score == 1 or i == 0:
            score += 2
            last_score = 2
        else:
            score += last_score + 2
            last_score += 2

print(score, end='')
