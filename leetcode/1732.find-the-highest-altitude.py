#
# @lc app=leetcode id=1732 lang=python3
#
# [1732] Find the Highest Altitude
#

class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        n = len(gain)
        pre = [0]*n
        pre[0] = gain[0]
        res = 0
        for i in range(1,n):
            pre[i] += pre[i-1]+gain[i]
        return max(max(pre),res)

# @lc code=end

