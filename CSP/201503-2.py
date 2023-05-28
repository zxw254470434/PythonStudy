n = int(input())
nums = input().split()
counter = [0] * 1001
num_number = set()  # 记录有多少个不重复的数字
for i in range(0, n):
    nums[i] = int(nums[i])
    num_number.add(nums[i])
    counter[nums[i]] += 1

for i in range(0, len(num_number)):
    max = 0
    index = 0
    for j in range(1, 1001):
        if counter[j] > max:
            max = counter[j]
            index = j
    counter[index] = 0
    if i != len(num_number) - 1:
        print(index, max)
    else:
        print(index, max, end='')
