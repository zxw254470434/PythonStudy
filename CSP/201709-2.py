N, K = map(int, input().split())
# N个钥匙，编号1-N
keys = list(range(1, N + 1))
# 表示存取钥匙的事件
teachers = []

for i in range(0, K):
    w, s, c = map(int, input().split())
    teachers.append([w, s, s + c])

# 待处理事件 [time,‘put’,key]
events = []

for i in range(0, K):

    key = teachers[i][0]
    get_time = teachers[i][1]
    put_time = teachers[i][2]

    # 存get_time
    l = len(events)
    if l == 0:
        events.append([get_time, 'get', key])
    else:
        l = len(events)
        index = 0
        for j in range(0, l):
            if get_time > events[j][0]:
                index += 1
                continue
            elif get_time < events[j][0]:
                break
            elif get_time == events[j][0]:
                if events[j][1] == 'put':
                    index += 1
                elif events[j][1] == 'get':
                    break
        if index == l:
            events.append([get_time, 'get', key])
        else:
            events.insert(index, [get_time, 'get', key])

    # 存put_time
    l = len(events)
    index = 0
    for j in range(0, l):
        if put_time > events[j][0]:
            index += 1
            continue
        elif put_time < events[j][0]:
            break
        elif put_time == events[j][0]:
            if events[j][1] == 'put':
                if key < events[j][2]:
                    break
                elif key > events[j][2]:
                    index += 1
            elif events[j][1] == 'get':
                break
    if index == l:
        events.append([put_time, 'put', key])
    else:
        events.insert(index, [put_time, 'put', key])

for i in range(0, 2 * K):
    state = events[i][1]
    key = events[i][2]
    if state == 'get':
        index = keys.index(key)
        keys[index] = 0
    else:
        for j in range(0, N):
            if keys[j] == 0:
                keys[j] = key
                break

for i in range(0, N - 1):
    print(keys[i], end=' ')
print(keys[N - 1], end='')
