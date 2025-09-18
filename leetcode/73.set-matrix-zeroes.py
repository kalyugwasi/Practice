#
# @lc app=leetcode id=73 lang=python3
#
# [73] Set Matrix Zeroes
#

# @lc code=start
from typing import List

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row, col = len(matrix), len(matrix[0])
        rowZero = False
        colZero = False
        for c in range(col):
            if matrix[0][c] == 0:
                rowZero = True
                break
        for r in range(row):
            if matrix[r][0] == 0:
                colZero = True
                break
        for r in range(1, row):
            for c in range(1, col):
                if matrix[r][c] == 0:
                    matrix[r][0] = 0
                    matrix[0][c] = 0
        for r in range(1, row):
            for c in range(1, col):
                if matrix[r][0] == 0 or matrix[0][c] == 0:
                    matrix[r][c] = 0
        if rowZero:
            for c in range(col):
                matrix[0][c] = 0
        if colZero:
            for r in range(row):
                matrix[r][0] = 0

# @lc code=end

