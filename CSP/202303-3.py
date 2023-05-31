n = int(input())
users = [[int(a) for a in input().split()] for i in range(0, n)]
m = int(input())
representations = [input() for i in range(0, m)]

# ord()函数返回字符对应的ascii码
# chr()函数将ascii码转换为字符
# 数字0-9对应的ascii码（10进制）为48-57
# &的ascii码为38，|的ascii码为124,:的ascii码为58，~的ascii码为126

results = []

for i in range(0, m):
    re = representations[i]
    attributes = []
    values = []
    is_equal = []
    length = len(re)
    num_re = 0
    result = []

    if 48 <= ord(re[0]) <= 57:
        attributes.append(int(re[0]))
        values.append(int(re[2]))
        is_equal.append(re[1])
        num_re = 1
    elif re[0] == '&':
        num_re = (length - 1) // 5
        for j in range(2, length, 5):
            attributes.append(int(re[j]))
            values.append(int(re[j + 2]))
            is_equal.append(re[j + 1])
    elif re[0] == '|':
        num_re = (length - 1) // 5
        for j in range(2, length, 5):
            attributes.append(int(re[j]))
            values.append(int(re[j + 2]))
            is_equal.append(re[j + 1])

    # 对每个表达式，依次检测每个用户的每个属性是否符合标准
    if num_re == 1:
        for j in range(0, n):
            dn = users[j][0]
            num_attr = users[j][1]
            length = len(users[j])
            for k in range(2, length, 2):
                if is_equal[0] == ':':
                    if users[j][k] == attributes[0]:
                        if users[j][k + 1] == values[0]:
                            result.append(dn)
                else:
                    if users[j][k] == attributes[0]:
                        if users[j][k + 1] != values[0]:
                            result.append(dn)
    else:
        for j in range(0, num_re):
            for k in range(0, n):
                dn = users[k][0]
                num_attr = users[k][1]
                l = len(users[k])


    results.append(result)

print(results)

for i in range(0, m):
    if i != m - 1:
        length = len(results[i])
        if length == 0:
            print()
        for j in range(0, length):
            if j != length - 1:
                print(results[i][j], end=' ')
            else:
                print(results[i][j])
    else:
        length = len(results[i])
        if length == 0:
            print()
        for j in range(0, length):
            if j != length - 1:
                print(results[i][j], end=' ')
            else:
                print(results[i][j], end='')
