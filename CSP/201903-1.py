n = int(input())
nums = input().split()
for i in range(0, n):
    nums[i] = int(nums[i])

nums.sort()

min = nums[0]
max = nums[n - 1]
mid = 0
if n % 2 == 0:
    if (nums[n // 2] + nums[n // 2 - 1]) % 2==0:
        mid = (nums[n // 2] + nums[n // 2 - 1]) // 2
    else:
        mid = (nums[n // 2] + nums[n // 2 - 1]) / 2
        mid = round(mid, 1)
else:
    mid = nums[n // 2]

print(max, mid, min, end='')