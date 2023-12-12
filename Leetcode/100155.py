from typing import *


class Solution:
    def getGoodIndices(self, variables: List[List[int]], target: int) -> List[int]:
        res = []
        for i in range(len(variables)):
            a, b, c, m = variables[i][0], variables[i][1], variables[i][2], variables[i][3]
            if (a ** b % 10) ** c % m == target:
                res.append(i)

        return res
