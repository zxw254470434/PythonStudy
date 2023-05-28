y = int(input())
d = int(input())


def is_runyear(y):
    if y % 4 == 0 and y % 100 != 0:
        return True
    elif y % 400 == 0:
        return True
    return False


# 非闰年
days_1 = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
# 闰年
days_2 = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

if is_runyear(y):
    sum = 0
    month = 0
    day = 0
    for i in range(0, 12):
        if sum + days_2[i] >= d:
            month = i + 1
            day = d - sum
            break
        sum += days_2[i]
    print(month)
    print(day, end='')
else:
    sum = 0
    month = 0
    day = 0
    for i in range(0, 12):
        if sum + days_1[i] >= d:
            month = i + 1
            day = d - sum
            break
        sum += days_1[i]
    print(month)
    print(day, end='')
