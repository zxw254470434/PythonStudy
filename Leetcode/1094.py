from ListNode import *
from typing import *


class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        nums = [0] * 1001
        diff = [0] * 1001

        for trip in trips:
            val = trip[0]
            i = trip[1]
            j = trip[2] - 1
            diff[i] += val
            diff[j + 1] -= val

        res = [0] * 1001
        res[0] = diff[0]
        for i in range(1001):
            res[i] = res[i - 1] + diff[i]
            if capacity < res[i]:
                return False
        return True
