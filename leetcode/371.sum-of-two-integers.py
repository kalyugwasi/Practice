#
# @lc app=leetcode id=371 lang=python3
#
# [371] Sum of Two Integers
#

# @lc code=start
class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0xffffffff
        while (mask&b)>0:
            a,b=a^b,(a&b)<<1
        return (mask&a) if b>0 else a
# @lc code=end

