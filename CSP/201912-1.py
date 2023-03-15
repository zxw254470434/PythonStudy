n = int(input())
jump_counter = [0, 0, 0, 0]
# 记录数过多少个有效数字
number = 0
# 报的数字（包含跳过的）
i = 0


def is_jump(n):
    if n % 7 == 0:
        return True
    while n > 0:
        if n % 10 == 7:
            return True
        n = n // 10
    return False


while number < n:
    i += 1
    if is_jump(i):
        index = i % 4
        if index != 0:
            jump_counter[index - 1] += 1
        else:
            jump_counter[3] += 1
    else:
        number += 1

for i in range(0, 4):
    if i != 3:
        print(jump_counter[i])
    else:
        print(jump_counter[i], end='')
