from ListNode import *
from typing import *


# 使用差分数组
class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        diff = [0] * n
        for i in range(len(bookings)):
            first, last, seats = bookings[i][0] - 1, bookings[i][1] - 1, bookings[i][2]
            diff[first] += seats
            if last + 1 < n:
                diff[last + 1] -= seats

        res = [0] * n
        res[0] = diff[0]
        for i in range(1, n):
            res[i] = res[i - 1] + diff[i]

        return res
