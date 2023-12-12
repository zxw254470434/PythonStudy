from typing import *


class Solution:
    def countTestedDevices(self, batteryPercentages: List[int]) -> int:
        n = len(batteryPercentages)
        device = 0
        for i in range(n):
            if batteryPercentages[i] > 0:
                device += 1
                for j in range(i + 1, n):
                    if batteryPercentages[j] > 0:
                        batteryPercentages[j] -= 1

        return device
