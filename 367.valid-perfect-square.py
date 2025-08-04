#
# @lc app=leetcode id=367 lang=python3
#
# [367] Valid Perfect Square
#

# @lc code=start
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        l,r = 0, num
        result = 0
        while l <= r:
            m = l + (r - l) // 2
            if m*m > num:
                r = m-1
            elif m*m <num:
                l = m+1
                result = m
            else:
                return True
        return False
        
        
# @lc code=end

