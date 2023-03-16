n = int(input())
nums = input().split()
for i in range(0, n):
    nums[i] = int(nums[i])
nums.sort()

index = -1
for i in range(0, n):
    temp = nums[i]
    less = 0
    great = 0
    for j in range(0, n):
        if nums[j] < temp:
            less += 1
        elif nums[j] > temp:
            great += 1
    if less == great:
        index = i

if index == -1:
    print(-1, end='')
else:
    print(nums[index], end='')
