from typing import List


class Solution26:
    def removeDuplicates(self, nums: List[int]) -> int:
        return self.process(nums, 1)

    def process(self, nums: List[int], k: int) -> int:
        idx = 0
        for x in nums:
            if idx < k or nums[idx - k] != x:
                nums[idx] = x
                idx += 1
        return idx
