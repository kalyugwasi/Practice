#
# @lc app=leetcode id=191 lang=python3
#
# [191] Number of 1 Bits
#

# @lc code=start
class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0
        while n:
            if n%2 == 1:
                res += 1
            n>>=1
        return res
print(Solution().hammingWeight(11))
# @lc code=end

