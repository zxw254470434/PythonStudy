from typing import List


class Solution88:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        res = []
        p1, p2 = 0, 0
        while p1 < m or p2 < n:
            if p1 == m:
                res.append(nums2[p2])
                p2 += 1
            elif p2 == n:
                res.append(nums1[p1])
                p1 += 1
            elif nums1[p1] < nums2[p2]:
                res.append(nums1[p1])
                p1 += 1
            else:
                res.append(nums2[p2])
                p2 += 1

        nums1[:] = res
