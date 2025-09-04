#
# @lc app=leetcode id=73 lang=python3
#
# [73] Set Matrix Zeroes
#

# @lc code=start
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row, col = len(matrix), len(matrix[0])
        zrow,zcol = [],[]
        for r in range(row):
            for c in range(col):
                if matrix[r][c] == 0:
                    zrow.append(r)
                    zcol.append(c)
        for r in set(zrow):
            for c in range(col):
                matrix[r][c] = 0
        for r in range(row):
            for c in set(zcol):
                matrix[r][c] = 0
# @lc code=end

