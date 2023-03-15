n = int(input())

# 计算有多少个50
counter = 0
counter += (n // 50) * 7
# 计算剩下的有多少个30
n = n % 50
counter += (n // 30) * 4
# 计算有多少个10
n = n % 30
counter += n // 10
print(counter, end='')
