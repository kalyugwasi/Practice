#
# @lc app=leetcode id=633 lang=python3
#
# [633] Sum of Square Numbers
#

# @lc code=start
import math
class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        if c ==0:
            return True
        roots = {0:0}
        for i in range(c+1):
            a = i**2
            if a>c:
                break
            roots[a] = 0
        print(roots)
        for i in roots.keys():
            if i and c-i in roots.keys():
                return True
        return False
# @lc code=end

