#
# @lc app=leetcode id=739 lang=python3
#
# [739] Daily Temperatures
#

# @lc code=start
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        res = [0] * n
        warmest = 0
        for i in range(n-1,-1,-1):
            if (t:=temperatures[i]) >= warmest:
                warmest = t
                continue
            d = 1
            while temperatures[i+d] <= t:
                d += res[i+d]
            res[i] = d
        return res


# @lc code=end

