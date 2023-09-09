from typing import List


def findNonMinOrMax(nums: List[int]):
    min_num = min(nums)
    max_num = max(nums)
    for elem in nums:
        if elem != min_num and elem != max_num:
            return elem
    return -1


nums = [1, 2, 3]
print(findNonMinOrMax(nums))
