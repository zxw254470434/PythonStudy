# 本题与724题相同
from typing import List

def findMiddleIndex(self, nums: List[int]) -> int:
    length = len(nums)
    left = 0
    allsum = sum(nums)
    for i in range(length):
        if allsum - nums[i] == left * 2:
            return i
        left += nums[i]
    return -1
