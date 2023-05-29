n, k = map(int, input().split())

# 使用集合存储被赋值过的变量的下标
varriables = {0}

# 右值未被初始化问题的赋值语句条数
counter = 0

for i in range(0, k):
    xi, yi = map(int, input().split())
    if yi not in varriables:
        counter += 1
    varriables.add(xi)

print(counter, end='')
