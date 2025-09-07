#
# @lc app=leetcode id=202 lang=python3
#
# [202] Happy Number
#

# @lc code=start
class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        while True:
            if n == 1:
                return True
            elif n in seen:
                return False
            else:
                seen.add(n)
                n = sum(int(i)**2 for i in str(n))
# @lc code=end

