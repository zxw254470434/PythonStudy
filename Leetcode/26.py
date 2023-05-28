from typing import List


class Solution_26:
    def removeDuplicates(nums: List[int]) -> int:
        for i in range(0, len(nums) - 1):
            if nums[i] > nums[i + 1]:
                break


test = Solution_26
nums = [1, 1, 2]
print(test.removeDuplicates(nums))
