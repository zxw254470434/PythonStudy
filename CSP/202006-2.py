n, a, b = map(int, input().split())
u = {}
for i in range(0, a):
    index, value = map(int, input().split())
    u[index] = value

v = {}
for i in range(0, b):
    index, value = map(int, input().split())
    v[index] = value

result = 0
if a <= b:
    for index, value in u.items():
        if index in v.keys():
            result += value * v[index]
elif a > b:
    for index, value in v.items():
        if index in u.keys():
            result += value * u[index]

print(result, end='')
