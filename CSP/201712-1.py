n = int(input())
nums = input().split()
for i in range(0, n):
    nums[i] = int(nums[i])

nums.sort()

min_diff = nums[1] - nums[0]

for i in range(2, n):
    if nums[i] - nums[i - 1] < min_diff:
        min_diff = nums[i] - nums[i - 1]

print(min_diff, end='')
