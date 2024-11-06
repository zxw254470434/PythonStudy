from typing import List


class Solution80:
    def removeDuplicates(self, nums: List[int]) -> int:
        return self.process(nums, 2)

    def process(self, nums: List[int], k: int) -> int:
        idx = 0
        for x in nums:
            if idx < k or nums[idx - k] != x:
                nums[idx] = x
                idx += 1
        return idx
