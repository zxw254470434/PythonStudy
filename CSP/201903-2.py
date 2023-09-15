n = int(input())

for i in range(n):
    s = input().replace('x', '*').replace('/', '//')
    print("Yes" if eval(s) == 24 else "No")
