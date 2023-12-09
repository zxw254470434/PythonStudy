from ListNode import *
from typing import *


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        # 先沿对角线镜像对称二维矩阵
        for i in range(n):
            for j in range(i, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        # 然后反转二维矩阵的每一行。[::-1] 是 Python 中的列表切片语法，[::-1] 表示从列表末尾到开头的逆序
        for i in range(n):
            matrix[i] = matrix[i][::-1]
