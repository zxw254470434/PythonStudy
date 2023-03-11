from typing import List


def twoSum(self, nums: List[int], target: int) -> List[int]:
    length = len(nums)
    for i in range(length):
        for j in range(i + 1, length):
            if nums[i] + nums[j] == target:
                return [i, j]
    return [-1, -1]


# 使用hash表，查找操作更快
def twoSum1(self, nums: List[int], target: int) -> List[int]:
    hashtable = dict()
    for i, num in enumerate(nums):
        if target - num in hashtable:
            return [hashtable[target - num], i]
        hashtable[nums[i]] = i
    return []
