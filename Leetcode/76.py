from typing import *


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need, window = {}, {}
        for c in t:
            if c in need:
                need[c] += 1
            else:
                need[c] = 1
        valid = 0
        left, right = 0, 0
        start, length = 0, float('inf')

        while right < len(s):
            c = s[right]
            right += 1

            if c in need:
                if c in window:
                    window[c] += 1
                else:
                    window[c] = 1
                if window[c] == need[c]:
                    valid += 1

            while valid == len(need):
                if right - left < length:
                    start = left
                    length = right - left

                d = s[left]
                left += 1
                if d in need:
                    if window[d] == need[d]:
                        valid -= 1
                    window[d] -= 1

        return "" if length == float('inf') else s[start:start + length]
