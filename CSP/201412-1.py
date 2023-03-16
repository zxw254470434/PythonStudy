n = int(input())
number = input().split()
counter = {}
for i in range(0, n):
    number[i] = int(number[i])
    if number[i] not in counter.keys():
        counter[number[i]] = 1
        if i != n - 1:
            print(1, end=' ')
        else:
            print(1, end='')
    else:
        temp = counter[number[i]]
        counter[number[i]] = temp + 1
        if i != n - 1:
            print(temp + 1, end=' ')
        else:
            print(temp + 1, end='')
