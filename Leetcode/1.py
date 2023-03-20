from typing import List


class Solution_1:
    def twoSum(nums, target):
        length = len(nums)
        for i in range(length):
            for j in range(i + 1, length):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return [-1, -1]

    # 使用hash表，查找操作更快
    def twoSum1(nums, target):
        hashtable = dict()
        for i, num in enumerate(nums):
            if target - num in hashtable:
                return [hashtable[target - num], i]
            hashtable[num] = i
        return []


nums = [2, 7, 11, 15]
target = 9

print(Solution_1.twoSum(nums, target))
print(Solution_1.twoSum1(nums, target))
