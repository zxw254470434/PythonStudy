n, k = map(int, input().split())
kids = [i for i in range(1, n + 1)]
counter = 0
num_del = 0


def is_del(counter, k):
    if counter % k == 0 or counter % 10 == k:
        return True
    return False


while num_del < n - 1:
    for i in range(0, n):
        if kids[i] != 0:
            counter += 1
            if is_del(counter, k):
                kids[i] = 0
                num_del += 1
                if num_del == n - 1:
                    break
for i in range(0, n):
    if kids[i] != 0:
        print(kids[i], end='')
