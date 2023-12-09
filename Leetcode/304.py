from ListNode import *
from typing import *


class NumMatrix:
    # 定义：preSum[i][j] 记录 matrix 中子矩阵 [0, 0, i-1, j-1] 的元素和
    def __init__(self, matrix: List[List[int]]):
        m, n = len(matrix), len(matrix[0])
        if m == 0 or n == 0: return
        # 构造前缀和矩阵
        self.perSum = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                # 计算每个矩阵 [0, 0, i, j] 的元素和
                self.perSum[i][j] = self.perSum[i - 1][j] + self.perSum[i][j - 1] + matrix[i - 1][j - 1] - \
                                    self.perSum[i - 1][j - 1]

    # 计算子矩阵 [x1, y1, x2, y2] 的元素和
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        # 目标矩阵之和由四个相邻矩阵运算获得
        return self.perSum[row2 + 1][col2 + 1] - self.perSum[row1][col2 + 1] - self.perSum[row2+1][col1] + \
            self.perSum[row1][col1]
