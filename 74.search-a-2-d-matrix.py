#
# @lc app=leetcode id=74 lang=python3
#
# [74] Search a 2D Matrix
#

# @lc code=start
class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        l , r = 0 , len(matrix)
        for i in matrix:
            if i[0] > target:
                break
            elif i[0] <= target and i[-1] >= target:
                r = len(i) -1
                while l <= r:
                    m = (l+r) // 2
                    if i[m] > target:
                        r = m -1
                    elif i[m] < target:
                        l = m+1
                    else: return True
        return False

        
# @lc code=end

