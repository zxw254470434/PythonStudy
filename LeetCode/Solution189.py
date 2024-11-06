from typing import List


class Solution189:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        res = [0] * length
        for i in range(length):
            res[(i + k) % length] = nums[i]

        nums[:] = res
