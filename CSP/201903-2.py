n = int(input())

for i in range(0, n):
    re = input()
    for j in range(0, 3):
        if 'x' in re:
            index = re.index('x')
            new_value = int(re[index - 1]) * int(re[index + 1])

        elif '/' in re:
            index = re.index('/')
            new_value = int(re[index - 1]) // int(re[index + 1])
