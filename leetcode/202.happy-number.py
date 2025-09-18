#
# @lc app=leetcode id=202 lang=python3
#
# [202] Happy Number
#

# @lc code=start
seen = set()
class Solution:
    def isHappy(self, n: int) -> bool:
        if n in seen:
            return False
        seen.add(n)
        s = sum(int(i)**2 for i in str(n))
        if s == 1:
            return True
        else:
            return self.isHappy(s)
s = Solution()
print(s.isHappy(10))
# @lc code=end

