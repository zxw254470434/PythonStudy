n = int(input())
m = int(input())
student = list(range(1, n + 1))

for i in range(0, m):
    p, q = map(int, input().split())
    index = student.index(p)
    student.pop(index)
    index += q
    if index == n - 1:
        student.append(p)
    else:
        student.insert(index, p)

for i in range(0, n):
    if i != n - 1:
        print(student[i], end=' ')
    else:
        print(student[i], end='')
