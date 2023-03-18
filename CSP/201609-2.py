n = int(input())
num_tickets = input().split()
for i in range(0, n):
    num_tickets[i] = int(num_tickets[i])

seats = []
for i in range(1, 97, 5):
    seat = [i, i + 1, i + 2, i + 3, i + 4]
    seats.append(seat)

for i in range(0, n):
    tickets = num_tickets[i]
    result = []
    is_allocation = False
    for j in range(0, 20):
        if len(seats[j]) >= tickets:
            is_allocation = True
            while tickets > 0:
                result.append(seats[j][0])
                seats[j].pop(0)
                tickets -= 1
            break
    if not is_allocation:
        for j in range(0, 20):
            if len(seats[j]) == 0:
                continue
            while tickets > 0:
                result.append(seats[j][0])
                seats[j].pop(0)
                tickets -= 1
                if len(seats[j]) == 0:
                    break
    # 输出结果
    if i != n - 1:
        l = len(result)
        for j in range(0, l):
            if j != l - 1:
                print(result[j], end=' ')
            else:
                print(result[j])
    else:
        l = len(result)
        for j in range(0, l):
            if j != l - 1:
                print(result[j], end=' ')
            else:
                print(result[j], end='')
